#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import random
from arrays import *
from pokers import *


class pokerlibs:

    def __init__(self,deck):
        random.seed(os.getpid())
        self.init_deck(deck)

    
    ## perform a binary search on a pre-sorted array
    ##
    def findit( key ):
        low, high,mid =0, 4887,0
        while  low <= high:
            mid = (high+low) >> 1    #divide by two
            if key < products[mid]: 
                high = mid - 1
            elif key > products[mid]:
                low = mid + 1
            else:
                return mid

        print "ERROR:  no match found; key = %d\n" % key
        return -1



    ##   This routine initializes the deck.  A deck of cards is
    ##   simply an integer array of length 52 (no jokers).  This
    ##   array is populated with each card, using the following
    ##   scheme:
    ##
    ##   An integer is made up of four bytes.  The high-order
    ##   bytes are used to hold the rank bit pattern, whereas
    ##   the low-order bytes hold the suit/rank/prime value
    ##   of the card.
    ##
    ##   +--------+--------+--------+--------+
    ##   |xxxbbbbb|bbbbbbbb|cdhsrrrr|xxpppppp|
    ##   +--------+--------+--------+--------+
    ##
    ##   p = prime number of rank (deuce=2,trey=3,four=5,five=7,...,ace=41)
    ##   r = rank of card (deuce=0,trey=1,four=2,five=3,...,ace=12)
    ##   cdhs = suit of card
    ##   b = bit turned on depending on rank of card
    ##
    def init_deck( deck ):
        i,j,n,suit = 0,0,0,0x8000
        for i in range(4):
            for j in range(13):
                deck.append(primes[j] | (j << 8) | suit | (1 << (16+j)))
                n = n + 1
            suit >>= 1



    ##  This routine will search a deck for a specific card
    ##  (specified by rank/suit), and return the INDEX giving
    ##  the position of the found card.  If it is not found,
    ##  then it returns -1
    ##
    def find_card( rank, suit, deck ):
        c = 0
        for i in range(52):
            c = deck[i]
            if ( (c & suit)  and  (RANK(c) == rank) ):
                return i

	return -1



    ##  This routine takes a deck and randomly mixes up
    ##  the order of the cards.
    ##
    def shuffle_deck( deck ):
        i,n,temp = 0,0,[]
        for i in range(52):
            temp.append(deck[i])
        for i in range(52):
            while True:
                if temp[n] != 0:
                    break
                n = 51.9999999 * random.random()
            deck[i] = temp[n]
            temp[n] = 0

    def hand_brandname(hand,s):
        r,suit = 0,0
        rank= (0,1,2,3,4,5,6,7,8,9,10,11,12)
        r = (hand >> 8) & 0xF
        if ( hand & 0x8000 ):
            suit = 32768
        elif ( hand & 0x4000 ):
            suit = 16384
        elif ( hand & 0x2000 ):
            suit = 8192
        else:
            suit = 4096

        s.append(suit)
        s.append(rank[r])

    def hand_rank( val ):
        if (val > 6185): 
            return(HIGH_CARD)        # 1277 high card
        if (val > 3325): 
            return(ONE_PAIR)         #2860 one pair
        if (val > 2467):
            return(TWO_PAIR)         #858 two pair
        if (val > 1609):
            return(THREE_OF_A_KIND)  #858 three-kind
        if (val > 1599):
            return(STRAIGHT)         #10 straights
        if (val > 322):
            return(FLUSH)            #1277 flushes
        if (val > 166):
            return(FULL_HOUSE)       #  156 full house
        if (val > 10):
            return(FOUR_OF_A_KIND)   #  156 four-kind

        return(STRAIGHT_FLUSH)       #10 straight-flushes

    def find_fast(u):
        a, b, r = 0,0,0
        u += 0xe91aaa35
        u ^= u >> 16
        u += u << 8
        u ^= u >> 4
        b  = (u >> 8) & 0x1ff
        a  = (u + (u << 2)) >> 19
        r  = a ^ hash_adjust[b]
        return r

    def eval_5cards_fast(c1,c2,c3,c4,c5):
        q = (c1 | c2 | c3 | c4 | c5) >> 16
        s = 0
        if (c1 & c2 & c3 & c4 & c5 & 0xf000): 
            return flushes[q]  #check for flushes and straight flushes
        s = unique5[q]
        if (s):
            return s           #check for straights and high card hands

        return hash_values[find_fast((c1 & 0xff) * (c2 & 0xff) * (c3 & 0xff) * (c4 & 0xff) * (c5 & 0xff))]

    def eval_5hand_fast(hand):
        c1, c2, c3, c4, c5 = 0,0,0,0,0
        c1 = hand[0]
        c2 = hand[1]
        c3 = hand[2]
        c4 = hand[3]
        c5 = hand[4]
        return( eval_5cards_fast(c1,c2,c3,c4,c5) )


    def eval_5cards( c1, c2, c3, c4, c5 ):
        q,s = 0,0
        q = (c1|c2|c3|c4|c5) >> 16
        # check for Flushes and StraightFlushes
        if ( c1 & c2 & c3 & c4 & c5 & 0xF000 ):
            return( flushes[q] )
        # check for Straights and HighCard hands
        s = unique5[q]
        if ( s ):
            return ( s )
        # let's do it the hard way
    
        q = (c1&0xFF) * (c2&0xFF) * (c3&0xFF) * (c4&0xFF) * (c5&0xFF)
        q = findit( q )

        return( values[q] )

    def eval_5hand( hand ):
        c1, c2, c3, c4, c5 = 0,0,0,0,0
        c1 = hand[0]
        c2 = hand[1]
        c3 = hand[2]
        c4 = hand[3]
        c5 = hand[4]
        return( eval_5cards(c1,c2,c3,c4,c5) )

    def eval_6hand(hand):
        q,best,subhand = 0,9999,[0,0,0,0,0]
        for i in range(6):
            for j in range(5):
                subhand[j] = hand[perm6[i][j]]
            q = eval_5hand(subhand)
            if q < best:
                best = q

        return best

    def eval_6hand_fast(hand):
        q,best,subhand = 0,9999,[0,0,0,0,0]
        for i in range(6):
            for j in range(5):
                subhand[j] = hand[perm6[i][j]]
            q = eval_5hand_fast(subhand)
            if q < best:
                best = q

        return best

    ## This is a non-optimized method of determining the
    ## best five-card hand possible out of seven cards.
    ## I am working on a faster algorithm.
    ##
    def eval_7hand( hand ):
        q,best,subhand = 0,9999,[0,0,0,0,0]
        for i in range(21):
            for j in range(5):
                subhand[j] = hand[perm7[i][j]]
            q = eval_5hand(subhand)
            if q < best:
                best = q

        return best

    def eval_7hand_fast( hand ):
        q,best,subhand = 0,9999,[0,0,0,0,0]
        for i in range(21):
            for j in range(5):
                subhand[j] = hand[perm7[i][j]]
            q = eval_5hand_fast(subhand)
            if q < best:    
                best = q
                
        return best
