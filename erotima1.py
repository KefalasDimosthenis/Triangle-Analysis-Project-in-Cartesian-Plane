import random
import utils
import statistics

points = []
for i in range(100):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    point = (x, y)
    points.append(point)

areas = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        for k in range(j + 1, len(points)):
            a = utils.distance(points[i], points[j])
            b = utils.distance(points[j], points[k])
            c = utils.distance(points[k], points[i])

            if a + b > c and a + c > b and b + c > a:
                areas.append(utils.emvadon(points[i], points[j], points[k]))


print("Arithmos trigonon:", len(areas))
print("mesos oros:", utils.mesos_oros(areas))
print("Diamesos:", utils.diamesos(areas))
print("Tipiki apoklisi:", utils.tipiki_apoklisi(areas))

# Epiveveosi me statistics
print("\n Xrisi statistics:")
print("mesos oros:", statistics.mean(areas))
print("Diamesos:", statistics.median(areas))
print("Tipiki apoklisi:", statistics.stdev(areas))
