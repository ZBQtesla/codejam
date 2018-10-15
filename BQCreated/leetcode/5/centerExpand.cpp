#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

string maxLen(string str);

int main(){
    string s("cbbd");
    cout << maxLen(s) <<  endl;
}


string maxLen(string str){
    int n = str.size();
    int max = 0;
    int maxL = 0;
    int maxR = 0;
    string maxString;
    for(int i = 0; i < 2*n-1; i++){
        int count = 0;
        int index = i / 2;
        int l, r;
        if(i % 2 == 0){
            count++;
            l = index - 1;
            r = index + 1;
        }
        else{
            l = index;
            r = index + 1;
        }
        while(l >=0 && r < n){
            if(str[l] == str[r]){
                count+=2;
                l--;
                r++;
            }
            else
                break;
        }
        if(count > max)
        { 
            maxL = l+1;
            maxR = r-1;
            max = count;
        }
    }

    return str.substr(maxL, maxR-maxL+1);

}

