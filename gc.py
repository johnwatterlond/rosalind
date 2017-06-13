"""
Program to solve the Rosalind problem at rosalind.info/problems/gc/

"""

def gc_content(s):
    """Return the GC-content (as a percent) of DNA string s."""
    return ((s.count('C') + s.count('G')) / len(s)) * 100



f = open('/home/john/Downloads/rosalind_gc.txt')
s = f.read()
l = [x.split('\n') for x in s.split('>')]
l.pop(0)
for x in l:
    x.pop()
ids = [x.pop(0) for x in l]
dna_str = [''.join(x) for x in l]


def solve_problem(f):
    """
    Takes a file containing a string in FASTA format and returns
    the id with the highest GC-content and its GC-content.
    """

    s = f.read()
    l = [x.split('\n') for x in s.split('>')]
    l.pop(0)    #get rid of extra ' ' at start of l.
    for x in l: #get rid of '' at the end of each list in l.
        x.pop()
    ids = [x.pop(0) for x in l]
    dna_str = [''.join(x) for x in l]
    gc_contents = [gc_content(x) for x in dna_str]
    id_gc_tuples = [x for x in zip(gc_contents, ids)]
    d = dict(zip(id_gc_tuples, dna_str))
    t = max(d.items())[0]
    print('{0[1]}\n{0[0]}'.format(t))


def main():
    location =  input('Location of rosalind_gc.txt?\n> ')
    f = open(location)
    solve_problem(f)


if __name__ == '__main__':
    main()
