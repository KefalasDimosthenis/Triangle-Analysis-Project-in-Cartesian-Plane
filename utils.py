import math


def distance(point1, point2):

    (x1, y1) = point1
    (x2, y2) = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def emvadon(p1, p2, p3):

    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    if a + b <= c or b + c <= a or c + a <= b:
        return 0
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def mesos_oros(x):
    plithos = len(x)
    sinolo = 0

    for i in range(plithos):
        sinolo += x[i]

    return "{:.2f}".format(float(sinolo) / plithos, 2)


def diamesos(x):
    t = sorted(x)
    n = len(t)
    if n % 2 == 0:
        simio1 = t[int(n / 2)]
        simio2 = t[(int(n / 2)) - 1]
        return (simio1 + simio2) / 2
    else:
        return "{:.2f}".format(t[int(n / 2)], 2)


def evros(x):
    apotelesma = max(x) - min(x)

    return apotelesma


def tipiki_apoklisi(x):
    megethos = len(x)
    mes_oross = mesos_oros(x)
    t = []
    for i in x:
        t.append((i - float(mes_oross)) ** 2)
    diafora = sum(t) / megethos
    apotelesma = "{:.2f}".format(math.sqrt(float(diafora)))
    return apotelesma
