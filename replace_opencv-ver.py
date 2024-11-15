from pathlib import Path
from typing import Dict

def replace_version(line, patterns):
    for pat, version in patterns.items():
        pos = line.find(pat)
        if pos > -1:
            line = line[:pos] + f'{pat}=={version}",\n'
            break
    return line

def replace_dependencies(src: Path, patterns: Dict):
    dst = Path(f"{src.stem}_new.toml")
    backup = Path(f"{src.stem}_backup.toml")
    olines = [replace_version(line, patterns) for line in open(src)]
    open(dst, "wt").writelines(olines)

    if dst.stat().st_size > 0:
        src.rename(backup)
        dst.rename(src)

if __name__ == "__main__":
    patterns = {
        "opencv-python": "4.0.0.21",
        "opencv-contrib-python": "4.0.0.21",
        "numpy": "1.22.1",
    }

    src = Path("pyproject.toml")
    replace_dependencies(src, patterns)
