"""

def powerset(s, k):
    x = len(s)
    powerset = []
    list = None
    for i in range(1, 1 << x):
        list = [s[j] for j in range(x) if (i & (1 << j))]
        if len(list) == k:
            powerset.append(list)

    return powerset


c=['I1', 'I2', 'I4']
k = 2
L = [('I1,I2', 4), ('I1,I3', 4), ('I1,I5', 2), ('I2,I3', 4), ('I2,I4', 2), ('I2,I5', 2)]
subsets = powerset(c, k)



for subset in subsets:

    infrequent_subset = False
    for item in L:
        if set(subset) == set(item[0].split(",")):
            infrequent_subset = True

    if infrequent_subset == False:
        print "false"
        break

print "true"

"""
def powerset(s, k):
    x = len(s)
    powerset = []
    list = None
    for i in range(1, 1 << x):
        list = [s[j] for j in range(x) if (i & (1 << j))]
        if len(list) == k:
            powerset.append(list)

    return powerset

def has_frequent_subset(c, L, k):
    subsets = powerset(c, k)

    for subset in subsets:

        frequent_subset = False
        for item in L:
            if set(subset) == set(item[0].split(",")):
                frequent_subset = True
                break

        if frequent_subset == False:
            return False

    return True

def apriori_gen(L, k):

    C = []
    for l1 in L:
        for l2 in L:

            first_itemlist = l1[0].split(",")
            second_itemlist = l2[0].split(",")

            i = 0
            flag = True
            while i <= k-2-1:
                if first_itemlist[i] != second_itemlist[i]:
                    flag = False
                    break
                i += 1

            if not first_itemlist[k-1-1] < second_itemlist[k-1-1]:
                flag = False

            if flag == True:
                c = sorted(set(first_itemlist) | set(second_itemlist))

                if has_frequent_subset(list(c), L, k-1):
                    C.append(",".join(list(c)))

    return C

k = 3
L = [('I1,I2', 4), ('I1,I3', 4), ('I1,I5', 2), ('I2,I3', 4), ('I2,I4', 2), ('I2,I5', 2)]
print apriori_gen(L, k)

#print has_infrequent_subset(c, L, k)
