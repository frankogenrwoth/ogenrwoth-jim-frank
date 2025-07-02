#import the necessary libraries
import numpy as np
import random  #helps us to setup random values

#environment setup
road_length = 5 #number of steps to move (0-4) index
actions = ['right', 'left'] #steps to move 

#Q-table intialisation
Q = np.zeros((road_length, len(actions)))

#hyperparameters
episodes = 1000 #the bigger the number of episodes the higher the learning chances of the model
learning_rate = 0.8
gamma = 0.9  #it will have a higher reward
epsilon = 0.3  #helps the agent to discover the new path

#training episodes
for episode in range(episodes):
    state = 0
    while state != 4:
        # Epsilon-greedy action selection
        if random.uniform(0,1) < epsilon:
            action_idx = random.randint(0,1)
        else:
            action_idx = np.argmax(Q[state])
        
        # Take action and observe next state and reward
        if actions[action_idx] == 'right':
            next_state = min(state + 1, road_length - 1)
        else:  # 'left'
            next_state = max(state - 1, 0)
        
        # Define reward
        if next_state == 4:
            reward = 1  # Goal reached
        else:
            reward = -0.01  # Small penalty to encourage faster solutions
        
        # Q-learning update
        Q[state, action_idx] = Q[state, action_idx] + learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action_idx]
        )
        
        state = next_state

# Test the learned policy
print("Learned Q-table:")
print(Q)

print("\nTesting the learned policy:")
state = 0
steps = 0
while state != 4 and steps < 20:
    action_idx = np.argmax(Q[state])
    print(f"State: {state}, Action: {actions[action_idx]}")
    if actions[action_idx] == 'right':
        state = min(state + 1, road_length - 1)
    else:
        state = max(state - 1, 0)
    steps += 1
if state == 4:
    print("Goal reached!")
else:
    print("Did not reach the goal within 20 steps.")


