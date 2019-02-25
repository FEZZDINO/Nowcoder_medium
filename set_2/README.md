1. 有一个投篮游戏。球场有p个篮筐，编号为0，1...，p-1。每个篮筐下有个袋子，每个袋子最多装一个篮球。有n个篮球，每个球编号xi 。规则是将数字为xi 的篮球投到xi 除p的余数为编号的袋里。若袋里已有篮球则球弹出游戏结束输出i，否则重复至所有球都投完。输出-1。问游戏最终的输出是什么？

输入描述:
第一行两个整数p,n（2≤p,n≤300)。p为篮筐数，n为篮球数。接着n行为篮球上的数字xi(0≤xi≤1e9)


输出描述:
输出游戏的结果
示例1
输入
10 5  
0  
21  
53  
41  
53  
输出  
4  


3. Volodya and Vlad play the following game. There are k pies at the cells of n  ×  m board. Each turn Volodya moves one pie to the neighbouring (by side) cell. If the pie lies at the border of the board then Volodya can move it outside the board, get the pie and win. After Volodya's move, Vlad bans some edge at the border of the board of length 1 (between two knots of the board) so that Volodya is not able to move the pie outside the board through this edge anymore. The question is: will Volodya win this game? We suppose both players follow the optimal strategy.

<center> </center> 
输入描述:
First line contains 3 integers, separated by space: 1 ≤ n, m ≤ 100 — dimensions of the board and 0 ≤ k ≤ 100 — the number of pies. Each of the next k lines contains 2 integers, separated by space: 1 ≤ x ≤ n, 1 ≤ y ≤ m — coordinates of the corresponding pie. There could be more than one pie at a cell. 



输出描述:
Output only one word: "YES" — if Volodya wins, "NO" — otherwise.

示例1
输入  
2 2 1  
1 2  
3 4 0  
100 50 2  
50 25  
50 25  
输出  
YESNONO  
