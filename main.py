import os
import sys
from pathlib import Path

TEXT = "My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers."

assert 1 <= len(TEXT) <= 280

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
if output_dir is None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
destination = Path(output_dir) / "entry.txt"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
