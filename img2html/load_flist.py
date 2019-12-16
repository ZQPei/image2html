import os
import numpy as np


def load_flist(flist, substr='', ext=['.jpg', '.png']):
    if isinstance(flist, list):
        return flist

    if isinstance(flist, np.ndarray):
        return flist

    # flist: image file path, image directory path, text file flist path
    if isinstance(flist, str):
        if os.path.isdir(flist):
            # flist = list(glob(flist + '/*.jpg')) + list(glob(flist + '/*.png'))
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