# **Gymnasium python**
- 強化學習套件，有測試強化學習的環境
- list all environment`python3 list_env.py`
```
# list_env.py

import gymnasium as gym
env_specs = gym.envs.registry
env_list = [env_spec for env_spec in env_specs]
print(env_list)
```
- 將環境的相關資訊顯示`python3 env_help.py target_env`
```
# env_help.py

import gymnasium as gym
import sys
env = gym.make(sys.argv[1], render_mode="egb_array")
help(env.unwrapped)
```
- 
# **強化學習算法**
- Qlearning：

