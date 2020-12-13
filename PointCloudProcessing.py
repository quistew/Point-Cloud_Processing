# ----------------------------------+
# Eli Quist                         |
# December 2020                     |
# ----------------------------------+


import numpy as np
import laspy as lp
import matplotlib.pyplot as plt
import sys


class LasData:

    def __init__(self, file):
        self.point_cloud = lp.file.File(file, mode='r')
        self.points = np.vstack((self.point_cloud.x, self.point_cloud.y, self.point_cloud.z)).transpose()

    def get_random_data(self, rand_factor):
        random_subset = self.points[::rand_factor]
        return random_subset

    def get_barycenter_voxel_data(self, voxel_size):
        # nb_vox = np.ceil((np.max(self.points, axis=0) - np.min(self.points, axis=0)) / voxel_size)

        non_empty_voxel_keys, inverse, nb_pts_per_voxel = np.unique(
            ((self.points - np.min(self.points, axis=0)) // voxel_size).astype(int), axis=0, return_inverse=True,
            return_counts=True)
        idx_pts_vox_sorted = np.argsort(inverse)

        voxel_grid = {}
        grid_barycenter = []
        last_seen = 0

        for idx, vox in enumerate(non_empty_voxel_keys):
            voxel_grid[tuple(vox)] = self.points[idx_pts_vox_sorted[last_seen:last_seen + nb_pts_per_voxel[idx]]]
            grid_barycenter.append(np.mean(voxel_grid[tuple(vox)], axis=0))
            last_seen += nb_pts_per_voxel[idx]
        return grid_barycenter

    def get_candidate_center_voxel_data(self, voxel_size):
        # nb_vox = np.ceil((np.max(self.points, axis=0) - np.min(self.points, axis=0)) / voxel_size)

        non_empty_voxel_keys, inverse, nb_pts_per_voxel = np.unique(
            ((self.points - np.min(self.points, axis=0)) // voxel_size).astype(int), axis=0, return_inverse=True,
            return_counts=True)
        idx_pts_vox_sorted = np.argsort(inverse)

        voxel_grid = {}
        grid_candidate_center = []
        last_seen = 0

        for idx, vox in enumerate(non_empty_voxel_keys):
            voxel_grid[tuple(vox)] = self.points[idx_pts_vox_sorted[last_seen:last_seen + nb_pts_per_voxel[idx]]]
            grid_candidate_center.append(voxel_grid[tuple(vox)][np.linalg.norm(voxel_grid[tuple(vox)] -
                                                                               np.mean(voxel_grid[tuple(vox)], axis=0), axis=1).argmin()])
            last_seen += nb_pts_per_voxel[idx]
        return grid_candidate_center


def plot_random_sampling(file_list, rand_factor):
    ax = plt.axes(projection='3d')
    for item in file_list:
        file = LasData(item)
        random_subset = file.get_random_data(rand_factor)
        ax.scatter(random_subset[:, 0], random_subset[:, 1], random_subset[:, 2], s=1)
    plt.show()


def plot_barycenter_sampling(file_list, voxel_size):
    ax = plt.axes(projection='3d')
    for item in file_list:
        file = LasData(item)
        barycenter_subset_array = np.array(file.get_barycenter_voxel_data(voxel_size))
        ax.scatter(barycenter_subset_array[:, 0], barycenter_subset_array[:, 1], barycenter_subset_array[:, 2])
    plt.show()


def plot_candidate_center_sampling(file_list, voxel_size):
    ax = plt.axes(projection='3d')
    for item in file_list:
        file = LasData(item)
        candidate_center_array = np.array(file.get_candidate_center_voxel_data(voxel_size))
        ax.scatter(candidate_center_array[:, 0], candidate_center_array[:, 1], candidate_center_array[:, 2])
    plt.show()


def main():
    # feel free to edit this file list to view other data. This is set up to read in the 3 files from the 2018 Blackmore data set.
    file_list = ["Mid_Glacier_Merged_T.las", "Lone_Peak_Observatory_Merged_T.las", "Lower_Glacier_Merged_T.las"]

    # uncomment desired subsampling technique, and feel free to play around with different sample sizes
    # plot_random_sampling(file_list, 15000)
    # plot_barycenter_sampling(file_list, 30)
    # plot_candidate_center_sampling(file_list, 30)


main()
print(sys.version)
