from functools import cache


with open('input day 11.txt', 'r') as f:
    stones = [int(x) for x in f.readline().split()]

@cache
def split_stone(stone, itr) -> list[str]:
    if itr == 0:
        return 1
    if stone == 0:
        return split_stone(1, itr - 1)
    elif len(str(stone)) % 2 == 0:
        n = len(str(stone))
        left = int(str(stone)[:n // 2])
        right = int(str(stone)[n // 2:])
        return split_stone(left, itr-1) + split_stone(right, itr-1)
    else:
        return split_stone(2024*stone, itr-1)
 
num = 75
print(sum(split_stone(x, num) for x in stones))
