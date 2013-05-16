from __future__ import division
from trie import Trie
from sys import argv
from time import clock
from random import choice

trie = Trie()
arr = []
n = 1000
if len(argv) > 1:
	n = int(argv[1])

words = [line for line in open("benchmarking/wordlist")][:n]

def insert_trie():
	for i in xrange(n):
		trie.insert(words[i])

def insert_array():
	for i in xrange(n):
		arr.append(words[i])

def trie_autocomplete():
	word = choice(words)[:3]
	trie.autocomplete(word)

def array_autocomplete():
	for i in xrange(n):
		word = choice(words)[:3]
		trie.autocomplete(word)

def timefn(f, times):
	for i in xrange(n):
		total = 0
		for i in xrange(times):
			start = clock()
			f()
			end = clock()
			total += end - start
		return total / times

def benchmark():
	print "array insertion: %.10f" % timefn(insert_array, 5)
	print "trie insertion: %.10f" % timefn(insert_trie, 5)
	print "array autocomplete: %.10f" % timefn(array_autocomplete, 5)
	print "trie autocomplete: %.10f" % timefn(trie_autocomplete, 5)

if __name__ == '__main__':
	benchmark()
