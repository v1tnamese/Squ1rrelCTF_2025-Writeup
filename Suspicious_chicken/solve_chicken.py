from PIL import Image

def extract_bits(image, coords, bit_plane=0, channel='red', bit_order='LSB', direction='row'):
    bits = ""
    for (x, y) in coords:
        r, g, b = image.getpixel((x, y))
        if channel == 'red':
            color_value = r
        elif channel == 'green':
            color_value = g
        elif channel == 'blue':
            color_value = b
        else:
            raise ValueError("Invalid channel selected")

        if bit_order == 'LSB':
            bit = (color_value >> bit_plane) & 1
        elif bit_order == 'MSB':
            bit = (color_value >> (7 - bit_plane)) & 1
        else:
            raise ValueError("Invalid bit order selected")

        bits += str(bit)
    return bits

def bits_to_ascii(bits):
    flag = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        flag += chr(int(byte, 2))
    return flag

def get_coordinates(img):
    coords = []
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if img.getpixel((x, y)) != (255, 255, 255):
                coords.append((x, y))
    return coords

map_img = Image.open("treasure_map.png").convert("RGB")
data_img = Image.open("suspicious_chicken.png").convert("RGB")
coords = get_coordinates(map_img)

bit_plane = 0
channel = 'red'
bit_order = 'LSB'
direction = 'row'

bits = extract_bits(data_img, coords, bit_plane, channel, bit_order, direction)
flag = bits_to_ascii(bits)
print("Extracted flag:", flag)
