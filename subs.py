"""
Program to solve the Rosalind problem at rosalind.info/problems/subs/

"""


def find_all_sub(s, sub):
    """
    Returns a list of indices (starting at 1) corresponding to locations
    of all occurences string sub in string s.
    """
    indices = []
    if s.find(sub) == 0:
        indices.append(1)
    i = 1
    while i != 0:
        x = s.find(sub, i)
        if x != -1:
            indices.append(x + 1)
        i = x + 1
    return indices


def format_list_to_str(l):
    """Convert list l into string."""
    return ' '.join(map(str, l))


def solve_problem(s, sub):
    """Create file in cwd 'subs_answer.txt' containing solution."""
    fout = open('subs_answer.txt', 'w')
    l = find_all_sub(s, sub)
    fout.write(format_list_to_str(l))
    fout.close()


def main():
    location = input('Location of rosalind_subs.txt?\n> ')
    fin = open(location)
    s = fin.readline().strip()
    sub = fin.readline().strip()
    solve_problem(s, sub)


if __name__ == '__main__':
    main()
