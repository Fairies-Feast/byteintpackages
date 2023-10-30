from __byteint import stdin
class key:
  UP = " "
  DOWN = "-"
  LEFT = "+"
  RIGHT = "_"
  ENTER = "!"
def readkey():
  R = stdin()
  if R == "UpArrow":
    return key.UP
  elif R == "DownArrow":
    return key.DOWN
  elif R == "LeftArrow":
    return key.LEFT
  elif R == "RightArrow":
    return key.RIGHT
  elif R == "Enter":
    return key.ENTER
  else:
    return R
