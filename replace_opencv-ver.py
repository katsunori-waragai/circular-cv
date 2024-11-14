patterns = [
    "opencv-python",
    "opencv-contrib-python",
]

patterns = {
    "opencv-python": "4.0.0.21",
    "opencv-contrib-python": "4.0.0.21",
    "numpy": "1.22.1",
}

pyproject="pyproject.toml"

def replace_version(line, patterns):
    for pat, version in patterns.items():
        pos = line.find(pat)
        if pos > -1:
            line = line[:pos] + f'{pat}=={version}",\n'
            break
    return line


olines = []
for line in open(pyproject):
    olines.append(replace_version(line, patterns))

outfile = "pyproject_new.toml"
open(outfile, "wt").writelines(olines)