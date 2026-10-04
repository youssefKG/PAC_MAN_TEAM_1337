from ctypes import CDLL, c_double, c_char_p, c_int, c_void_p, Structure, POINTER, byref, cast, pointer


libc = CDLL("libc.so.6")



class TimeVal(Structure):
    _fields_ = [("tv_sec", c_int), ("tv_usec", c_int)]


time_val = TimeVal()
time_val_pointer = byref(time_val)

libc.gettimeofday.argtypes = [POINTER(TimeVal), c_void_p]
libc.gettimeofday.restype = c_int
a: int = libc.gettimeofday(byref(time_val), None)
print(time_val_pointer.contents.tv_sec)
print(a)
print(time_val.tv_sec)
# print(libc.printf(b"hello word %s",  None))
