"""
Program to solve the Rosalind problem at rosalind.info/problems/gc/

"""

def gc_content(s):
    """Return the GC-content (as a percent) of DNA string s."""
    return ((s.count('C') + s.count('G')) / len(s)) * 100


def format_fasta_file(f):
    """
    Takes a file containing DNA strings in FASTA format.
    Outputs a dictionary FASTA_id:DNA_string.

    The file f should be formatted as follows:
        FASTA_id 1
        line 1 of DNA string
        line 2 of DNA string
        ...
        FASTA_id 2
        line 1 of DNA string
        etc.
    """

    s = f.read()
    l = [x.split('\n') for x in s.split('>')]
    l.pop(0)    #get rid of extra ' ' at start of l.
    for x in l: #get rid of '' at the end of each list in l.
        x.pop()

    ids = [x.pop(0) for x in l]
    dna_str = [''.join(x) for x in l]
    return dict(zip(ids, dna_str))


def get_gc_content_dict(fasta_dict):
    """
    Take a dictionary of FASTA_id:DNA_string.
    Return dictionary of FASTA_id:GC-content.
    """
    return {id:gc_content(fasta_dict[id]) for id in fasta_dict}


def find_max_gc_content(gc_content_dict):
    """
    Take a dictionary of FASTA_id:GC-content.
    Returns tuple (FASTA_id, Max_GC_content).
    """
    max_key = max(gc_content_dict, key=gc_content_dict.get)
    return (max_key, gc_content_dict[max_key])


def solve_problem(f):
    """Create file '../output/gc_answer.txt' containing solution."""
    fout = open('../output/gc_answer.txt', 'w')
    gc_content_dict = get_gc_content_dict(format_fasta_file(f))
    max_tuple = find_max_gc_content(gc_content_dict)
    fout.write(max_tuple[0])
    fout.write('\n')
    fout.write(str(max_tuple[1]))
    fout.close()


def main():
    location = '../datasets/rosalind_gc.txt'
    fin = open(location)
    solve_problem(fin)
    fin.close()


if __name__ == '__main__':
    main()
