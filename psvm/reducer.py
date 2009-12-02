#!/usr/bin/env python
# encoding: utf-8

import base64
import cPickle as pickle
import logging
import numpy

import mrtools

def reduce(key, values, mu=0.1):
    sumETE = None
    sumETDe = None
    
    for _, value in values:
        ETE, ETDe = pickle.loads(base64.b64decode(value))
        if sumETE == None:
            sumETE = numpy.matrix(numpy.eye(ETE.shape[1])/mu)
        sumETE += ETE
            
        if sumETDe == None:
            sumETDe = ETDe
        else:
            sumETDe += ETDe

    result = sumETE.I*sumETDe
    print "%s\t%s" % (key, str(result.tolist()))

if __name__ == "__main__":
    mrtools.run_reducer(reduce)
