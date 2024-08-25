import time
import math


def easeLinear_bmp(t, b, c, d):
    return c * t / d + b
def easeLinear(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeLinear_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeInQuad_bmp(t, b, c, d):
    return c * (t / d) * t + b
def easeInQuad(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInQuad_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeOutQuad_bmp (t, b, c, d):
    return -c * (t / d) * (t - 2) + b
def easeOutQuad(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeOutQuad_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeInOutQuad_bmp (t, b, c, d):
    if (t / d / 2) < 1:
        return c / 2 * t * t + b
    return -c / 2 * ((--t) * (t - 2) - 1) + b
def easeInOutQuad(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInOutQuad_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeInSine_bmp (t, b, c, d):
    return -c * math.cos(t / d * (math.pi / 2)) + c + b
def easeInSine(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInSine_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeOutSine_bmp(t, b, c, d):
    return c * math.sin(t / d * (math.pi / 2)) + b
def easeOutSine(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeOutSine_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)



def easeInOutSine_bmp(t, b, c, d):
    return -c / 2 * (math.cos(math.pi * t / d) - 1) + b
def easeInOutSine(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInOutSine_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeInExpo_bmp(t, b, c, d):
    return b if t == 0 else c * math.pow(2, 10 * (t / d - 1)) + b
def easeInExpo(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInExpo_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeOutExpo_bmp(t, b, c, d):
    return b + c if t == d else c * (-math.pow(2, -10 * t / d) + 1) + b
def easeOutExpo(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeOutExpo_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeInOutExpo_bmp(t, b, c, d):
    if t == 0:
        return b
    if t == d:
        return b + c
    if (t / d / 2) < 1:
        return c / 2 * math.pow(2, 10 * (t - 1)) + b
    return c / 2 * (-math.pow(2, -10 * --t) + 2) + b
def easeInOutExpo(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInOutExpo_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)

def easeInCirc_bmp(t, b, c, d):
    return -c * (math.sqrt(1 - (t / d) * t) - 1) + b
def easeInCirc(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInCirc_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


def easeInOutQuart_bmp(t, b, c, d):
    if (t / d / 2) < 1:
        return c / 2 * t * t * t * t + b
    return -c / 2 * ((t - 2) * t * t * t - 2) + b

def easeInOutQuart(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInOutQuart_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)



def easeInElastic_bmp(t, b, c, d):
    s = 1.70158
    p = 0
    a = c
    if t == 0:
        return b
    if (t / d) == 1:
        return b + c
    if not p:
        p = d * .3
    if a < abs(c):
        a = c
        s = p / 4
    else:
        s = p / (2 * math.pi) * math.asin(c / a)
    return -(a * math.pow(2, 10 * (t - 1)) * math.sin((t * d - s) * (2 * math.pi) / p)) + b
def easeInElastic(obj, x_or_y, startPos, Endpos, speed):
    startTime = time.time()
    while True:
        t = time.time() - startTime
        position = easeInElastic_bmp(t, startPos, Endpos, speed)
        if position >= Endpos:
            break
        else:
            if x_or_y.upper() == "x".upper():
                obj.place(x=position)
            elif x_or_y.upper() == "y".upper():
                obj.place(y=position)


