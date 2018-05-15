# Problem A. Minimum Scalar Product

## Problem
You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.

### Input
The first line of the input file contains integer number T - the number of test cases. For each test case, the first line contains integer number n. The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively.

### Output
For each test case, output a line
```
Case #X: Y
```

where X is the test case number, starting from 1, and Y is the minimum scalar product of all permutations of the two given vectors.

### Limits
**Small dataset**

T = 1000
1 ≤ n ≤ 8
-1000 ≤ xi, yi ≤ 1000

**Large dataset**

T = 10
100 ≤ n ≤ 800
-100000 ≤ xi, yi ≤ 100000

### Sample
```
Input       Output
 	 
2           Case #1: -25
3           Case #2: 6
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1
```

## 谷歌翻译（仅供参考）
给出两个向量v1 =（x1，x2，...，xn）和v2 =（y1，y2，...，yn）。 这些向量的标量乘积是一个单数，计算为x1y1 + x2y2 + ... + xnyn。 假设你可以按照你的意愿排列每个向量的坐标。 选择两个置换，使得两个新向量的标量乘积尽可能小，并输出最小标量乘积。

