# ----------------------------------+
# Eli Quist                         |
# December 2020                     |
# ----------------------------------+
# This script generates a subset of |
# point cloud data through two      |
# filtering mechanisms. The first   |
# by subsampling through a voxel    |
# projection and plotting only the  |
# point closest to the barycenter   |
# of each voxel grid. Second, the   |
# data is filtered by only plotting |
# a specific slice of the data set. |
# ----------------------------------+

import numpy as np
import laspy as lp
import matplotlib.pyplot as plt
import sys


def get_candidate_center_voxel_data(points, voxel_size):
    non_empty_voxel_keys, inverse, nb_pts_per_voxel = np.unique(
            ((points - np.min(points, axis=0)) // voxel_size).astype(int), axis=0, return_inverse=True,
            return_counts=True)
    idx_pts_vox_sorted = np.argsort(inverse)

    voxel_grid = {}
    grid_candidate_center = []
    last_seen = 0

    for idx, vox in enumerate(non_empty_voxel_keys):
        voxel_grid[tuple(vox)] = points[idx_pts_vox_sorted[last_seen:last_seen + nb_pts_per_voxel[idx]]]
        grid_candidate_center.append(voxel_grid[tuple(vox)][np.linalg.norm(voxel_grid[tuple(vox)] -
                                                                               np.mean(voxel_grid[tuple(vox)], axis=0), axis=1).argmin()])
        last_seen += nb_pts_per_voxel[idx]
    return grid_candidate_center


def main():
    input_file = "Lower_Glacier_Merged_T.las"

    voxel_size = 5
    slice_start = 250
    slice_end = 1000

    ax = plt.axes(projection='3d')
    point_cloud = lp.file.File(input_file, mode='r')
    points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
    candidate_center_array = np.array(get_candidate_center_voxel_data(points, voxel_size))
    ax.scatter(candidate_center_array[slice_start:slice_end, 0], candidate_center_array[slice_start:slice_end, 1],
               candidate_center_array[slice_start:slice_end, 2])
    plt.show()


main()
print(sys.version)
