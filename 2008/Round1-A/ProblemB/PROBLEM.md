# Problem B. Milkshakes
## Problem
You own a milkshake shop. There are N different flavors that you can prepare, and each flavor can be prepared "malted" or "unmalted". So, you can make 2N different types of milkshakes.

Each of your customers has a set of milkshake types that they like, and they will be satisfied if you have at least one of those types prepared. At most one of the types a customer likes will be a "malted" flavor.

You want to make N batches of milkshakes, so that:

There is exactly one batch for each flavor of milkshake, and it is either malted or unmalted.
For each customer, you make at least one milkshake type that they like.
The minimum possible number of batches are malted.
Find whether it is possible to satisfy all your customers given these constraints, and if it is, what milkshake types you should make.
If it is possible to satisfy all your customers, there will be only one answer which minimizes the number of malted batches.

### Input
One line containing an integer C, the number of test cases in the input file.
For each test case, there will be:
One line containing the integer N, the number of milkshake flavors.
One line containing the integer M, the number of customers.
M lines, one for each customer, each containing:
An integer T >= 1, the number of milkshake types the customer likes, followed by
T pairs of integers "X Y", one for each type the customer likes, where X is the milkshake flavor between 1 and N inclusive, and Y is either 0 to indicate unmalted, or 1 to indicated malted. Note that:
No pair will occur more than once for a single customer.
Each customer will have at least one flavor that they like (T >= 1).
Each customer will like at most one malted flavor. (At most one pair for each customer has Y = 1).
All of these numbers are separated by single spaces.

### Output
C lines, one for each test case in the order they occur in the input file, each containing the string "Case #X: " where X is the number of the test case, starting from 1, followed by:
The string "IMPOSSIBLE", if the customers' preferences cannot be satisfied; OR
N space-separated integers, one for each flavor from 1 to N, which are 0 if the corresponding flavor should be prepared unmalted, and 1 if it should be malted.

### Limits
**Small dataset**
C = 100 

1 <= N <= 10 
1 <= M <= 100

**Large dataset**
C = 5 
1 <= N <= 2000 
1 <= M <= 2000

The sum of all the T values for the customers in a test case will not exceed 3000.

### Sample
```
Input       Output 
 	
2           Case #1: 1 0 0 0 0
5           Case #2: IMPOSSIBLE
3
1 1 1
2 1 0 2 0
1 5 0
1
2
1 1 0
1 1 1
```

In the first case, you must make flavor #1 malted, to satisfy the first customer. Every other flavor can be unmalted. The second customer is satisfied by getting flavor #2 unmalted, and the third customer is satisfied by getting flavor #5 unmalted.

In the second case, there is only one flavor. One of your customers wants it malted and one wants it unmalted. You cannot satisfy them both.

## 谷歌翻译（仅供参考）
你拥有一家奶昔店。 你可以准备N种不同的口味，每种口味都可以做成“麦芽”或“未发芽”。 所以，你可以制作2N种不同类型的奶昔。

您的每个客户都有一套他们喜欢的奶昔类型，如果您至少准备了一种奶昔类型，他们会很满意。 顾客喜欢的类型中至多有一种是“麦芽”味道。 

你想制作N批次的奶昔，以便：
- 每种奶昔都有一批，而且是麦芽或未麦芽。 
- 对于每个客户，您至少制作一种他们喜欢的奶昔类型。 
- 可能的最小批次数是麦芽。 

发现是否有可能满足所有客户的这些限制，如果是的话，应该制定什么样的奶昔类型。 

如果可以满足您的所有客户，将只有一个答案，最大限度地减少麦芽批次的数量。


