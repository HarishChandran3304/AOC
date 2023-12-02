with open("input.txt", "r") as f:
    data = f.read()

def solve(data: str) -> int:
    data = data.split("\n")
    res = 0
    for line in data:
        l, r = 0, len(line) - 1
        while not line[l].isdigit():
            l += 1
        while not line[r].isdigit():
            r -= 1
        res += int(line[l])*10 + int(line[r])
    return res

def replace(line: str) -> str:
    return (
            line.replace("oneight", "18")
            .replace("eightwo", "82")
            .replace("eighthree", "83")
            .replace("twone", "21")
            .replace("sevennine", "79")
            .replace("fiveeight", "58")
            .replace("seven", "7")
            .replace("five", "5")
            .replace("eight", "8")
            .replace("one", "1")
            .replace("nine", "9")
            .replace("three", "3")
            .replace("two", "2")
            .replace("four", "4")
            .replace("six", "6")
        )

def main():
    print(solve(data))
    print(solve(replace(data)))

if __name__ == "__main__":
    main()