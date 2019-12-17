import os
import numpy as np

from glob import glob


def load_flist(flist, substr='', ext=['.jpg', '.png'], recursive=False):
    if isinstance(flist, list):
        return flist

    if isinstance(flist, np.ndarray):
        return flist

    # flist: image file path, image directory path, text file flist path
    if isinstance(flist, str):
        if os.path.isdir(flist):
            if not recursive:
                _flist = flist
                flist = []
                for _ext in ext:
                    flist += [os.path.abspath(fn) for fn in glob(_flist + '/*%s' %(_ext)) if substr in os.path.basename(fn)]
            else:
                walk = os.walk(flist)
                flist = []
                for parentname, _, filelist in walk:
                    flist += [os.path.abspath(os.path.join(parentname, fn)) for fn in filelist if os.path.splitext(fn)[-1].lower() in ext and substr in fn]

            flist.sort()
            return flist

        if os.path.isfile(flist):
            try:
                flist = np.genfromtxt(flist, dtype=np.str, encoding='utf-8')
                if flist.ndim > 1 :
                    flist = flist[:, 0]
                return flist.tolist()
            except:
                return [flist]

    return []


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str, help="Choose an image folder.")
    parser.add_argument("output", type=str, help="Output flist file")
    parser.add_argument("--keyword", type=str, default='', help="Keyword of image name")
    parser.add_argument("--ext", type=tuple, nargs='+', default=('.png', '.jpg'), help="Extension of image name")
    parser.add_argument("--recursive", action='store_true', help="Recursive to its sub dir")
    args = parser.parse_args()
    return args


def save_flist(flist, fn, substr='', ext=['.jpg', '.png'], recursive=False):
    flist = load_flist(flist, substr, ext, recursive=recursive)
    # with open(fn, "w") as foo:
    #     import ipdb; ipdb.set_trace()
    np.savetxt(fn, flist, fmt="%s")


def make_flist():
    args = parse_args()
    save_flist(args.dir, args.output, substr=args.keyword, ext=args.ext, recursive=args.recursive)
