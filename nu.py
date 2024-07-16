def PlainTextToBinaryAlphanumeric(plainText):
    binaryList = [format(ord(char), '08b') for char in plainText]
    binaryString = ''.join(binaryList)
    return binaryString
