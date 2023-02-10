# Operator Bitwise, biner, binary

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print('\n====== OR ======')
print('nilai :', a, ', Binary: ', format(a, '08b'))
print('nilai :', b, ', Binary: ', format(b, '08b'))
print('----------------------------- (|)')
print('nilai :', c, ', Binary:', format(c, '08b'))

# Bitwise AND (&)
c = a & b
print('\n====== AND ======')
print('nilai :', a, ', Binary: ', format(a, '08b'))
print('nilai :', b, ', Binary: ', format(b, '08b'))
print('----------------------------- (&)')
print('nilai :', c, ', Binary:', format(c, ' 08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n====== XOR ======')
print('nilai :', a, ', Binary: ', format(a, '08b'))
print('nilai :', b, ', Binary: ', format(b, '08b'))
print('----------------------------- (^)')
print('nilai :', c, ', Binary:', format(c, '08b'))


# Bitwise Not (~)
c = ~a
print('\n====== NOT ======')
print('nilai :', a, ', Binary: ', format(a, '08b'))
print('----------------------------- (~)')
print('nilai :', c, ', Binary:', format(c, '08b'))
print('----------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai =', e ^ d, ', Binary:', format(e ^ d, '08b'))


# Shifting
# shif right (>>)
c = a >> 2
print('\n====== Shif Right ======')
print('nilai :', a, ', Binary: ', format(a, '08b'))
print('----------------------------- (>>)')
print('nilai :', c, ', Binary:', format(c, '08b'))

# shif Left (<<)
c = a << 2
print('\n====== Shif Left ======')
print('nilai :', a, ', Binary: ', format(a, '08b'))
print('----------------------------- (<<)')
print('nilai :', c, ', Binary:', format(c, '08b'))
