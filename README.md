# Markov_Board_Games
Modelling the famous Snakes &amp; Ladders and Risk Game as an Absorbing Markov Chain

 

Making a board game using the concepts of Markov Chain.
 as a part of Applied Stochastic Process
─
Participants
Avil Aneja                2017A7PS0968G
Soneji Visarg Balkrishna        2017A7PS0029G
Jineet Desai                2017A7PS0168G
Ishan Patel                2017A3PS0431G

Overview
A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.It is a stochastic process, but it differs from a general stochastic process in that a Markov chain must be "memory-less." That is, (the probability of) future actions are not dependent upon the steps that led up to the present state. This is called the Markov property. The state space, or set of all possible states, can be anything: letters, numbers, weather conditions, baseball scores, or stock performances.

Let X be a stochastic process,  X can clearly take on the values according to the state space defined. Let Xt be the value of the process (what state we are in) at time t . Then Markov Property is stated as : 
P(Xt+1=i|Xt=j)=P(Xt+1=1|Xt=j,...,X0=x0)

A Markov chain is an absorbing chain if:
 there is at least one absorbing state.
It is possible to go from each non-absorbing state to at least one absorbing state in a finite number of steps.
A state in a Markov chain is called an absorbing state if once the state is entered, it is impossible to leave.

If a standard form P for an absorbing Markov chain is partitioned as
                                  


then approaches a limiting matrixas k increases where
     
The matrix F is given by
  
and is called the fundamental matrix for P
The identity matrix used to form the fundamental matrix F must be the same size as the matrix Q.
In this project we are going to compare the theoretical and simulated results for two board games 
Snakes and ladders
Risk
Game 1 : Snakes And Ladders
Goals
To calculate the expected number of steps to complete the game and to compare the results obtained from theoretical and simulated calculations.
Rules/Specifications
After getting the first six only, the user can start playing game.
Take it in turns to roll the dice. Move his/her counter forward the number of spaces shown on the dice.
If the counter lands at the bottom of a ladder, can move up to the top of the ladder.
If the counter lands on the head of a snake, must slide down to the bottom of the snake.
The game completes when one reaches the 100th position.


Figure of the snakes and ladders board used in this project
Snake and Ladders as Markov Chain
The game of Snakes and Ladders is a good candidate for analysis with a Markov Chain because of its memorylessness: at a given point in the game, the player's progression from the current square is independent of how they arrived at that square.

Since in this project we are trying to figure out the expected number of dice throws to reach the final state, we are not considering the states where there are ladders or snakes as different. For eg. consider we have a ladder from 2 to 23. Now when we reach 2 we don’t have to throw dice again , we will directly go to 23. So probability of reaching to state 2 is 0 from any state. So, if we consider it in our transition matrix it will not remain transition matrix as the sum of columns for every row is 1 in transition matrix but for row 2 it is 0. Hence we consider 2 and 23 as the same state. SImilarly for other states which has ladders or snakes they are considered as the same state. So we end up with 86 states in total as there were 15 snakes and ladders combined.

After reaching the final state i.e. 100 we are absorbed in that state only. So, 100 (or 85 corresponding to the mapping) is the absorbing state in our model.
Result
Expected number of steps :
Theoretical : Using the transition matrix we got the expected number of steps to complete the game to be  41.31040267345721
Simulated : We simulated this board game in python and got the expected steps to be 41.773
Graph :

The red line in the above graph shows the theoretical expected number of steps to complete the game.
Game 2 : Risk  
Goals
To calculate the expected number of steps to complete the game and to compare the results obtained from theoretical and simulated calculations.
To find the winning probabilities for attacker and defender.
Rules/Specifications
Battles in risk are resolved as follows : 
The attacker and defender roll one dice simultaneously.
The attacker and defender compare their  rolls. Whichever is higher wins and the loser loses an army. Ties go to the defender.
If there are no attacking armies left, the defender wins. If there are no defending armies left, the attacker wins and claims the territory. Else return to first rule.

Figure of the RISK board used in this project
Risk as Markov Chain
This game is also a classical example of markov chain.It also follows memoryless property since the battle is fought on the recent dice throws, it has no dependency on previous throws.Hence, we can classify different conditions modelled as markov states and classify some of them as absorbing states to perform the theoretical analysis and compare the results with simulated one.
In this game we start with 7 attacker and 6 defender armies. So seeing this we can have 56 states in total from (0 to 55) mapped with two-coordinates (from (0,0) to (7,6)). Mapping is shown below.
Interesting thing about this game is that we can have several absorbing states as if attacker loses with 2 defender armies left is an absorbing state and also if attacker loses with 1 defender army left , that is also an absorbing state. So, in total we have 14 absorbing states possible in it.

Mapping :            0    1    2    3    4    5    6
            0    49    50    51    52    53    54    55
            1    48    0    1    2    3    4    5
            2    47    6    7    8    9    10    11
            3    46    12    13    14    15    16    17
            4    45    18    19    20    21    22    23
            5    44    24    25    26    27    28    29
            6    43    30    31    32    33    34    35
            7    42    36    37    38    39    40    41

Here the left most represents the no. of attackers army and top most represents the no. of defenders army. In blue color, we have mentioned the states. This mapping is done to keep absorbing states together which makes initialisation of transition matrix easier.

Results
Expected number of steps :
Theoretical : Using the transition matrix we got the expected number of steps to complete the game to be  10.168180083907123
Simulated : We simulated this board game in python and got the expected steps to be 10.17177 (100000 iterations)
Graph :


The red line in the above graph shows the theoretical expected number of steps to complete the game.


Winning probabilities :
    Theoretical : 
             Attackers : 0.3797688225251342
             Defenders : 0.6202311774748666
    Simulated :     (100000 iterations)
             Attackers : 0.37961
             Defenders : 0.6204

