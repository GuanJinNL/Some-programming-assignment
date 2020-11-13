import unittest
import Yak
from Yak import yak


class TestStockstatus(unittest.TestCase):

    def test_Stockstatus(self):  # assignment examples
        Herd = []
        age = [4, 8, 9.5]
        sex = ['f', 'f', 'f']
        for a,s in zip(age,sex):
            NewYak = yak()
            NewYak.age = a
            NewYak.sex = s
            Herd.append(NewYak)
        for T in [13,14]:
            if T == 13:
                A1 = [1104.48, 3]
                A2 = [4.13, 8.13, 9.63]
            else:
                A1 = [1188.81, 4]
                A2 = [4.14, 8.14, 9.64]
            for i in range(3):
                if i == 2:
                    for j in range(3):
                        self.assertAlmostEqual(Yak.Stockstatus(Herd, T)[2][i], A2[i], places=2)
                else:
                    self.assertAlmostEqual(Yak.Stockstatus(Herd, T)[i], A1[i], places=2)

    def test_Stockstatus2(self):  # boundary condition test: day 0
        A1 = [0, 0]
        A2 = [5, 4, 8]
        Herd = []
        age = [5, 4, 8]
        sex = ['f', 'f', 'f']
        for a, s in zip(age, sex):
            NewYak = yak()
            NewYak.age = a
            NewYak.sex = s
            Herd.append(NewYak)
        for i in range(3):
            if i == 2:
                for j in range(3):
                    self.assertAlmostEqual(Yak.Stockstatus(Herd, 0)[2][i], A2[i], places=2)
            else:
                self.assertAlmostEqual(Yak.Stockstatus(Herd, 0)[i], A1[i], places=2)

    def test_Stockstatus3(self):  # boundary condition test: starting with dead yaks
        A1 = [0, 0]
        A2 = [10, 10, 10]
        Herd = []
        age = [10, 10, 10]
        sex = ['f', 'f', 'f']
        for a, s in zip(age, sex):
            NewYak = yak()
            NewYak.age = a
            NewYak.sex = s
            Herd.append(NewYak)
        for i in range(3):
            if i == 2:
                for j in range(3):
                    self.assertAlmostEqual(Yak.Stockstatus(Herd, 12)[2][i], A2[i], places=2)
            else:
                self.assertAlmostEqual(Yak.Stockstatus(Herd, 0)[i], A1[i], places=2)

    def test_Stockstatus4(self):  # boundary condition test: yaks below age 1 and some are male
        A1 = [1167.24, 0]
        A2 = [0.62, 0.52, 0.42]
        Herd = []
        age = [0.5, 0.4, 0.3]
        sex = ['f', 'm', 'f']
        for a, s in zip(age, sex):
            NewYak = yak()
            NewYak.age = a
            NewYak.sex = s
            Herd.append(NewYak)
        for i in range(3):
            if i == 2:
                for j in range(3):
                    self.assertAlmostEqual(Yak.Stockstatus(Herd, 12)[2][i], A2[i], places=2)
            else:
                self.assertAlmostEqual(Yak.Stockstatus(Herd, 12)[i], A1[i], places=2)


if __name__ == '__main__':
    unittest.main()
