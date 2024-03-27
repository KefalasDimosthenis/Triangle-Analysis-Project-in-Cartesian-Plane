import unittest
import statistics
import utils


class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        with open("points.txt", "r") as file:
            points = [tuple(map(int, line.strip().split())) for line in file]
        areas = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    a = utils.emvadon(points[i], points[j], points[k])
                    if a > 0.0:  # Egkiro trigono
                        areas.append(a)

        # apotelesmata
        self.assertEqual(len(areas), 161672)
        self.assertAlmostEqual(round(statistics.mean(areas), 2), 3206.82, places=0)
        self.assertAlmostEqual(statistics.median(areas), 2392.50, places=2)
        self.assertAlmostEqual(statistics.stdev(areas), 2843.24, places=2)


if True:
    unittest.main()
