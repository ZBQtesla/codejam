# Problem C. Fly Swatter

Problem

What are your chances of hitting a fly with a tennis racquet?

To start with, ignore the racquet's handle. Assume the racquet is a perfect ring, of outer radius R and thickness t (so the inner radius of the ring is R−t).

The ring is covered with horizontal and vertical strings. Each string is a cylinder of radius r. Each string is a chord of the ring (a straight line connecting two points of the circle). There is a gap of length g between neighbouring strings. The strings are symmetric with respect to the center of the racquet i.e. there is a pair of strings whose centers meet at the center of the ring.

The fly is a sphere of radius f. Assume that the racquet is moving in a straight line perpendicular to the plane of the ring. Assume also that the fly's center is inside the outer radius of the racquet and is equally likely to be anywhere within that radius. Any overlap between the fly and the racquet (the ring or a string) counts as a hit.

谷歌翻译（仅供参考）

问题 用网球拍击打苍蝇有什么机会？ 

首先，忽略球拍的手柄。假设球拍是一个完美的环，外径为R，厚度为t（因此环的内半径为R-t）。 

戒指上覆盖着水平和垂直的琴弦。每个字符串都是半径为r的圆柱体。每个字符串都是环的弦（连接圆的两个点的直线）。相邻字符串之间有一段长度为g的空白。琴弦相对于球拍的中心是对称的，即有一对琴弦的中心在琴键的中心相遇。 

苍蝇是一个半径为f的球体。假定球拍正在垂直于环平面的一条直线上。假定苍蝇的中心位于球拍的外半径内，并且同样可能在该半径内的任何地方。苍蝇和球拍（戒指或绳子）之间的任何重叠都算作命中。

![image](https://code.google.com/codejam/contest/images/?image=test2.png&p=24479&c=32013)

Input

One line containing an integer N, the number of test cases in the input file.

The next N lines will each contain the numbers f, R, t, r and g separated by exactly one space. Also the numbers will have at most 6 digits after the decimal point.

Output

N lines, each of the form "Case #k: P", where k is the number of the test case and P is the probability of hitting the fly with a piece of the racquet.

Answers with a relative or absolute error of at most 10-6 will be considered correct.

Limits

f, R, t, r and g will be positive and smaller or equal to 10000.

t < R

f < R

r < R

