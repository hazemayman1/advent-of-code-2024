#################### DAY1 #################
def dist(l1, l2):
    l1.sort()
    l2.sort()
    if len(l1) != len(l2):
        return False
    dist = 0
    for i in range(len(l1)):
        print(l1[i], l2[i])
        dist += abs(l1[i] - l2[i])
    return dist

def similarity(l1, l2):
    l1.sort()
    l2.sort()
    sim = 0
    ptr2 = 0
    numMap = {}
    for num in l1:
        if num in numMap:
            sim += numMap[num]
            continue
        ctr = 0
        while l2[ptr2] <= num:
            if l2[ptr2] == num:
                ctr += 1
            ptr2 += 1
        sim += num * ctr
        numMap[num] = num*ctr
    return sim


# l1 = [3,4,2,1,3,3]
# l2 = [4,3,5,3,9,3]

# print(similarity(l1,l2))
# l1 = []
# l2 = []
# for line in f:
#     l1.append(int(line.split()[0]))  
#     l2.append(int(line.split()[1]))
# print(similarity(l1,l2))

# print(dist(l1,l2))