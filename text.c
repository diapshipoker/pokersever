#include <stdio.h>
#include "poker.h"


main(){
   int deck[52], hand[5], freq[10];
    int a, b, c, d, e, i, j;
    srand48( getpid() );
    init_deck( deck );
    hand[0]=deck[11];
    hand[1]=deck[111];
    hand[2]=0;
    hand[3]=0;
    hand[4]=0;
    i=eval_5hand(hand);
    j=hand_rank(i);
    printf("%d\n",j);
}
