from ctypes import *

module = cdll.LoadLibrary('./sin_n_times.dll')
module.sin_n_times(10000000)
module.sin_n_times(100000000)
module.sin_n_times(1000000000)