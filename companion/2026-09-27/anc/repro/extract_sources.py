"""Extract the 32 indexed historical proof documents without running code."""
from pathlib import Path
import argparse,hashlib,io,json,zipfile

HERE=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True,help='New or empty directory')
    args=parser.parse_args();out=args.output.resolve()
    if out.exists() and any(out.iterdir()):parser.error('Output must be new or empty')
    out.mkdir(parents=True,exist_ok=True)
    hashes=json.loads((HERE/'input_sha256.json').read_text())
    index=json.loads((HERE/'source_index.json').read_text(encoding='utf-8'))
    for row in index:
        archives=row['archive'].split('!')
        raw=(HERE/'inputs'/archives[0]).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=hashes[archives[0]]:raise ValueError('Frozen ZIP hash mismatch')
        for member in archives[1:]:
            with zipfile.ZipFile(io.BytesIO(raw))as z:raw=z.read(member)
        name=f"forest_threshold_{row['stage']}_release/{row['source_relative_to_release']}"
        with zipfile.ZipFile(io.BytesIO(raw))as z:data=z.read(name)
        if hashlib.sha256(data).hexdigest()!=row['sha256']:raise ValueError('Proof document hash mismatch')
        dest=(out/row['output_path']).resolve();dest.relative_to(out)
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    print('Extracted and authenticated',len(index),'historical proof documents; no code executed.')

if __name__=='__main__':main()
