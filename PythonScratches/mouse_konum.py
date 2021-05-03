import ctypes

class POINT(ctypes.Structure):
    _fields_=[("x",ctypes.c_long),("y",ctypes.c_long)]

def mouse_konumu():
    c_point=POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(c_point))
    return c_point.x,c_point.y

"""
while True:
    print(mouse_konumu())
"""

