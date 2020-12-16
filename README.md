As we begin to think about mdoeling how this glacier moves, there are two directions which may help us stablize and register our data set.
The first is to think about general (and continuous) transformation across the entire data set. 
The second is to look at specific, smaller areas of stable terrain to allow for more precise measurement of geometric transformations.

For both of these methods, we will need to implement large scale filtration of our data set, as found in the `Sample Concentration Filtering` directory.
Poux introduces 3 different methods: random sampling, barycenter sampling, and candidate center sampling. Random sampling will plot one data point out of a specified random factor.
Barycenter sampling projects a voxel grid onto the dataset, and plots the center point of each voxel cell.
Candidate center sampling projects this same voxel grid, but plots the closest data point to the center point of the voxel (measured with Euclidean distance).

Beyond this large scale data filtration, we may want to extract small area subsamples (that are high in data concentration) for a precise measurement of geometric transformation across a
small physical area. In this case, one possibility for subsampling is through generating slices of the array. Example code and images for this process can be found in `Area\ Filtering/Array\ Slicing`. Unfortunately, this does not give an easy way to utilize specificity to a certain 
geographic area, but this data is not georegistered anyway. It is much simpler than extracting certain voxels, and these voxel grids are projected specifically onto the dataset anyway, so they would
not necessarily match other datasets (although I plan to look into this concept further). What we do get is a high concentration of data (that we can decide to filter more or less) that can be as
precise as the initial sampling. 

As always, feel free to reach out with questions or comments,

Eli

Parts of this code are adpated from Florent Poux, _How to automate LiDAR point cloud sub-sampling with Python_.
