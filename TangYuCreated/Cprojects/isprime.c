#include <stdio.h>
#include <math.h>
void main()
{ long c,d,cs,ds,ct,dt,f,g,i,j,k,m,max,a[11000];
  int e,u,x,y;
  printf("  ������ c,d:"); scanf("%ld,%ld",&c,&d);
  if(d-c<=20000) {cs=c;ds=d;x=0;}
  else {
        x=(d-c)/20000;
        cs=c;
        ds=d-20000*x;
        }
  f=cs;
  max=0;

  for(y=1;y<=x+1;y++)  // ��[c,d]�з�x+1��������ɸѡ����,x + 1 subintervals in total
{ if(cs%2==0) cs++;

    for(i=0;i<=10999;i++)
        a[i]=0;

    e=(ds-cs)/2;    //��������
    i=1;

    while (i<=sqrt(ds))
    {
        i=i+2;
        g=2*(cs/(2*i))+1;   //��������������i��λ��cs�������ĵط�
        if(g*i>ds) continue;
        if(g==1)
            g=3;

        j=i*g;  //��cs����ĵط�:j
        while (j<=ds)
        {
            if(j>=cs)
            a[(j-cs)/2]=-1;   // ɸȥ���-1

            j=j+2*i;    //��i��ɸ
        }
    }

    for(u=1,k=0;k<=e;k++)   //e ��cs��ds֮�����������
    {
        if(a[k]!=-1)
        {
            m=cs+2*k;        // m��ɸѡ��������

            if(m-f>max)      // Ѱ�������������������ֵ
            {
                max=m-f;
                ct=f+1;
                dt=cs+2*k-1;
            }

            f=m;
        }
    }
cs=ds+1;
ds=ds+20000;    //  cs��ds���������̽��
}
  printf("  ������������ĸ���Ϊ��%ld\n",max-1);
  printf("  ������������Ϊ��[%ld,%ld]\n",ct,dt);
 }
