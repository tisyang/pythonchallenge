import pickle
with open("banner.p", "rb") as f:
    obj = pickle.load(f)
    print(type(obj))
    for line in obj:
        print("".join(tuple(k*v for k, v in line)))
