"""
Program to solve the Rosalind problem at rosalind.info/problems/subs/

"""

def find_all_sub(s, sub):
    """
    Returns a list of indices (starting at 1) corresponding to locations
    of all occurences string sub in string s.
    """
    indices = {s.find(sub, i) for i in range(len(s) + 1) if s.find(sub, i) != -1}
    indices_up_one = [index + 1 for index in indices]
    return sorted(indices_up_one)


def format_list_to_str(l):
    """Convert list l into string with elements sep. by a space."""
    return ' '.join(map(str, l))


def solve_problem(s, sub):
    """Create file '../output/subs_answer.txt' containing solution."""
    fout = open('../output/subs_answer.txt', 'w')
    sub_indices = find_all_sub(s, sub)
    fout.write(format_list_to_str(sub_indices))
    fout.close()


def main():
    location = '../datasets/rosalind_subs.txt'
    fin = open(location)
    s = fin.readline().strip()
    sub = fin.readline().strip()
    solve_problem(s, sub)
    fin.close()


if __name__ == '__main__':
    main()
