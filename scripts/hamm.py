"""
Program to solve the Rosalind problem at rosalind.info/problems/hamm/

"""

def hamm_dist(s1, s2):
    """Return the Hamming distance between the DNA strings s1 and s2."""
    return len([l1 for (l1, l2) in zip(s1, s2) if l1 != l2])


def solve_problem(s1, s2):
    """Create file '../output/hamm_answer.txt' containing solution."""
    fout = open('../output/hamm_answer.txt', 'w')
    distance = hamm_dist(s1, s2)
    fout.write(str(distance))
    fout.close()


def main():
    location = '../datasets/rosalind_hamm.txt'
    fin = open(location)
    s1 = fin.readline().strip()
    s2 = fin.readline().strip()
    solve_problem(s1, s2)
    fin.close()


if __name__ == '__main__':
    main()
