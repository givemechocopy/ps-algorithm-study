import sys
import array

# 변수 1개
c = b'a'    # char
i = 1       # int
s = 1       # short
f = 1.0     # float
l = 1       # long

# 배열 (array 모듈 사용: 고정형 배열)
c_array = array.array('b', [0] * 100)     # signed char
i_array = array.array('i', [0] * 100)     # signed int
s_array = array.array('h', [0] * 100)     # signed short
f_array = array.array('f', [0.0] * 100)   # float
l_array = array.array('l', [0] * 100)     # signed long

print(f"\n char c 크기 = {sys.getsizeof(c)}\t: char c_array 크기 = {sys.getsizeof(c_array)}")
print(f"\n int i 크기 = {sys.getsizeof(i)}\t: int i_array 크기 = {sys.getsizeof(i_array)}")
print(f"\n short s 크기 = {sys.getsizeof(s)}\t: short s_array 크기 = {sys.getsizeof(s_array)}")
print(f"\n float f 크기 = {sys.getsizeof(f)}\t: float f_array 크기 = {sys.getsizeof(f_array)}")
print(f"\n long l 크기 = {sys.getsizeof(l)}\t: long l_array 크기 = {sys.getsizeof(l_array)}")
