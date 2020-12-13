Parts of this code are adapted from Florent Poux, _How to automate LiDAR point cloud sub-sampling with Python_, but are rewritten to increase functionality
for our specific data sets. 

This program takes a list of .las files and plots subsets using three different methods: random sampling, 
barycenter of a voxel grid, and candidate center of a voxel grid.

Random sampling will plot one out of every (random factor) data points. The other two methods project a voxel grid onto the data set,
and plot either the barycenter or the closest data point to the barycenter. We can discuss the advantages/disadvantages of each of these three methods 
and decide how we can use them in our project. 

The `file_list` variable is formatted to plot the three files from the 2018 Blackmore data set, but this can be adapted to any of our .las files.
Just remember to download the files into the same directory as the python script before running!

I hope to maybe add some more functionality for preprocessing the data, adding colors, etc. sometime soon.

As always, feel free to reach out with questions or comments,

Eli
