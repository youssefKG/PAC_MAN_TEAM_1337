from ctypes import CDLL


lib = CDLL("libc.so.6")


lib.printf(b"hello world %f", 10.0)
