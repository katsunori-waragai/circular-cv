patterns = [
    "opencv-python",
    "opencv-contrib-python",
]

pyproject="pyproject.toml"

version = "4.0.0.21"


def replace_version(line, patterns):
    pos = max([line.find(pat) for pat in patterns])
    new_string = line[:pos] + f'opencv-python=={version}",\n' if pos > -1 else line
    return new_string


olines = []
for line in open(pyproject):
    olines.append(replace_version(line, patterns))

outfile = "pyproject_new.toml"
open(outfile, "wt").writelines(olines)