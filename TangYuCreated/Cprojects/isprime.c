#include <stdio.h>
#include <math.h>
void main()
{ long c,d,cs,ds,ct,dt,f,g,i,j,k,m,max,a[11000];
  int e,u,x,y;
  printf("  请输入 c,d:"); scanf("%ld,%ld",&c,&d);
  if(d-c<=20000) {cs=c;ds=d;x=0;}
  else {
        x=(d-c)/20000;
        cs=c;
        ds=d-20000*x;
        }
  f=cs;
  max=0;

  for(y=1;y<=x+1;y++)  // 把[c,d]中分x+1个子区间筛选素数,x + 1 subintervals in total
{ if(cs%2==0) cs++;

    for(i=0;i<=10999;i++)
        a[i]=0;

    e=(ds-cs)/2;    //奇数个数
    i=1;

    while (i<=sqrt(ds))
    {
        i=i+2;
        g=2*(cs/(2*i))+1;   //个数，想用奇数i定位到cs尽量近的地方
        if(g*i>ds) continue;
        if(g==1)
            g=3;

        j=i*g;  //离cs最近的地方:j
        while (j<=ds)
        {
            if(j>=cs)
            a[(j-cs)/2]=-1;   // 筛去标记-1

            j=j+2*i;    //用i开筛
        }
    }

    for(u=1,k=0;k<=e;k++)   //e 是cs到ds之间的奇数个数
    {
        if(a[k]!=-1)
        {
            m=cs+2*k;        // m即筛选所得素数

            if(m-f>max)      // 寻求两相邻素数间距的最大值
            {
                max=m-f;
                ct=f+1;
                dt=cs+2*k-1;
            }

            f=m;
        }
    }
cs=ds+1;
ds=ds+20000;    //  cs与ds增长后继续探求
}
  printf("  最多连续合数的个数为：%ld\n",max-1);
  printf("  连续合数区间为：[%ld,%ld]\n",ct,dt);
 }
