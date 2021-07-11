import random

#alpha: selfish miners mining power (percentage),
#gamma: the ratio of honest miners choose to mine on the selfish miners pool's block
#N: number of simulations run
def Simulate(alpha,gamma,N, seed):
    
    # DO NOT CHANGE. This is used to test your function despite randomness
    random.seed(seed)
  
    #the same as the state of the state machine in the slides 
    state=0
    # the length of the blockchain
    ChainLength=0
    # the revenue of the selfish mining pool
    SelfishRevenue=0
    # hidden blocks
    HiddenBlocks=0

    #A round begin when the state=0
    for i in range(N):
        r=random.random()
        if state==0:
            #The selfish pool has 0 hidden block.
            if r<=alpha:
                #The selfish pool mines a block.
                #They don't publish it. 
                state=1
                HiddenBlocks=1
            else:
                #The honest miners found a block.
                #The round is finished : the honest miners found 1 block
                # and the selfish miners found 0 block.
                ChainLength+=1
                HiddenBlocks=0
                state=0

        elif state==1:
            #The selfish pool has 1 hidden block.
            if r<=alpha:
                state=2
                HiddenBlocks=2
                #The selfish miners found a new block.
                #Write a piece of code to change the required variables.
                #You might need to define new variable to keep track of the number of hidden blocks.
            else:
                state=-1
                ChainLength+=1
                HiddenBlocks=0
                #Write a piece of code to change the required variables.

        elif state==-1:
            #It's the state 0' in the slides (the paper of Eyal and Gun Sirer)
            #There are three situations! 
            #Write a piece of code to change the required variables in each one.
            if r<=alpha:
                SelfishRevenue+=2   
            elif r<=alpha+(1-alpha)*gamma:
                SelfishRevenue+=1
            else:
                SelfishRevenue+=0   
            HiddenBlocks=0
            state = 0
            ChainLength+=1
        elif state==2:
            #The selfish pool has 2 hidden block.
            if r<=alpha:
                state+=1
                HiddenBlocks+=1
            else:
                state = 0
                SelfishRevenue+=2
                ChainLength+=2
                HiddenBlocks=0
                #The honest miners found a block.

        elif state>2:
            if r<=alpha:
                state+=1
                HiddenBlocks+=1
                #The selfish miners found a new block

            else:
                state = state - 1
                SelfishRevenue+=1
                HiddenBlocks=HiddenBlocks-1
                ChainLength+=1
                #The honest miners found a block

    return float(SelfishRevenue)/ChainLength
