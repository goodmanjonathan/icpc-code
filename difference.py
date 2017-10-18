# 2011 Southeast USA 5773

while True:
    
    try:
        int_list = list(map(int, input().split(' ')))
    except EOFError:
        exit()
    
    iteration_count = 0
    
    def check_equivalent(numlist):
        for i in range(len(numlist)):
            if numlist[i] != numlist[0]:
                return False
        if numlist[0] == 0:
            exit()
        else:
            return True
        
    while not check_equivalent(int_list):
        new_list = []
        for i in range(4):
            new_list.append(abs(int_list[i] - int_list[(i + 1) % 4]))
            
        int_list = new_list
        iteration_count += 1
                
    print(iteration_count)
