string = "1 (3 (5)*3 2)*2 7"

timing_list = []

def find_matching_parens(string):
    open_parens = 0

    for i in range(len(string)):
        if string[i] == '(':
            open_parens += 1
        if string[i] == ')':
            open_parens -= 1
        if open_parens == 0:
            return i

def repeat_string(string, amount):
    ret_string = ''
    for i in range(amount):
        ret_string += string[1:]
    return string

def parse_timings(timings):
    repeat_amount = 1
    start_paren_index = 0
    close_paren_index = len(timings)
    if ('(') in timings:
        start_paren_index = timings.find('(')
        close_paren_index = find_matching_parens(timings[start_paren_index:]) + \
              timings.find('(')
        repeat_amount = int(timings[close_paren_index + 2:
                                    timings.find(' ', close_paren_index + 2)])

        return(timings[:start_paren_index] +
               (parse_timings(timings[start_paren_index + 1:close_paren_index]) + ' ') * repeat_amount +
               timings[timings.find(' ', close_paren_index):])
    else:
        return timings

timing_string = parse_timings(string).replace('  ', ' ')
timing_list = list(map(int, timing_string.split(' ')))
print(timing_list)

total_time = 1000
for i in range(total_time):
    
