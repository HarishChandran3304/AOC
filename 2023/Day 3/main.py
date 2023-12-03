with open("input.txt", "r") as f:
    data = f.read()

def check(lines, i, j):
    nums = set()
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for x, y in directions:
        i2, j2 = i+x, j+y
        if 0 <= i2 < len(lines) and 0 <= j2 < len(lines[i2]):
            if lines[i2][j2].isdigit():
                l, r = j2, j2
                while (0 <= l < len(lines[i2])) and lines[i2][l].isdigit():
                    l -= 1
                while (0 <= r < len(lines[i2])) and lines[i2][r].isdigit():
                    r += 1
                nums.add((int(lines[i2][l+1:r]), i2, l+1))
    
    return nums

def solve(data):
    lines = data.split("\n")
    res1, res2 = 0, 0
    visited = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char = lines[i][j]
            if not char.isalnum() and char != ".":
                    nums = check(lines, i, j)
                    for num in nums:
                        n, x, y = num
                        if (x, y) not in visited:
                            res1 += n
                            visited.add((x, y))
                    
                    if len(nums) == 2 and char == "*":
                        res2 += (lambda x, y: x*y) (*[n for n, _, _ in nums])

    return res1, res2

def main():
    res1, res2 = solve(data)
    print(res1)
    print(res2)

if __name__ == "__main__":
    main()