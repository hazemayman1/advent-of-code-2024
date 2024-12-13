##### PART 1######

f = open('input day 10.txt', 'r')
map = []
for line in f:
    map.append([int(item) for item in line.strip()])  

rows, cols = len(map), len(map[0])
count = 0

def dfs(map, i, j, last_val = -1):
    print(last_val, i, j)
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
        return set()
    if map[i][j] != last_val + 1:
        return set()
    if map[i][j] == 9:
        return {(i,j)}
    r = set()
    r = r.union(dfs(map, i+1, j, map[i][j])) 
    r = r.union(dfs(map, i-1, j, map[i][j])) 
    r = r.union(dfs(map, i, j+1, map[i][j])) 
    r = r.union(dfs(map, i, j-1, map[i][j])) 
    return r

for row in range(rows):
    for col in range(cols):
        if map[row][col] == 0:
            r = dfs(map, row, col)
            count += len(r)

print(count)


####PART 2######

f = open('input day 10.txt', 'r')
map = []
for line in f:
    map.append([int(item) for item in line.strip()])  

rows, cols = len(map), len(map[0])
count = 0

def dfs(map, i, j, last_val = -1):
    print(last_val, i, j)
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
        return 0
    if map[i][j] != last_val + 1:
        return 0
    if map[i][j] == 9:
        return 1
    r = 0
    r += (dfs(map, i+1, j, map[i][j])) 
    r += (dfs(map, i-1, j, map[i][j])) 
    r += (dfs(map, i, j+1, map[i][j])) 
    r += (dfs(map, i, j-1, map[i][j])) 
    return r

for row in range(rows):
    for col in range(cols):
        if map[row][col] == 0:
            r = dfs(map, row, col)
            count += (r)

print(count)