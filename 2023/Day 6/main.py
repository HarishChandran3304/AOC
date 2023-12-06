import re

with open("input.txt", "r") as f:
    data = f.read()

def get_ways(time, dist):
    for i in range(time+1):
        curr = i*(time-i)
        if curr > dist:
            return (time+1)-(i*2)

def solve(data):
    times, dists = data.split("\n")
    times = re.findall(r'(\d+)', times)
    dists = re.findall(r'(\d+)', dists)
    time = int("".join(times))
    dist = int("".join(dists))
    times = list(map(int, times))
    dists = list(map(int, dists))
    res1 = 1

    for i in range(len(times)):
        res1 *= get_ways(times[i], dists[i])
    
    res2 = get_ways(time, dist)
    
    return res1, res2

def main():
    res1, res2 = solve(data)
    print(res1)
    print(res2)

if __name__ == "__main__":
    main()