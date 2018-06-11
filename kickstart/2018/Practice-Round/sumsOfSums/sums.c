#include <stdio.h>

long result(long nonzore_num, long n, long sum[], long count[], long num_index[])
{
  for(long i = 1; i <= nonzore_num; i++)
  {
    if(count[i] == n)
    {
      return sum[i];
    }
    if(count[i] > n)
    {
      return sum[i] - (count[i] - n) * num_index[i];
    }
  }
  return 0;
}

void solution(long N, long Q, long original_num[], long left_bound[], long right_bound[])
{
  long total = 0;
  for(int i = 0; i < N; i++)
  {
    total += original_num[i];
  }
  long num[total + 1];
  for(int i = 0; i < total + 1; i++)
  {
    num[i] = 0;
  }
  long M = total;
  for(long i = 0; i < N; i++)
  {
    long n_index = 0;
    for(long j = i; j < N; j++)
    {
      n_index += original_num[j];
      num[n_index]++;
    }
  }
  long nonzore_num = 0;
  for(long i = 0; i < M + 1; i++)
  {
    if(num[i] != 0)
    {
      nonzore_num++;
    }
  }

  long sum[nonzore_num + 1];
  long count[nonzore_num + 1];
  long num_index[nonzore_num + 1];
  for(int i = 0; i < nonzore_num + 1; i++){
    sum[i] = 0;
    count[i] = 0;
    num_index[i] = 0;
  }
  long index = 0;
  for(long i = 1; i <= M; i++)
  {
    if(num[i] != 0)
    {
      index++;
      sum[index] = sum[index - 1] + i * num[i];
      count[index] = count[index - 1] + num[i];
      num_index[index] = i;
    }
  }
  for(int i = 0; i < Q; i++)
  {
    printf("%ld\n", result(nonzore_num, right_bound[i], sum, count, num_index) - result(M, left_bound[i] - 1,  sum, count, num_index));
  }
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int case_num = 1; case_num <= T; case_num++)
  {
    long N;
    long Q;
    scanf("%ld %ld", &N, &Q);
    long original_num[N];
    long left_bound[Q];
    long right_bound[Q];
    for(int i = 0; i < N; i++)
    {
      scanf("%ld", &original_num[i]);
    }

    for(int i = 0; i < Q; i++)
    {
      scanf("%ld %ld", &left_bound[i], &right_bound[i]);
    }
    printf("Case #%d:\n", case_num);
    solution(N, Q, original_num, left_bound, right_bound);
  }
  return 0;
}