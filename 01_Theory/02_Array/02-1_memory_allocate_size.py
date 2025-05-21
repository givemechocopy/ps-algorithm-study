import struct

# struct format codes:
# 'c' = char (1 byte)
# 'i' = int (4 bytes)
# 'h' = short (2 bytes)
# 'f' = float (4 bytes)
# 'l' = long (보통 4 or 8 bytes depending on system)

# 개별 크기
char_size = struct.calcsize('c')
int_size = struct.calcsize('i')
short_size = struct.calcsize('h')
float_size = struct.calcsize('f')
long_size = struct.calcsize('l')

# 배열 크기 (100개 원소)
char_array_size = 100 * char_size
int_array_size = 100 * int_size
short_array_size = 100 * short_size
float_array_size = 100 * float_size
long_array_size = 100 * long_size

# 출력 (C 스타일)
print(f"char c 크기 = {char_size:2d} \t: char c_array 크기 = {char_array_size:4d}")
print(f"int i 크기 = {int_size:2d} \t: int i_array 크기 = {int_array_size:4d}")
print(f"short s 크기 = {short_size:2d} \t: short s_array 크기 = {short_array_size:4d}")
print(f"float f 크기 = {float_size:2d} \t: float f_array 크기 = {float_array_size:4d}")
print(f"long l 크기 = {long_size:2d} \t: long l_array 크기 = {long_array_size:4d}")
