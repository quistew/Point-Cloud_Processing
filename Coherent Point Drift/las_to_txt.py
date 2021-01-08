import numpy as np
import laspy as lp
import sys


class LasData:

    def __init__(self, file):
        self.point_cloud = lp.file.File(file, mode='r')
        self.points = np.vstack((self.point_cloud.x, self.point_cloud.y, self.point_cloud.z)).transpose()

    def write_to_text(self,file_name):
        txt_file = open(f"{file_name}.txt", "w")
        for coord_set in self.points:
            txt_file.write((str(coord_set[0]) + " " + str(coord_set[1]) + " " + str(coord_set[2]) + "\n"))
        txt_file.close()


def main():
    file = LasData("2018_selection_1.las")
    file.write_to_text("2018_source")


main()
print('\n' + sys.version)
