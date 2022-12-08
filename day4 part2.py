def split_in_pairs(list):
    pairs_list = []
    for item in list:
        pairs_list.append(item.replace('\n','').split(','))
    return pairs_list

contained_pars = 0

with open('day4 input.txt', mode='r') as file:
    data_list = file.readlines()

pairs_list = split_in_pairs(data_list)

for assignment1,assignment2 in pairs_list:
    a1_range_start = int(assignment1[:assignment1.find('-')])
    a1_range_end = int(assignment1[assignment1.find('-') + 1:])
    a2_range_start = int(assignment2[:assignment2.find('-')])
    a2_range_end = int(assignment2[assignment2.find('-') + 1:])
    if a1_range_end - a1_range_start < a2_range_end - a2_range_start:
        for i in range(a1_range_start,a1_range_end+1):
            if i in range(a2_range_start, a2_range_end+1):
                contained_pars +=1
                break
    else:
        for i in range(a1_range_start,a1_range_end+1):
            if i in range(a2_range_start, a2_range_end+1):
                contained_pars +=1
                break
    
        

print(contained_pars)

