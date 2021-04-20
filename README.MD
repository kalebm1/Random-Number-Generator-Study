# Testing the bounds of Psuedorandomness

We all know that random number generation in computers is a never-ending cycle of chasing
true randomness. We are trying different variables that can be recorded in the users
machine to find the optimal solution to the problem of randomness. We will be combining
these factors with popular Pseudorandom Algorithms to find the best algorithm we can design.

## Current ideas:

- [ ] Users MAC address
- [x] Users Time
- [ ] Users amount of space on computer
- [ ] Users battery life
- [x] Users' System Memory Value (GB)
- [ ] MANY MORE TO COME.

### Time

Using the time subtracted by an arbitrary value n has worked well for finding a
Psuedorandom seed value for the Marsenne Twister Algo. Finding the seed is one of the
keys to unlocking a more random generator that can be used as random data to plug-in to
other random algorithms such as WELLRNG512a.

### Inspiration

This project and the implementation of the Marsenne Twister Algorithm was provided by
yinengy on GitHub.

## V1.0 Inclusion and Implementation

Current implementation includes a Marsenne twister by calling class Random() which is seeded
by the users' time multiplied by the amount of memory their system has. This causes a different
seed number everytime it is ran even at the same exact time on different machines.

```python
>>rand = Random()
>>rand.random() or rand.randint()
```

We also have have WELLRNG512a implemented using random data for the initial array
from the new random algo from the Marsenne Twister.

```python
>>rand = WellsRandom()
>>rand.InitWELLRNG512a()
>>rand.WELLRNG512a()
```

Recently implemented was the Blum Blum Shub Algorithm which can be used as follows:

```python
>>test = RandomBBS() OR RandomBBS(p,q,s)
#p and q are prime numbers and s being a seed
>>test.getRandBit()#returns a random bit(0 or 1)
>>test.setP()#set the p value(int)
>>test.setQ()#set the q value(int)
>>test.setSeed()#set the seed value(int)
>>test.getRandNumber()#returns random int
```

We have also included the Blum-Micali algorithm with a few helpful
methods which are laid out as follows:

```python
>>test = RandomBM()
>>test.getRandBits(n)#returns a random string of bits of length n
>>test.setSeed()#set the seed value(int)
>>test.binaryToDecimal()#takes a string binary representation and converts it to decimal(string)
>>test.getRandNumber()#returns a random int
>>test.getRandSetNum(a)#returns a random int between 0-a(int)
```

More algorithms to come. Enjoy!
