import csv
import sys
import operator
import time

start_time = time.clock()

def find_frequent_1_itemsets(D, min_sup, row_count):

    dataset = None
    itemset = {}

    """
        Calculate candidate itemsets
    """
    with open(D, 'rb') as f:
        dataset = csv.reader(f)
        for i in dataset:
            for j in i:
                if j in itemset:
                    itemset[j.strip()] += 1
                else:
                    itemset[j.strip()] = 1

    """
        Calculate frequent itemsets
    """
    for item in itemset.copy():
        if itemset[item]/float(row_count) < min_sup:
            itemset.pop(item, None)

    return sorted(itemset.items(), key=operator.itemgetter(0))

"""
    Calculates powerset with set size = k
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

def apriori_gen(L, k, row_count):

    C = []
    for l1 in L:
        for l2 in L:

            first_itemlist = l1[0].split(",")
            second_itemlist = l2[0].split(",")
            #print first_itemlist, second_itemlist
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

def generate_association_rules(itemset, min_conf, row_count):

    if len(itemset) < 2:
        print "No association rules"
    else:
        D = str(sys.argv[1])

        print "\nMinimum Confidence Threshold: ", min_conf*100, "%\n"

        print "Association rules:\n"

        for k in range(1, len(itemset)):
            for pair in itemset[k]:
                for i in range(1, len(itemset[k][0][0].split(','))):
                    for item in powerset(pair[0].split(','), i):
                        item_sup = None
                        for j in itemset[i-1]:
                            if j[0] == ",".join(item):
                                item_sup = int(j[1])
                        if item_sup is not None and pair[1]/float(item_sup) >= min_conf:
                                print ",".join(item), "=>", ",".join(list(set(pair[0].split(',')) - set(item))), "Support: ", float("{0:.2f}".format(float(item_sup)/row_count))*100, "%", "Confidence: ", float("{0:.2f}".format(pair[1]/float(item_sup)*100)), "%"

def main():

    """
    Input: D, a dataset of transaction
           min_sup, the minimum support count threshold
           min_conf, the minimum confidence threshold
    """

    D = str(sys.argv[1])
    min_sup = float(sys.argv[2])
    min_conf = float(sys.argv[3])

    row_count = 0

    with open(D, 'rb') as f:
        dataset = csv.reader(f)
        row_count = sum(1 for row in dataset)

    L1 = find_frequent_1_itemsets(D, min_sup, row_count)
    itemset = [L1]



    k = 2

    while True:
        if not itemset[k-2]:
            break

        C = apriori_gen(itemset[k-2], k, row_count)
        L = {}


        with open(D, 'rb') as f:
            dataset = csv.reader(f)
            for t in dataset:
                for c in C:
                    if set(c.split(",")).issubset(set(t)):
                        if c in L:
                            L[c] += 1
                        else:
                            L[c] = 1

        for item in L.copy():
            if L[item]/float(row_count) < min_sup:
                L.pop(item, None)

        itemset.append(sorted(L.items(), key=operator.itemgetter(0)))
        k += 1

    itemset.pop()
    generate_association_rules(itemset, min_conf, row_count)
    print "\nResultant Item sets:"

    for k in range(1, len(itemset)):
        print "\n", k, "-itemsets:\n"
        for item in itemset[k]:
            print item[0], "| Support ", float("{0:.2f}".format(item[1]/float(row_count)))*100, "%"


if __name__ == "__main__":
    main()

print "\nProgram Execution Time: ",time.clock() - start_time, " seconds"
