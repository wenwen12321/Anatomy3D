import pickle

f = open(r'data/score.pkl','rb')
content=pickle.load(f)

print(content)
