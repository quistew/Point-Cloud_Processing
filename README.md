### Array Slicing
This script slices the data matrix to plot a specific subsample of the data set. 
This technique of data subsampling did not give us the ability to easily combine data selection with visualization. 
Although it can be very precise, it is difficult to accurately select the stable regions that we wanted to subsample.

### Coherent Point Drift
Find transformation matrix between two point cloud data sets using the Coherent Point Drift Algorithm.
Adapted from https://github.com/siavashk/pycpd, and the journal article, https://arxiv.org/pdf/0905.2635.pdf.

### Sample Concentration Filtering
This code is adapted from Florent Poux, _How to automate LiDAR point cloud sub-sampling with Python_ 
https://towardsdatascience.com/how-to-automate-lidar-point-cloud-processing-with-python-a027454a536c.
Utilizes three techniques:
1. Random sampling: using one randomly sampled data point to represent a set number of data points
2. Barycenter sampling: projecting a voxel grid onto the data set (of various size), and using the center of each voxel cell as the representative point
3. Candidate center sampling: projecting a voxel grid onto the data set (of various size), and using the closest data point to the true center of each voxel (determined by euclidean distance) as the representative point


