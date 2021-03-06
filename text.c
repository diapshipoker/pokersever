#include <stdio.h>
#include "poker.h"


main(){
   int deck[52], hand[5], freq[10];
    int a, b, c, d, e, i, j;
    srand48( getpid() );
    init_deck( deck );
    hand[0]=deck[0];
    hand[1]=deck[1];
    hand[2]=deck[2];
    hand[3]=deck[3];
    hand[4]=deck[4];
    i=eval_5hand(hand);
    j=hand_rank(i);
    printf("%d-%d\n",i,j);
    i=eval_5hand_fast(hand);
    j=hand_rank(i);
    printf("%d-%d\n",i,j);
    int k[2];
    hand_brandname(hand[0],k);
    printf("%d=%d\n",k[0],k[1]);
    print_hand(hand,5);
    int m=find_card(2,'c',deck);
    printf("%d=%d\n",m,hand[0]);
}
