# Adapted from https://github.com/StefanEnsmann/Minify-Json-Action/blob/main/minify.py
from json import dump, load
from os.path import isfile
from os import system

def minify(name):
    in_path = '{:}.json'.format(name)
    out_path = '{:}.min.json'.format(name)

    if not isfile(in_path):
        print('{:} is not a file!'.format(in_path))
        return
    
    content = None
    print('Reading file {:}...'.format(in_path))
    with open(in_path, 'r', encoding='utf-8') as f_in:
        content = load(f_in)

    print('Writing file {:}...'.format(out_path))
    with open(out_path, 'w', encoding='utf-8') as f_out:
        dump(content, f_out, ensure_ascii=False, check_circular=False, indent=None, separators=(',', ':'))

    print('Adding {:} to git...'.format(out_path))
    system('git add {:}'.format(out_path))

if __name__ == "__main__":
    with open("./list.json", "r") as f:
        names = load(f)
        for name in names:
            minify(name)
    print('Done! 🎉')
