import gymnasium as gym
from gymnasium.wrappers import FlattenObservation


# env = gym.make("CarRacing-v2", render_mode="human")
# observation, info = env.reset()

# for _ in range(1000):
#     action = env.action_space.sample()  # agent policy that uses the observation and info
#     observation, reward, terminated, truncated, info = env.step(action)
#     print(env.observation_space.shape)

#     if terminated or truncated:
#         observation, info = env.reset()

# env.close()


import gymnasium as gym

env = gym.make('HumanoidStandup-v4', render_mode="human")

# env = gym.make("FetchPickAndPlace-v2", render_mode="human")


observation, info = env.reset(seed=42)

iterations = 1000

import numpy as np

for i in range(iterations):
   # action = policy(observation)  # User-defined policy function
   action = env.action_space.sample()
   #print(action, type(action))
   # action = np.array([0.5, (2.0*float(i)/float(iterations))-1.0, 0.5,0.0])
   observation, reward, terminated, truncated, info = env.step(action)

#    if terminated or truncated:
#       observation, info = env.reset()

env.close()



