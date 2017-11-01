# North America/Rocky Mountain 2007 - 3829 Elementary Additions

def gen():
    """
    Generate a list of strings of the form `{}`, `{{}}`,
    `{{},{{}}}`, etc., representing 0 through 15, respectively.
    """
    sets = ['{}', '{{}}']

    for i in range(2, 16):
        sets.append(sets[i - 1][:-1] + ',' + sets[i - 1] + '}')

    return sets


sets = gen()
cases = int(input())

for _ in range(cases):
    n1 = input()
    n2 = input()
    print(sets[sets.index(n1) + sets.index(n2)])
