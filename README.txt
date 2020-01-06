# The purpose of this project is to import my Garmin Fitness Data, Parse the
.FIT file type and then figure out how the dynamic step count goal is
calculated.

Hyothesis:
The step count is calculated using a rolling average using n previous days to
keep the new step goal adaptable yet resistant to outlier days.  I also
believe that there is a lower limit for the step count, below which the step
count may decrease at a slower rate or not at all.

# TO DO:

1. Export my Garmin Connect Data from the past year.
2. Understand the file structure.
3. Build a parser to get the relevant data from the .FIT file.
4. Structure the parsed data.
5. Visualize and analyze the data acording to the hypothesis.
6. Recreate the algorithm and use k-fold cross validation to verify. 
