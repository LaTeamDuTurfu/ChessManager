import math


def csc(angle_radians: float) -> float:
    if 0 > angle_radians > 2 * math.pi:
        raise ValueError("Veuillez fournir l'angle en radian dans l'intervalle [0, 2pi]")

    return 1 / math.sin(angle_radians)


def sec(angle_radians: float) -> float:
    return 1 / math.cos(angle_radians)
