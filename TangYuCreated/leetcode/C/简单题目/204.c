int countPrimes(int n) {
    int i;
    int j;
    int sum = 0;
    int state = 1;
    if (n == 0 || n == 1 || n == 2)     return 0;
    for (i = 2;i < n;i++)
    {
        for (j = 2;j < i;j++)
        {
            if (i % j == 0)
            {
                state = 0;
                break;
            }
        }

        if (state)  sum++;
    }
    return sum;

}

