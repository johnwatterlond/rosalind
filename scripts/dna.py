"""
Program to solve the Rosalind problem at rosalind.info/problems/dna/

"""

def dna_letter_count(dna_string):
    """
    Return a dictionary of dna_letter:count for DNA string dna_string.
    """
    dna_letters = ['A', 'C', 'G', 'T']
    d = dict()
    for letter in dna_letters:
        d[letter] = dna_string.count(letter)
    return d


def display_dna_letters(d):
    """
    Take a dict d of dna_letter:count and print counts in
    alphabetical order.
    """
    ordered_counts = [count for (let, count) in sorted(list(d.items()))]
    return '{0[0]}  {0[1]}  {0[2]}  {0[3]}'.format(ordered_counts)


def solve_problem(s):
    """Create file '../output/dna_answer.txt' containing solution."""
    fout = open('../output/dna_answer.txt', 'w')
    dna_counts = display_dna_letters(dna_letter_count(s))
    fout.write(dna_counts)
    fout.close()


def main():
    location = '../datasets/rosalind_dna.txt'
    fin = open(location)
    dna_string = fin.readline().strip()
    solve_problem(dna_string)
    fin.close()


if __name__ == '__main__':
    main()
