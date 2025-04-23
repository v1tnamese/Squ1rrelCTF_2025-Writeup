Writeup: Hidden Bits in the Chicken (Steganography Challenge)
Challenge Description:
We were given two images:

🗺️ treasure_map.png: A black-and-white image hinting at "where" to look.

🐔 suspicious_chicken.png: A colorful image suspected of hiding something.

The goal was to extract a hidden flag from suspicious_chicken.png using the "coordinates" from the treasure_map.png.

💡 Initial Observations
The challenge likely uses LSB (Least Significant Bit) steganography.

The treasure map indicates which pixels contain useful data.

The actual hidden content is embedded in the LSBs of some color channel (Red, Green, or Blue) of suspicious_chicken.png.

🔍 Strategy
Identify all non-white pixels in the map image. These pixels act as coordinates.

For each such pixel, extract the LSB of the red channel at the same location in the chicken image.

Collect the bits and reconstruct bytes to retrieve ASCII characters.

Print the decoded message — which turns out to be the flag.

🧠 Code Explanation
1. Collecting Coordinates from the Map

def get_coordinates(map_img):
    coords = []
    for y in range(height): 
        for x in range(width):
            r, g, b = map_img.getpixel((x, y))
            if (r, g, b) != (255, 255, 255):  # skip white pixels
                coords.append((x, y))
    return coords
This function parses through every pixel in treasure_map.png and selects coordinates that aren't white, marking them as important data points.

2. Extracting Bits

def extract_bits(image, coords, bit_plane=0, channel='red', bit_order='LSB'):
    bits = ""
    for (x, y) in coords:
        r, g, b = image.getpixel((x, y))
        if channel == 'red':
            value = r
        # ...
        bit = (value >> bit_plane) & 1  # LSB extraction
        bits += str(bit)
    return bits
We extract bit 0 (LSB) of the Red channel for every coordinate, and collect the result in a string of bits.

3. Converting Bits to ASCII

def bits_to_ascii(bits):
    flag = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            flag += chr(int(byte, 2))
    return flag
Every 8 bits are grouped to form a byte, then converted to characters.

🏁 Output
Finally, after running the script:


flag = bits_to_ascii(bits)
print("Extracted flag:", flag)
You’ll get the hidden flag in the format like squ1rrel{...} or similar.

✅ Conclusion
This challenge is a creative combination of map-based coordinate selection and LSB steganography. By using one image as a navigation map and the other as the data carrier, it simulates a realistic and clever way to conceal information visually.

🔐 A great reminder: Not all secrets are encrypted — sometimes they're just... pixel-deep.