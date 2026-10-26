"""Optional: make rmd17_ethanol.npz smaller for the web (GitHub refuses files > 100 MB).
Keeps only the arrays used by the notebook, in float32 for coordinates and forces.
Usage: python tools/slim_data.py path/to/rmd17_ethanol.npz content/rmd17_ethanol.npz
"""
import sys
import numpy as np

src, dst = sys.argv[1], sys.argv[2]
d = np.load(src)
np.savez_compressed(
    dst,
    nuclear_charges=d["nuclear_charges"],
    coords=d["coords"].astype(np.float32),
    energies=d["energies"],              # kept in float64: absolute energies are ~ -97 000 kcal/mol
    forces=d["forces"].astype(np.float32),
    old_indices=d["old_indices"],
    old_energies=d["old_energies"],
)
print("written", dst)
