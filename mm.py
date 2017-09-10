#!/usr/bin/env python

import os, sys

class A(object):
    def __init__(self):
        print 'this is instance of class A'

    def __call__(self):
        print 'instance called'
