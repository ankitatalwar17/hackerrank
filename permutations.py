# This tool returns successive  length permutations of elements in an iterable.

# If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced 
# in a sorted order.

from itertools import permutations

S = input().split()

if not S[1]:
    S[1] = len(S[0])
for i in sorted(permutations(S[0], int(S[1]))):
    print (''.join(i))
