import random
import time
import difflib





for i in range(2**10):

    a = "A one minute typing test is like a sprint.\n If you make a mistake it is probably best to just ignore it and keep typing the paragraphs.\n Of course accuracy is important, but your speed and accuracy will get better as long as you treat this as a learning exercise. "
    
    b = "The work of these two men is so close (closely) interwoven that, though Fletcher outlived Buaumont (Beaumont)"

    
    option=[a,b]

    randomwrd = random.choice(option)
    
    

    start = time.time()
    options = input(f'\033[1;34;40m Type: {randomwrd} \n\nHere: ')
    
    
    
    def result():
        re= difflib.SequenceMatcher(None, randomwrd, options).ratio()
        te=re*100
        q=round(te,0)
        qe=(f'{q}%')
        print(f'\033[1;31;40m Accuracy: {qe}\n')

        

    
    result()    

    end = time.time()
    
    end_start = round(end-start,2)    
    print("it took", (end_start), "seconds")

    print("  ")
    






