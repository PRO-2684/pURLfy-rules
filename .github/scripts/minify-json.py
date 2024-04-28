# Adapted from https://github.com/StefanEnsmann/Minify-Json-Action/blob/main/minify.py
from json import dump, load
from os.path import isfile
from os import system

def minify(name):
    in_path = f"{name}.json"
    out_path = f"{name}.min.json"

    if not isfile(in_path):
        print(f"{in_path} is not a file!")
        return
    
    content = None
    print(f"Reading file {in_path}...")
    with open(in_path, "r", encoding="utf-8") as f_in:
        content = load(f_in)

    print(f"Writing file {out_path}...")
    with open(out_path, "w", encoding="utf-8") as f_out:
        dump(content, f_out, ensure_ascii=False, check_circular=False, indent=None, separators=(",", ":"))

    print(f"Adding {out_path} to git...")
    system(f"git add {out_path}")

if __name__ == "__main__":
    with open("./list.json", "r") as f:
        names = load(f)
        for name in names:
            minify(name)
    print('Done! 🎉')
