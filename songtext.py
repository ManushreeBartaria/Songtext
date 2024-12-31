import time
with open ("song.txt",'r+') as f:
    data=f.readlines()
    n=len(data)
    for line in data:
        for word in line:
            print(word,end='',flush=True)
            time.sleep(0.09)