#include<cstdio>
#include<cstdlib>
#include<iostream>

using namespace std;

typedef struct{
    int size;
    int num;
} Fragment;


long ciel(long n){
    return (n << 2) + (n & 0x1);
}

long floor(long n){
    return n << 2;
}


void solution(){
    int T = 0;
    cin >> T;
    for(int i = 0; i < T; i++){
        long N = 0;
        long T = 0;
        cin >> N;
        cin >> T;
        Fragment curr_min = {0, 0};
        Fragment curr_max = {N, 1};
        Fragment next_min = {0, 0};
        Fragment next_max = {0, 0};
        
        int j = 0;
        while(j != T){
            if(curr_max->num != 0){
                
            
