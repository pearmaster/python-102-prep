lookup = {1: "one", 2: "two"}

def add(n, word):
    print(f"Adding {word} to lookup as {n}")
    global lookup
    lookup[n] = word

def find(n):
    print(f"Looking up {n}")
    return lookup[n]

if __name__ == "__main__":
    print(find(2))

