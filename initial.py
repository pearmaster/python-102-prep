lookup = {1: "one", 2: "two"}

def add(n, word):
    print("Adding " +word +"to lookup as "+str(n))
    global lookup
    lookup[n] = word

def find(n):
    print("Looking up " + str(n))
    return lookup[n]

print(find(2))
