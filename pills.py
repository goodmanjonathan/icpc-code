sltn_dict = {}

def solve(whole_amt, half_amt):
    if (whole_amt, half_amt) in sltn_dict:
        return sltn_dict[(whole_amt, half_amt)]

    if whole_amt == 1 and half_amt == 0:
        return 1
    elif whole_amt == 0 and half_amt > 0:
        return 1
    else:
        eat_whole_sltn = solve(whole_amt - 1, half_amt + 1)
        eat_half_sltn = solve(whole_amt, half_amt - 1) if half_amt > 0 else 0
    
        sltn_dict[(whole_amt, half_amt)] = eat_whole_sltn + eat_half_sltn
        return eat_whole_sltn + eat_half_sltn

for i in range(1, 31):
    print(i, '\t:', solve(i, 0))
