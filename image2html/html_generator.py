"""
html_generator.py
Author : pzq

To display a single image folder or Compare multiple image folders.
For a single folder or a single flist file, generate a html of all image files.
For multiple folders or flist files, generate a html to compare them. It is recommended that file sequences should match.
"""


import datetime
import dominate
from dominate.tags import *
import os
import glob
import numpy as np

from .flist import load_flist


class HTML(object):
    def __init__(self, html_title):
        self.doc = dominate.document(title=html_title)
        self.doc.add(h1(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")))


    def add_header(self, string):
        self.doc.add(h3(string))

    def add_table(self, border=1):
        self.t = table(border=border, style="table-layout: fixed;")
        self.doc.add(self.t)

    def save(self, fn):
        with open(fn, 'w') as foo:
            foo.write(self.doc.render())


class HtmlGenerator(object):
    def __init__(self, args):
        # self.mode = args.mode
        self.dirs = args.dirs
        self.keyword = args.keyword
        self.ext = args.ext
        self.width = args.width
        self.output = args.output


        assert self.dirs, "Use `image2html --help` to get help!"

        self.n = len(self.dirs)
        if self.n == 1:
            self.mode = "single"
        else:
            self.mode = "multiple"

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] * self.n
        if not isinstance(self.ext, list):
            self.ext = [self.ext] * self.n

        self._check()

        self.num_images = 0
        self._parse_flists()


        self._init_html()


    def generate(self):
        if self.mode is 'single':
            self._display_single()
        elif self.mode is 'multiple':
            self._compare_multiple()
        self.html.save(self.output)


    def _check(self):
        print(self.mode, self.n, self.keyword, self.ext, self.dirs)
        if isinstance(self.keyword, list):
            assert len(self.keyword) == self.n, "Arg error: keyword"
        if isinstance(self.ext, list):
            assert len(self.ext) == self.n, "Arg error: ext"
        for dn in self.dirs:
            assert os.path.isdir(dn), "Error: Folder %s not found"%(dn)


    def _parse_flists(self):
        flists = []

        for i in range(self.n):
            flist = load_flist(self.dirs[i], self.keyword[i], self.ext[i])
            if self.num_images == 0:
                self.num_images = len(flist)
            elif self.num_images != len(flist):
                raise AssertionError("Num of images should equal!")
            flists += [flist]

        self.flists = flists


    def _init_html(self):
        self.html = HTML(self.mode)


    def _display_single(self, nrow=4):
        '''
            for a single image dir
        '''
        flist = self.flists[0]

        idx = 0
        while idx < self.num_images:
            self.html.add_table()
            with self.html.t:
                with tr():
                    for _ in range(nrow):
                        with td(style="word-wrap: break-word;", halign="center", valign="top"):
                            with p():
                                basename = os.path.basename(flist[idx])
                                linker = flist[idx]
                                with a(href=linker):
                                    img(style="width:%dpx" %(self.width), src=linker)
                                    idx += 1
                                br()
                                p(basename)
                                if idx == self.num_images:
                                    break


    def _compare_multiple(self):
        '''
            for multiple image dirs with same image number
        '''
        flists = self.flists
        num_dirs = self.n
        num_images = self.num_images

        for idx in range(num_images):
            self.html.add_header(str(idx))
            self.html.add_table()
            with self.html.t:
                with tr():
                    for d in range(num_dirs):
                        with td(style="word-wrap: break-word;", halign="center", valign="top"):
                            with p():
                                linker = flists[d][idx]
                                with a(href=linker):
                                    img(style="width:%dpx" %(self.width), src=linker)
                                br()
                                p(os.path.basename(flists[d][idx]))



def build_html_generator(args):
    return HtmlGenerator(args)