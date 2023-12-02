import re

with open("input.txt", "r") as f:
    data = f.read()

def solve(data: str) -> int:
    data = data.split("\n")
    limit = {"red": 12, "green": 13, "blue": 14}
    res1, res2 = 0, 0
    
    for game in data:
        gameid, game = game.split(":")
        game = game.strip()
        curr = {"red": 0, "green": 0, "blue": 0}
        valid = True
        for n, c in re.findall(r'(\d+) (\w+)', game):
            if int(n) > limit[c]:
                valid = False
            curr[c] = max(curr[c], int(n))    

        res1 += int(gameid.split(" ")[-1]) if valid else 0
        res2 += curr["red"] * curr["green"] * curr["blue"]
    
    return res1, res2

def main():
    res1, res2 = solve(data)
    print(res1)
    print(res2)

if __name__ == "__main__":
    main()