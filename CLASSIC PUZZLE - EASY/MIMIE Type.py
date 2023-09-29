n =int(input())
q = int(input())
dic = {}
for _ in range(n):
    ext, mt = input().split()
    dic[ext.lower()] = mt
for _ in range(q):
    fname = input()
    print(dic.get( fname.split(".")[-1].lower() if "." in fname else "UNKNOWN", "UNKNOWN"))