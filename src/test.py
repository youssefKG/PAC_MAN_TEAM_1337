from ctypes import CDLL, c_char_p, c_int, c_double, Structure, POINTER, c_void_p, byref



class TimeVal(Structure):
    _fields_ = [("tv_sec", c_int), ("tv_usec", c_int)]

libc = CDLL("libc.so.6")

printf = libc.printf
gettimeofday = libc.gettimeofday
gettimeofday.argtypes = [POINTER(TimeVal), c_void_p]
gettimeofday.restype = c_int
printf.argtypes = [c_char_p, c_double, c_int, c_char_p]
printf.restype = c_int


current_time: TimeVal = TimeVal()
gettimeofday(byref(current_time), None)
print(current_time.tv_sec)
# print(dir(current_time))
# print(current_time.contents.tv_sec)


printf(b"hello %.2f world %d %s", 10.10, 10, None)
