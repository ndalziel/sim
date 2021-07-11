from mining_simulation import *

#let's run the code with the follwing parameters!
alpha=0.35
gamma=0.5
Nsimu=10**7
seed = 100
#This is the theoretical probability computed in the original paper
print("Theoretical probability :",(alpha*(1-alpha)**2*(4*alpha+gamma*(1-2*alpha))-alpha**3)/(1-alpha*(1+(2-alpha)*alpha)))
print("Simulated probability :",Simulate(alpha,gamma,Nsimu, seed))