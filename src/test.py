from ctypes import CDLL, c_char_p, c_double, byref, Structure, c_int, POINTER, byref, c_void_p, cast


lib = CDLL("libc.so.6")


class Time(Structure):
    _fields_ = [("tv_sec", c_int), ("tv_usec", c_int)]


time = Time()
time_ref = byref(time)
lib.gettimeofday.argtypes = [POINTER(Time), c_void_p]
lib.gettimeofday.restype = c_int
print(lib.gettimeofday(time_ref, None))
print(dir(cast(time_ref, POINTER(Time)).contents))
