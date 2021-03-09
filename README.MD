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
- [ ] MANY MORE TO COME.

### Time

Using the time subtracted by an arbitrary value n has worked well for finding a
Psuedorandom seed value for the Marsenne Twister Algo. Finding the seed is one of the
keys to unlocking a more random generator that can be used as random data to plug-in to
other random algorithms such as WELLRNG512a.

### Inspiration
This project and the implementation of the Marsenne Twister Algorithm was provided by
yinengy on GitHub.
