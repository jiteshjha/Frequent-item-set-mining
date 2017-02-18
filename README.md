#  Frequent Itemset Mining


Apriori algorithm for discovering frequent itemsets for mining Boolean association rules.

**Motivation** : http://cse.iitkgp.ac.in/~bivasm/uc_notes/07apriori.pdf

**Original Paper** :

> *Rakesh Agrawal and Ramakrishnan Srikant Fast algorithms for mining association rules in large databases. Proceedings of the 20th International Conference on Very Large Data Bases, VLDB, pages 487-499, Santiago, Chile, September 1994.*

##Usage

The algorithm can be executed with (Both minimum support and minimum confidence lie between [0, 1]):

    python apriori.py <data_set> <minimum_support> <minimum_confidence>

Example:

    python apriori.py datasets/retail.csv 0.3 0.6



##Dataset:

`retail.dat` contains the (anonymized) retail market basket data from an anonymous Belgian retail store(Source: http://fimi.ua.ac.be/data/).
Additionally, `retail.dat` was converted into `retail.csv` using `dat2csv.py` provided in the repository.

##To-Do:

* Parallel Partition method for speeding up mining process (Reference : http://ieeexplore.ieee.org/abstract/document/553164/)
