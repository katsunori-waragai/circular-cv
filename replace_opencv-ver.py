from pathlib import Path


def replace_version(line, patterns):
    for pat, version in patterns.items():
        pos = line.find(pat)
        if pos > -1:
            line = line[:pos] + f'{pat}=={version}",\n'
            break
    return line

if __name__ == "__main__":
    patterns = {
        "opencv-python": "4.0.0.21",
        "opencv-contrib-python": "4.0.0.21",
        "numpy": "1.22.1",
    }

    pyproject = Path("pyproject.toml")
    outfile = Path("pyproject_new.toml")
    olines = [replace_version(line, patterns) for line in open(pyproject)]
    open(outfile, "wt").writelines(olines)

    if outfile.stat().st_size > 0:
        pyproject.rename(Path("pyproject_backup.toml"))
        outfile.rename(Path("pyproject.toml"))
