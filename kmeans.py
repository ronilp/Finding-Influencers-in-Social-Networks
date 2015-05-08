from collections import defaultdict
from math import sqrt
import random
from utilities import KVAL
from database import getClusterCollection
 
def densify(x, n):
    d = [0] * n
    for i, v in x:
        d[i] = v
    return d
 
 
def dist(x, c):
    sqdist = 0.
    for i, v in x:
        sqdist += (v - c[i]) ** 2
    return sqrt(sqdist)
 
 
def mean(xs, l):
    c = [0.] * l
    n = 0
    for x in xs:
        for i, v in x:
            c[i] += v
        n += 1
    for i in xrange(l):
        c[i] /= n
    return c
 
 
def kmeans(k, xs, l, n_iter=10):
    # Initialize from random points.
    centers = [densify(xs[i], l) for i in random.sample(xrange(len(xs)), k)]
    cluster = [None] * len(xs)
 
    for _ in xrange(n_iter):
        for i, x in enumerate(xs):
            cluster[i] = min(xrange(k), key=lambda j: dist(xs[i], centers[j]))
        for j, c in enumerate(centers):
            members = (x for i, x in enumerate(xs) if cluster[i] == j)
            centers[j] = mean(members, l)
 
    return cluster
 
 
if __name__ == '__main__':
    # Cluster a bunch of text documents.
    import re
    import sys
    import glob
    def usage():
        print("usage: %s k docs..." % sys.argv[0])
        print("    The number of documents must be >= k.")
        sys.exit(1)
 
    try:
        k = KVAL
    except ValueError():
        usage()
 
    vocab = {}
    xs = []
    args = []
    for name in glob.glob('./data/*.txt'):
        args.append(name)
    for a in args:
        x = defaultdict(float)
        with open(a) as f:
            for w in re.findall(r"\w+", f.read()):
                vocab.setdefault(w, len(vocab))
                x[vocab[w]] += 1
        xs.append(x.items())
 
    cluster_ind = kmeans(k, xs, len(vocab))
    clusters = [set() for _ in xrange(k)]
    for i, j in enumerate(cluster_ind):
        clusters[j].add(i)
    
    def cleanName(string):
        return string[7:-4]

    collection = getClusterCollection()
    collection.drop()
    for j, c in enumerate(clusters):
        print("cluster %d:" % j)
        array = []
        for i in c:
            print("\t%s" % args[i])
            array.append(args[i])
        array = map(cleanName, array)
        doc = {'cluster' : j, 'pages' : array}
        collection.insert(doc)