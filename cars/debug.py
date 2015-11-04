import pickle

def loadd(a):
    f = open(a, 'rb')
    f0 = pickle.load(f)
    print(f0)
