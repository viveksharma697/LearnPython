#  Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
# Sample Output:
# (255, 165, 1)
# (255, 255, 255)
# (0, 0, 0)
# (255, 0, 0)
# (0, 0, 128)
# (192, 192, 192)

def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)) 
print(hex_to_rgb('FFA501'))
print(hex_to_rgb('FFFFFF'))
print(hex_to_rgb('000000'))
print(hex_to_rgb('FF0000'))
print(hex_to_rgb('000080'))
print(hex_to_rgb('C0C0C0'))
