import numpy as np
import pandas as pd

"""This application will take a set of daily step data and calculate a step goal,
while trying to recreate the Garmin Forerunner 35 step goal calculations as close as possible.
"""

df = pd.read_csv(r'Data/example.csv')

# Set initial Step Goal
goal_init = 7500

"""Process:
- Run Categorizer over incoming data to sort it into the 4 buckets
- Run each line through their designated case function
- Check result against outlier cases
- Post results and continue onto the next line
"""

# Write the 4 different possible cases

# Positive + Consecutive

# Positive + Non-Consecutive

# Negative + Consecutive

# Positive + Non-Consecutive
