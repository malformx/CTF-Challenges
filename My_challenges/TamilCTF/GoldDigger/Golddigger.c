#include <stdio.h>
#include <string.h>
#include<malloc.h>
#ifndef TEST_H
#define TEST_H
const int deez[] = {22, 10, 31, 16, 24, 27, 9, 11, 30, 3, 8, 20, 29, 0, 7, 17, 23, 19, 21, 28, 18, 2, 6, 4, 25, 5, 26, 1};
const int nutz[] = {112, 83, 106, 113, 52, 125, 129, 80, 99, 72, 104, 88, 89, 99, 73, 109, 71, 101, 74, 115, 88, 114, 76, 99, 121, 75, 127, 120};
#endif

int *sugma()
{
        int *fuck=malloc(sizeof(deez)*4);
        int i;
        for (i = 0; i<28; i++){
                fuck[i] = deez[i] ^ 0x12;
        }
        return fuck;
}

int balls(char flag[])
{
        int *ding;
        int *reord = malloc(sizeof(28)*4);

        ding = sugma();
        int l = sizeof(*ding);

        int i;
        for (i = 0; i<28; i++){
                reord[i] = flag[ding[i]]+4;
        }

        for (i=0; i<28; i++){
                if (reord[i]!=nutz[i]){
                        return -1;
                }
        };

        return 0;

}

int main(int argc, char** argv)
{
        if (argc<2){
                printf("You forgot something to give me?\n");
                return -1;
        }
        if (strlen(argv[1])!=28){
                printf("I only need 28 chars dude..Not much, Not less\n");
                return -1;
        }
        if (balls(argv[1]) == 0){
                printf("Yeeyaww, Now go submit the flag, kind sir\n");
        }
        else{
                printf("Beep Boop Beep 1010100 1110010 1111001 100000 1001000 1100001 1110010 1100100 1100101 1110010 100001 100001 100001\n");
        }

        return 0;
}