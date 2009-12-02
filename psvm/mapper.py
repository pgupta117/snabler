#!/usr/bin/env python
# encoding: utf-8

import base64
import cPickle as pickle
import logging
import numpy
import sys

def read_input(file, separator="\t"):
    for line in file:
        yield line.rstrip().split(separator)

def run_mapper(map, separator="\t"):
    data = read_input(sys.stdin,separator)
    for (key,value) in data:
        map(key,value)

def map(key, value):
    key = [float(i) for i in key.split(",")]
    value = [float(i) for i in value.split(",")]
    D = numpy.diag(key)
    A = numpy.matrix(value)
    e = numpy.matrix(numpy.ones(len(A)).reshape(len(A),1))
    E = numpy.matrix(numpy.append(A,-e,axis=1))
    value = base64.b64encode(pickle.dumps((E.T*E, E.T*D*e)))
    print "outputkey\t%s" % ( value )

if __name__ == "__main__":
    run_mapper(map)
