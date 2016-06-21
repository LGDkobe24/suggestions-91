#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 1
b = 'a'
print "testing module import"


class Test(object):
    def __init__(self, course=None):
        if course is None:
            course = []
        self.course = course
