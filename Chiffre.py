import binascii

msg = '6262db1240b04de23039e0c96a344f1af85ad677d0444c279808dd0440db'
hex = binascii.hexlify(msg)
print "Hex:  ", hex
print "unHex:", binascii.unhexlify(hex)

hex = binascii.hexlify(b'foo')
print "Hex:  ", hex
print "unHex:", binascii.unhexlify(hex)
