from .func import func
import threading


def EseLinear(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeLinear, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInQuad(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInQuad, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseOutQuad(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeOutQuad, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInOutQuad(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInOutQuad, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInSine(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInSine, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseOutSine(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeOutSine, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInOutSine(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInOutSine, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInExpo(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInExpo, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseOutExpo(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeOutExpo, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInOutExpo(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInOutExpo, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInCirc(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInCirc, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInOutQuart(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInOutQuart, args=(obj, x_or_y, startPos, Endpos, speed)).start()

def EaseInElastic(obj, x_or_y, startPos, Endpos, speed):
    threading.Thread(target=func.easeInElastic, args=(obj, x_or_y, startPos, Endpos, speed)).start()
