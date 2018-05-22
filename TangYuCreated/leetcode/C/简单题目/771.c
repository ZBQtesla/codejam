#include <stdio.h>
int numJewelsInStones(char* J, char* S) {
    int sum = 0;
    int i;
    int j;
    for (i = 0;;i++)        //we take care of each character in the string
    {
        if (S[i] == '\0')
        {
            break;
        }
        else
        {
            for(j = 0;J[j] != '\0';j ++)
            {
                if (J[j] == S[i])
                {
                    sum++;
                    break;
                }
            }
        }


    }

    return sum;
}
