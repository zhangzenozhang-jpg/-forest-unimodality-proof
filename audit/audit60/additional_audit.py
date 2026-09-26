"""Fresh audit of source provenance and the paper's explicit affine example."""
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

from verify import algebra, choose, inc, row

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'extension60' / 'forest_n60_extension_and_n100_gap'
standalone = Path('C:/Users/Lenovo/Downloads/60点以内全森林单峰_接续证明.md')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = []
for line in (SOURCE / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    digest, name = line.split('  ', 1)
    actual = sha(SOURCE / name)
    assert digest == actual, (name, digest, actual)
    manifest.append(name)

proof = SOURCE / '60点以内全森林单峰_接续证明.md'
assert standalone.read_bytes() == proof.read_bytes()

data = json.loads((SOURCE / 'certificates.json').read_text(encoding='utf-8'))
example = json.loads((SOURCE / 'example_60_33_19.json').read_text(encoding='utf-8'))
record = next(rec for rec in data['cases'] if (rec['n'], rec['alpha'], rec['k']) == (60, 33, 19))
assert record == example
certificate = example['certificate']
n, a, k = 60, 33, 19
v = n - a
keys = [(j, m) for j in range(1, v + 1) for m in range(a - j + 1)]
target_scale = max([1, abs(inc(a, 0, k + 1))] + [abs(inc(m, j, k + 1)) * choose(v, j) for j, m in keys])
assumptions = [r for r in certificate['rows'] if r['name'][0] == 'assumption']
assert len(assumptions) == 1
_, _, assumption_scale = row(n, a, assumptions[0]['name'], keys)
comparison = Fraction(assumptions[0]['mult'] * target_scale, certificate['D'] * assumption_scale)
margin, terms, denominator_digits = algebra(n, a, k, certificate)
constant = margin * target_scale
assert comparison == Fraction(96885639, 100000000)
assert constant == -Fraction(4010142596414187852788421881, 28302876966000000000)
assert constant < -141686748

out = {
    'python': platform.python_version(),
    'platform': platform.platform(),
    'source_manifest_files_checked': len(manifest),
    'source_manifest_all_passed': True,
    'standalone_markdown_equals_archive_copy': True,
    'proof_markdown_sha256': sha(proof),
    'example_identical_to_master_certificate': True,
    'example_terms_including_assumption': terms,
    'example_affine_slope': str(comparison),
    'example_affine_constant': str(constant),
    'example_integer_constant_is_valid': True,
}
(ROOT / 'additional_audit_results.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=2))
