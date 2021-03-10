'''This File is used for testing Randomness in the algorithms
   and for plotting the findings of those tests.'''

from RandomMarsenne import Random
from RandomWells import WellsRandom
import matplotlib.pyplot as plt   
from collections import Counter
from PIL import Image
from IPython.display import display
import random

# %matplotlib inline

test = Random()


num_trials = 10**7

s = [test.randint(0,1001) for n in range(num_trials)]  
y = [s.count(n) for n in range(1000)]

# your code here
plt.bar(range(1000),y, width=1.0, edgecolor='black')
plt.title('My MT algorithm')
plt.ylabel("Times of show up")
plt.xlabel('Outcome')
plt.show()



num_trials = 10**7
random.seed()
s = [random.randint(0,1000) for n in range(num_trials)]  
y = [s.count(n) for n in range(1000)]

# your code here
plt.bar(range(1000),y, width=1.0, edgecolor='black')
plt.title('Python buit-in Random')
plt.ylabel("Times of show up")
plt.xlabel('Outcome')
plt.show()


"""THIS IS THE CODE FOR THE IMAGE"""
# IMAGE_SIZE = 500

# myImg = Image.new('RGB', (IMAGE_SIZE,IMAGE_SIZE), "white")
# pixels = myImg.load()

# test = Random()
# for i in range(50000):
#     x = test.randint(0,IMAGE_SIZE)
#     y = test.randint(0,IMAGE_SIZE)
#     # print(str(x)+", "+str(y)+"\n")
#     pixels[x,y] = (0,0,0)

# myImg.save("RANDOMSEEDWITHTIME50000.png","PNG")

"""THIS IS THE CODE TO TEST THE 
    WELLS ALGO"""
# test = WellsRandom()
# test.InitWELLRNG512a()
# print(test.WELLRNG512a())
# print(test.WELLRNG512a())
# print(test.WELLRNG512a())
# rand = Random()

# print(rand.randint(0,600))
# print(rand.randint(0,600))
# print(rand.randint(0,600))