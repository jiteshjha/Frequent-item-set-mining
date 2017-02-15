import csv
import sys
import operator

def find_frequent_1_itemsets(D, min_sup):

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
        if itemset[item] < min_sup:
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

def generate_association_rules(itemset, min_conf):

    if len(itemset) < 2:
        print "No association rules"
    else:
        D = str(sys.argv[1])
        row_count = 0

        with open(D, 'rb') as f:
            dataset = csv.reader(f)
            row_count = sum(1 for row in dataset)

        print "Minimum Confidence Threshold: ", float("{0:.2f}".format(min_conf/float(row_count)*100)), "%\n"

        print "Association rules:\n"

        for k in range(1, len(itemset)):
            for pair in itemset[k]:
                for i in range(1, len(itemset[k][0][0].split(','))):
                    for item in powerset(pair[0].split(','), i):
                        item_sup = None
                        for j in itemset[i-1]:
                            if j[0] == ",".join(item):
                                item_sup = int(j[1])
                        if item_sup is not None and pair[1]/float(item_sup) >= min_conf/float(row_count):
                                print ",".join(item), "=>", ",".join(list(set(pair[0].split(',')) - set(item))), "Support: ", item_sup, "Confidence: ", float("{0:.2f}".format(pair[1]/float(item_sup)*100)), "%"

def main():

    """
    Input: D, a dataset of transaction
           min_sup, the minimum support count threshold
           min_conf, the minimum confidence threshold
    """

    D = str(sys.argv[1])
    min_sup = int(sys.argv[2])
    min_conf = int(sys.argv[3])

    L1 = find_frequent_1_itemsets(D, min_sup)
    itemset = [L1]

    k = 2

    while True:
        if not itemset[k-2]:
            break

        C = apriori_gen(itemset[k-2], k)
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
            if L[item] < min_sup:
                L.pop(item, None)

        itemset.append(sorted(L.items(), key=operator.itemgetter(0)))
        k += 1

    itemset.pop()
    generate_association_rules(itemset, min_conf)
    print "Result (Item sets):"

    for i in itemset:
        if i:
            print i


if __name__ == "__main__":
    main()
