import re

with open("input.txt", "r") as f:
    data = f.read()

def solve(data):
    res1 = 0
    lines = data.split("\n")
    pattern = r'\d+'
    copies = [0] * len(lines)

    for i in range(len(lines)):
        curr, winning = lines[i].split(":")[1].split("|")
        score = len(set(re.findall(pattern, curr)).intersection(set(re.findall(pattern, winning))))

        res1 += 2**(score-1) if score else 0
        
        copies[i] += 1
        for j in range(i+1, i+score+1):
            copies[j] += copies[i]

    res2 = sum(copies)
    return res1, res2

def main():
    res1, res2 = solve(data)
    print(res1)
    print(res2)

if __name__ == "__main__":
    main()
