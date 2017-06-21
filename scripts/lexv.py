"""
Program to solve the Rosalind problem at rosalind.info/problems/lexv/

"""

import itertools


#need to understand the yield from statement.
#also note use of tuple sorting which is possibly different than string sorting.
def perms_up_to_n_from_m(n, m):
    """
    Return all perms of size up to n from the numbers in range(m).
    Used later when converting numbers to letters.
    """
    yield from sorted(string
    for i in range(1, n + 1)
    for string in itertools.product(range(m), repeat=i))


def create_dict(s):
    """
    Create dictionary from string.
    'DNA'--> {0:'D', 1:'N', 2:'A'}
    """
    return dict(zip(range(len(s)), s))


def nums_to_letters(s, n):
    d = create_dict(s)
    m = len(s)
    perm_nums = list(perms_up_to_n_from_m(n, m))

    letter_perms = [list(x) for x in perm_nums]
    for x in letter_perms:
        for i, num in enumerate(x):
            x[i] = d[num]

    return [''.join(x) for x in letter_perms]


def solve_problem(s, n):
    """Create file '../output/lexv_answer.txt' containing solution."""
    fout = open('../output/lexv_answer.txt', 'w')
    letter_perms = nums_to_letters(s, n)
    for perm in letter_perms:
        fout.write(perm)
        fout.write('\n')
    fout.close()


def main():
    location = '../datasets/rosalind_lexv.txt'
    fin = open(location)
    s_unformatted = fin.readline().strip()
    s = s_unformatted.replace(' ', '')
    n = int(fin.readline())
    solve_problem(s, n)


if __name__ == '__main__':
    main()
