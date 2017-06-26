"""
Program to solve the Rosalind problem at rosalind.info/problems/lcsm/

"""

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


# This is VERY smart. use itertools.combinations to grab slice indices- not the substrings.
# Then return all the slices grabbed from itertools.combinations.

def substrings(s):
    """Return (as a generator object) all substrings of string s."""
    for i, j in itertools.combinations(range(len(s) + 1), 2):
        yield s[i:j]


# is there a better way? this calculates all matching substrings for l[0] and l[1].
# can be improved slightly to calculate matching substrings for the two smallest strings in the list l. not sure if it is worth it...
def find_matching_subs(l):
    """
    Take a list of strings l.
    Return the set of all strings that are substrings
    of every string in l.
    """
    s1, s2 = l[0], l[1]
    s1_subs = set(substrings(s1))
    s2_subs = set(substrings(s2))
    subs = s1_subs.intersection(s2_subs)
    not_common_subs = set()
    for x in l:
        for sub in subs:
            if sub not in x:
                not_common_subs.add(sub)
    return subs - not_common_subs


def find_largest_sub(l):
    """
    Take a list of strings l.
    Return the largest string that is a substring of every string in l.
    """
    subs = find_matching_subs(l)
    return max(subs, key=len)


def solve_problem(f):
    """Create file '../output/lcsm_answer.txt' containing solution."""
    fout = open('../output/lcsm_answer.txt', 'w')
    dna_strings = format_fasta_file(f).values()
    largest_common_substr = find_largest_sub(dna_strings)
    fout.write(largest_common_substr)
    fout.close()


def main():
    location = '../datasets/rosalind_lcsm.txt'
    fin = open(location)
    solve_problem(fin)
    fin.close()


if __name__ == '__main__':
    main()
