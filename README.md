### 基本思路
先在第一行第一列放置皇后，然后再第二行可以放置的位置放置一个皇后，一行一行下去。直到某一行无法放置皇后了，说明前面放置的皇后需要调整位置。再去尝试上一行可以放置的另一个位置，看是否可以继续下去。一次次的尝试直到棋盘每行都有皇后，说明此方案正确，做一个输出。再去尝试倒数第二行可以放置的另一个位置，如果不行就一次次回溯直到又一个正确方案，就可以得到所有可能的方案了
### 实现
首先编写一个Queen类，把棋盘布局放在实列属性里
```
class Queen(object):
    def __init__(self, count):
        self.count = count
        self.chess = [[0] * self.count for _ in range(self.count)]
```
然后定义一个可以在每行放置皇后的实列方法<br>
首先判断放置的行数是否超过棋盘大小，如果超过了就说明此时所有行都放置了皇后，是一个正确方案，那就输出此时的布局，然后剪断此时的枝<br>
没有超过棋盘的行数说明要放置一个皇后，如果当前行可以放置皇后，那就去尝试下一行，如果没法放置，那就剪断此时的枝<br>
为了完成这个实列方法，需要先完成两个实列方法
```
def seek(self, row=0):
    if row == self.count:
        self.reset(row - 1)
        return
    for col in range(self.count):
        if self.check(row, col):
            self.chess[row][col] = 1
            self.seek(row + 1)
    else:
        self.reset(row - 1)
```
self.check()用来判断当前格子是否有冲突，为此需要传入row和col<br>
判断行列很简单，判断对角线可以观察坐标系发现<br>
如果把它当成普通的直角坐标系，需要判断的位置当成原点，对角线上的点就是y=x和y=-x上的点，它们的相同点就是tan的绝对值是1，也就是Δy与Δx的绝对值相等
```
abs(i - row) == abs(j - col)
```
```
|0 0|0 1|0 2|0 3|0 4|0 5|0 6|0 7|
|1 0|1 1|1 2|1 3|1 4|1 5|1 6|1 7|
|2 0|2 1|2 2|2 3|2 4|2 5|2 6|2 7|
|3 0|3 1|3 2|3 3|3 4|3 5|3 6|3 7|
|4 0|4 1|4 2|4 3|4 4|4 5|4 6|4 7|
|5 0|5 1|5 2|5 3|5 4|5 5|5 6|5 7|
|6 0|6 1|6 2|6 3|6 4|6 5|6 6|6 7|
|7 0|7 1|7 2|7 3|7 4|7 5|7 6|7 7|
```
```
def check(self, row, col):
    for i in range(self.count):
        if self.chess[row][i] or self.chess[i][col]:
            return False
        for j in range(self.count):
            if abs(i - row) == abs(j - col) and self.chess[i][j]:
                return False
    else:
        return True
```
self.reset()用来剪枝，把传入的row坐标所在行的皇后重置就行了
```
def reset(self, row):
    for col in range(self.count):
        if self.chess[row][col]:
            self.chess[row][col] = 0
            return
```
剩下的工作就是输出了，就不再赘述了