#!/usr/bin/env python3

class Ring:
    def __init__(self, levels):
        self.levels = levels

    def rotate(self, level):
        self.levels[level].append(self.levels[level].pop(0))

    def get_num(self, row):
        for level in self.levels:
            if level[row] != 0:
                return level[row]

class Tower:
    def __init__(self, rings):
        self.tower = rings
        self.rotations = [0, 0, 0, 0, 0]

    def rotate_gear(self, level):
        for ring in self.tower:
            ring.rotate(level)

        self.rotations[level] += 1
        if self.rotations[level] == 12 and level < 4:
            self.rotate_gear(level+1)
            self.rotations[level] = 0

    def get_sum(self, row):
        total = 0
        for ring in self.tower:
            total += ring.get_num(row)
        return total

    def check_all_row_sums(self):
        for i in range(12):
            if self.get_sum(i) != 42:
                return False
        return True

    def solve(self):
        while tower.rotations[4] < 12:
            tower.rotate_gear(0)
            if tower.check_all_row_sums():
                print(tower.rotations) 
                break

if __name__=="__main__":
    inner_ring = Ring([
        [3,  0,  6,  0, 10,  0,  7,  0, 15,  0,  8,  0],
        [7,  3,  0,  6,  0, 11, 11,  6, 11,  0,  6, 17],
        [9, 13,  9,  7, 13, 21, 17,  4,  5,  0,  7,  8],
        [7,  0,  9,  0,  7, 14, 11,  0,  8,  0, 16,  2],
        [11, 11, 14, 11, 14, 11, 14, 14, 11, 14, 11, 14]
    ]) # Verified
    mid1_ring = Ring([
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [4,  0,  7, 15,  0,  0, 14,  0,  9,  0, 12,  0],
        [21,  6, 15,  4,  9, 18, 11, 26, 14,  1, 12,  0],
        [9, 20, 12,  3,  6,  0, 14, 12,  3,  8,  9,  0],
        [ 4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]
    ]) # Verified, but mid1_ring[2][9] is ambiguous, could be 7
    mid2_ring = Ring([
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [5,  0, 10,  0,  8,  0, 22,  0, 16,  0,  9,  0],
        [3, 26,  6,  0,  2, 13,  9,  0, 17, 19,  3, 12],
        [ 4,  4,  6,  6,  3,  3, 14, 14, 21, 21,  9,  9],
        ]) # Verified
    outer_ring = Ring([
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [1,  0,  9,  0, 12,  0,  6,  0, 10,  0, 10,  0],
        [ 8,  3,  4, 12,  2,  5, 10,  7, 16,  8,  7,  8]
    ]) # Verified
    tower = Tower([inner_ring, mid1_ring, mid2_ring, outer_ring])

    tower.solve()



