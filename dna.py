"""
Program to solve the Rosalind problem at rosalind.info/problems/dna/

"""


def count_letters(s):
    """Form a dictionary letter:letter_count from string s."""
    d = dict()
    for l in s:
        if l not in d:
            d[l] = 1
        else:
            d[l] = d[l] + 1
    return d


def display_letters(d):
    """
    Take dict d of letter:letter_count and print counts in
    alphabetical order by letter.
    """
    l = [n for (a, n) in sorted(list(d.items()))]
    print('{0[0]}  {0[1]}  {0[2]}  {0[3]}'.format(l))


def solve_problem(s):
    display_letters(count_letters(s))


def main():
    s = open(input('Location of rosalind_dna.txt?\n> ')).read().strip()
    solve_problem(s)


if __name__ == '__main__':
    main()
