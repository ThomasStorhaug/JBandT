def convertToRGB(hex:str):
    R = int(hex[0] + hex[1], 16)
    G = int(hex[2] + hex[3], 16)
    B = int(hex[4] + hex[5], 16)

    return (R,G,B)
    