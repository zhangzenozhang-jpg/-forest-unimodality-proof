"""Independent all-unlabelled-forest structural check through order ten.

Tree/forest generation and independent-set enumeration do not use the supplied
certificate generator. Supplied row implementation is only called after exact
graph counts are independently constructed.

Usage (Python 3.10+, without -O; standard library only):
  python finite_exhaustive.py
  python finite_exhaustive.py --verifier /path/to/verify.py
  python finite_exhaustive.py --output /path/to/new_results.json

By default, use ../audit60/verify.py in the development workspace; otherwise
find inputs/forest_n60_extension_and_n100_gap.zip under an ancestor of this
script, extract only its original verify.py to a temporary directory, and
import it with its real __file__ preserved. No source code is rewritten.
Results go to standard output unless --output is explicitly supplied.
"""
import argparse, collections, hashlib, importlib.util, json, math, tempfile, time, zipfile
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parent

@contextmanager
def load_verifier(explicit):
    """Load the original module from a file or a safely extracted ZIP member."""
    if explicit is not None:
        source=explicit.expanduser().resolve()
        if not source.is_file():
            raise FileNotFoundError(f'Verifier file does not exist: {source}')
        info={'kind':'explicit_file','source':str(source)}
    else:
        source=ROOT.parent/'audit60'/'verify.py'
        info={'kind':'workspace_file','source':str(source)}
        if not source.is_file():
            source=None
    with tempfile.TemporaryDirectory(prefix='forest_finite_verifier_') as tmp:
        if source is None:
            archive=next((p/'inputs'/'forest_n60_extension_and_n100_gap.zip'
                          for p in (ROOT,*ROOT.parents)
                          if (p/'inputs'/'forest_n60_extension_and_n100_gap.zip').is_file()),None)
            if archive is None:
                raise FileNotFoundError(
                    'No local audit60/verify.py or package inputs ZIP found. '
                    'Supply --verifier /path/to/the/original/verify.py.')
            with zipfile.ZipFile(archive) as zf:
                members=[name for name in zf.namelist()
                         if name.replace('\\','/').rsplit('/',1)[-1]=='verify.py']
                if len(members)!=1:
                    raise ValueError(f'Expected one verify.py in {archive}; found {len(members)}')
                # Write to a fixed local basename instead of trusting an archive path.
                source=Path(tmp)/'verify.py'
                source.write_bytes(zf.read(members[0]))
            info={'kind':'package_zip','source':str(archive),'member':members[0]}
        info['sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
        spec=importlib.util.spec_from_file_location('original_verify',source)
        if spec is None or spec.loader is None:
            raise ImportError(f'Cannot load verifier: {source}')
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        yield module,info

def c(n,k):
    return math.comb(n,k) if 0 <= k <= n else 0

def adj_of(rooted):
    adj=[]
    def visit(t,parent):
        i=len(adj); adj.append([])
        if parent is not None: adj[i].append(parent);adj[parent].append(i)
        for child in t: visit(child,i)
    visit(rooted,None)
    return adj

def canon(adj,u,p=-1):
    return tuple(sorted(canon(adj,w,u) for w in adj[u] if w != p))

def multisets(items,target,start=0):
    if target == 0:
        yield ()
        return
    for idx in range(start,len(items)):
        size,tree=items[idx]
        if size > target: break
        for tail in multisets(items,target-size,idx):
            yield (tree,)+tail

def generate_trees(maxn):
    rooted=[]; unrooted=[]; counts={}
    for n in range(1,maxn+1):
        new=list(multisets(rooted,n-1))
        uniques={}
        for t in new:
            adj=adj_of(t)
            key=min(canon(adj,u) for u in range(n))
            uniques[key]=t
        rooted += [(n,t) for t in new]
        unrooted += [(n,t) for t in sorted(uniques)]
        counts[n]=(len(new),len(uniques))
    return unrooted,counts

def row_names(n,a):
    v=n-a
    for r in range(2,v+1):
        for tag in ('count','mean','union','edge_lower','edge_upper'):
            yield (tag,r)
        for h in range(a): yield ('private',r,h)
        for h in range(a-r+2):
            for tag in ('tail','release_upper','tail_upper'):yield(tag,r,h)
    for r in range(2,a+1):yield ('path',r)
    for l in range(a+1):
        for r in range(min(v,a-l)):
            if v-r-max(0,l-a+v)>=0:yield('hall',r,l)

def graph_checks(forest,ver):
    adj=[]
    for t in forest:
        shift=len(adj)
        adj += [[v+shift for v in ns] for ns in adj_of(t)]
    n=len(adj);allmask=(1<<n)-1
    neighbors=[sum(1<<v for v in ns)for ns in adj]
    independent=[0];independent_set={0}
    for mask in range(1,1<<n):
        bit=mask&-mask;u=bit.bit_length()-1;rest=mask^bit
        if rest in independent_set and not(neighbors[u]&rest):
            independent.append(mask)
            independent_set.add(mask)
    a=max(x.bit_count()for x in independent);v=n-a;delta=a-v
    coeff=[0]*(a+1)
    for mask in independent:coeff[mask.bit_count()]+=1
    if v==0:return n,0
    maximal=[mask for mask in independent if mask.bit_count()==a]
    def induced_edges(mask):
        return sum((neighbors[u]&mask).bit_count()for u in range(n)if mask>>u&1)//2
    I=min(maximal,key=lambda mask:induced_edges(allmask^mask));Y=allmask^I
    e=induced_edges(Y)
    assert e<=max(0,delta-1),(n,forest,'sparse',e,delta)
    counts=collections.Counter()
    for J in independent:
        if J and J & I == 0:
            union=0
            for u in range(n):
                if J>>u&1:union |= neighbors[u]
            j=J.bit_count();m=(I&~union).bit_count()
            assert j+m<=a
            counts[j,m]+=1
    keys=[(j,m)for j in range(1,v+1)for m in range(a-j+1)]
    vals=[counts[key]for key in keys]
    for r in range(a+1):
        assert coeff[r]==c(a,r)+sum(c(m,r-j)*t for (j,m),t in zip(keys,vals))
        assert coeff[r]>=c(n-r+1,r)
    for k in range(a):assert (k+1)*coeff[k+1] <= 2*(a-k)*coeff[k]
    numrows=0
    for name in row_names(n,a):
        ar,b,scale=ver.row(n,a,name,keys)
        lhs=sum(x*y for x,y in zip(ar,vals))
        assert lhs<=b,(n,forest,a,name,lhs,b,counts)
        numrows+=1
    return n,numrows

def run(ver,source_info):
    start=time.time();trees,tree_counts=generate_trees(10)
    expected_unrooted=[1,1,1,2,3,6,11,23,47,106]
    assert [tree_counts[n][1]for n in range(1,11)]==expected_unrooted
    result={'status':'PASS','max_order':10,'verifier':source_info,'tree_counts':tree_counts,'forest_counts':{},'row_checks':0}
    for n in range(1,11):
        total=0
        for forest in multisets(trees,n):
            _,rows=graph_checks(forest,ver)
            total+=1;result['row_checks']+=rows
        result['forest_counts'][n]=total
    result['total_forests']=sum(result['forest_counts'].values())
    assert result['total_forests']==637
    assert result['row_checks']==45529
    result['seconds']=round(time.time()-start,3)
    return result

def main():
    if not __debug__:
        raise RuntimeError('Run this exact check without Python -O.')
    parser=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--verifier',type=Path,help='Explicit path to the original finite verify.py')
    parser.add_argument('--output',type=Path,help='Write result JSON here (explicitly overwrites this file); otherwise print only')
    args=parser.parse_args()
    with load_verifier(args.verifier) as (ver,source_info):
        result=run(ver,source_info)
    rendered=json.dumps(result,indent=2)+'\n'
    if args.output is not None:
        output=args.output.expanduser().resolve()
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(rendered,encoding='utf-8')
    print(rendered,end='')

if __name__=='__main__':main()
