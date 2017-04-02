#!/usr/bin/python

###############################################
# module: rand_bst.py
# description: starter code for HW09
# bugs to vladimir dot kulyukin at usu dot edu
###############################################

###############################################
# 1. the limit approaches zero
# 2.
#
#
#









from BSTNode import BSTNode
from BSTree import BSTree
import random
import matplotlib.pyplot as plt
import numpy as np

def gen_rand_bst(num_nodes, a, b):
    bsTree  = BSTree()
    for x in xrange(num_nodes):
        bsTree.insertKey(np.random.randint(a,b+1))
    return bsTree
    pass

def estimate_list_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b):
    countList = 0
    bsList = []
    for x in xrange(num_trees):
        temp = gen_rand_bst(num_nodes, a, b)
        if temp.isList():
            countList = countList + 1
            bsList.append(temp)
    return (float(countList)/float(num_trees), bsList)


def estimate_list_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_trees, a, b):
    d = {}
    for num_nodes in xrange(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_list_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b)
    return d

def estimate_balance_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b):
    countList = 0
    bsList = []
    for x in xrange(num_trees):
        temp = gen_rand_bst(num_nodes, a, b)
        if temp.isEmpty() == False:
            if temp.isBalanced():
                countList = countList + 1
                bsList.append(temp)
    return (float(countList)/float(num_trees), bsList)

def estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_trees, a, b):
    d = {}
    for num_nodes in xrange(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_balance_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b)
    return d

def plot_rbst_lin_probs(num_nodes_start, num_nodes_end, num_trees):
    d = estimate_list_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_trees, 0 , 1000000)
    fig1 = plt.figure(1)
    fig1.suptitle('Plot_rbst_lin_probs')
    plt.xlim([num_nodes_start,num_nodes_end])
    plt.plot(d)    
    pass

def plot_rbst_balance_probs(num_nodes_start, num_nodes_end, num_trees):
    d = estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_trees, 0 , 1000000)
    fig1 = plt.figure(1)
    fig1.suptitle('Plot_balance_lin_probs')
    plt.xlim([num_nodes_start,num_nodes_end])
    plt.plot(d)  
    pass

### ========== UNIT TESTS =============

## unit_test_01 tests BSTNode constructor
##           5
##          /  \
##         3    10
def unit_test_01():
    r = BSTNode(key=5)
    lc = BSTNode(key=3)
    rc = BSTNode(key=10)
    print('root=%s, lc=%s, rc=%s' % (r, lc, rc))
    r.setLeftChild(lc)
    r.setRightChild(rc)
    assert ( r.getLeftChild().getKey()   == 3 )
    assert ( r.getRightChild().getKey() == 10 )
    #
    print('root=%s, lc=%s, rc=%s' % (r, lc, rc))
    #

## unit_test_01() contstructs two bst's.
## bst
##        10
##       /  \
##      3   20
##
## bst2
##        5
##       /
##     3
##       \
##        4
def unit_test_02():
    bst = BSTree()
    bst.insertKey(10)
    bst.insertKey(3)
    bst.insertKey(20)
    assert ( bst.isBalanced() )
    assert ( bst.heightOf() == 1 )
    assert ( not bst.isList() )
    print('displaying bst')
    bst.displayInOrder()
    print('-------')

    bst2 = BSTree()
    bst2.insertKey(5)
    bst2.insertKey(3)
    bst2.insertKey(4)
    assert ( not bst2.isBalanced() )
    assert ( bst2.heightOf() == 2 )
    assert ( bst2.isList() )
    print('displaying bst2')
    bst2.displayInOrder()

def unit_test_03():
    rbst = gen_rand_bst(5, 0, 10)
    print('root=' + str(rbst.getRoot()))
    rbst.displayInOrder()
    print('is list? = ' + str(rbst.isList()))
    print('height = ' + str(rbst.heightOf()))
    print('is bal? = ' + str(rbst.isBalanced()))

def unit_test_04():
    print(estimate_list_prob_in_rand_bsts_with_num_nodes(100, 5, 0, 1000))

def unit_test_05():
    d = estimate_list_probs_in_rand_bsts(5, 20, 1000, 0, 1000000)
    for k, v in d.iteritems():
        print('probability of linearity in rbsts with %d nodes = %f' % (k, v[0]))

def unit_test_06(from_num_nodes, upto_num_nodes):
    d = estimate_list_probs_in_rand_bsts(from_num_nodes, upto_num_nodes, 1000, 0, 1000000)
    for k, v in d.iteritems():
        print('probability of linearity in rbsts with %d nodes = %f' % (k, v[0]))

def unit_test_07(num_nodes_start, num_nodes_end):
    d = estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, 1000, 0, 1000000)
    for k, v in d.iteritems():
        print('probability of balance in rbsts with %d nodes = %f' % (k, v[0]))



if __name__ == '__main__':
#    unit_test_01()
#    unit_test_02()
#    unit_test_03()
#    unit_test_04()
#    unit_test_05()
#    unit_test_06(0,10)
#    unit_test_07(0,10)
    plot_rbst_lin_probs(0,10,50)
    plot_rbst_balance_probs(0,10,50)




