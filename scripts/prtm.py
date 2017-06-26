"""
Program to solve the Rosalind problem at rosalind.info/problems/prtm/

"""

mass_table = dict([('A', '71.03711'),
 ('C', '103.00919'),
 ('D', '115.02694'),
 ('E', '129.04259'),
 ('F', '147.06841'),
 ('G', '57.02146'),
 ('H', '137.05891'),
 ('I', '113.08406'),
 ('K', '128.09496'),
 ('L', '113.08406'),
 ('M', '131.04049'),
 ('N', '114.04293'),
 ('P', '97.05276'),
 ('Q', '128.05858'),
 ('R', '156.10111'),
 ('S', '87.03203'),
 ('T', '101.04768'),
 ('V', '99.06841'),
 ('W', '186.07931'),
 ('Y', '163.06333')])


def total_weight(prot_string):
    """Return total weight of protien string prot_string."""
    return sum(float(mass_table[letter]) for letter in prot_string)


def solve_problem(prot_string):
    """Create file '../output/prtm_answer.txt' containing solution."""
    fout = open('../output/prtm_answer.txt', 'w')
    fout.write(str(total_weight(prot_string)))
    fout.close()


def main():
    location = '../datasets/rosalind_prtm.txt'
    fin = open(location)
    prot_string = fin.read().strip()
    solve_problem(prot_string)
    fin.close()


if __name__ == '__main__':
    main()
