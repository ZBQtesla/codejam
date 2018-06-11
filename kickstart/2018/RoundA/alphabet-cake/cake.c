#include <stdio.h>

void assign(int row, int col, char cake[row][col])
{

  char write;
  for(int i = 0; i < row; i++)
  {
    write = '?';
    for(int j = 0; j < col; j++)
    {
      if(cake[i][j] != '?')
      {
        write = cake[i][j];
        break;
      }
    }
    if(write == '?')
    {
      continue;
    }
    for(int j = 0; j < col; j++)
    {
      if(cake[i][j] == '?')
      {
        cake[i][j] = write;
      }
      else
      {
        write = cake[i][j];
      }
    }
  }

  for(int j = 0; j < col; j++)
  {
    write = '?';
    for(int i = 0; i < row; i++)
    {
      if(cake[i][j] != '?')
      {
        write = cake[i][j];
        break;
      }
    }
    if(write == '?')
    {
      continue;
    }
    for(int i = 0; i < row; i++)
    {
      if(cake[i][j] == '?')
      {
        cake[i][j] = write;
      }
      else
      {
        write = cake[i][j];
      }      
    }
  }

  // print
  for(int i = 0; i < row; i++)
  {
    for(int j = 0; j <  col; j++)
    {
      printf("%c", cake[i][j]);
    }
    printf("\n");
  }
}

int main(int argc, char const *argv[])
{
  int T = 0;
  scanf("%d", &T);
  for(int i = 1; i <= T; i++)
  {
    printf("Case #%d:\n", i);
    int row = 0;
    int col = 0;
    scanf("%d %d", &row, &col);
    char cake[row][col];
    for(int r = 0; r < row; r++)
    {
        scanf("%s", cake[r]);
    }

    // for(int r = 0; r < row; r++)
    // {
    //   for(int c = 0; c < col; c++)
    //   {
    //     printf("%c", cake[r][c]);
    //   }
    //   printf("\n");
    // }

    assign(row, col, cake);
  }
  return 0;
}