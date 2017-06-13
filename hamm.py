"""
Program to solve the Rosalind problem at rosalind.info/problems/hamm/

"""

def hamm_dist(s1, s2):
    """Return the Hamming distance between the strings s1 and s2."""
    return len([l1 for (l1, l2) in zip(s1, s2) if l1 != l2])


def solve_problem(s1, s2):
    print(hamm_dist(s1, s2))


def main():
    location = input('Location of rosalind_hamm.txt?\n> ')
    f = open(location)
    s1 = f.readline()
    s2 = f.readline()
    solve_problem(s1, s2)


if __name__ == '__main__':
    main()
