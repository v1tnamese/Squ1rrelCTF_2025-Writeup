
# 🐔 Steganography Challenge: Suspicious Chicken

## 🧩 Challenge Overview

We were given two PNG images:

- 📍 `treasure_map.png`: A black-and-white image acting as a guide.
- 🐔 `suspicious_chicken.png`: A colorful image believed to contain hidden information.

The objective was to extract a **hidden flag** using information from both images. It was clear from the context that this was a **Least Significant Bit (LSB) steganography** challenge.

---

## 🔍 Approach

### 🗺️ Step 1: Extract Coordinates from the Map

The map image acts as a filter to indicate **which pixels** from the chicken image are significant. Any pixel in `treasure_map.png` that is **not white** is treated as a coordinate to be read from the second image.

```python
def get_coordinates(map_img):
    coords = []
    for y in range(height): 
        for x in range(width):
            r, g, b = map_img.getpixel((x, y))
            if (r, g, b) != (255, 255, 255):  # Non-white = valid point
                coords.append((x, y))
    return coords
```

---

### 🎯 Step 2: Extract Bits from the Chicken Image

At each valid coordinate (x, y), we read the **LSB of the red channel** from the suspicious chicken image.

```python
def extract_bits(image, coords, bit_plane=0, channel='red', bit_order='LSB'):
    bits = ""
    for (x, y) in coords:
        r, g, b = image.getpixel((x, y))
        if channel == 'red':
            color_value = r
        # Select LSB or MSB from chosen channel
        if bit_order == 'LSB':
            bit = (color_value >> bit_plane) & 1
        elif bit_order == 'MSB':
            bit = (color_value >> (7 - bit_plane)) & 1
        bits += str(bit)
    return bits
```

> 🔧 In our case, we chose:
> - `bit_plane = 0` (LSB)
> - `channel = 'red'`
> - `bit_order = 'LSB'`

---

### 🧠 Step 3: Convert Bits to ASCII

Bits are grouped into bytes (8 bits) and converted to ASCII to reveal the hidden flag.

```python
def bits_to_ascii(bits):
    flag = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            flag += chr(int(byte, 2))
    return flag
```

---

## 🧪 Full Script

```python
from PIL import Image

# Load both images
map_img = Image.open("treasure_map.png").convert("RGB")
data_img = Image.open("suspicious_chicken.png").convert("RGB")

# Extract non-white coordinates from the map
coords = get_coordinates(map_img)

# Extract bits from chicken image
bits = extract_bits(data_img, coords, bit_plane=0, channel='red', bit_order='LSB')

# Decode to ASCII
flag = bits_to_ascii(bits)
print("Extracted flag:", flag)
```

---

## 🏁 Final Output

The decoded output gave us the flag:

```bash
Extracted flag: squ1rrelctf{why_w0u1d_u_fo11ow_4_chicken}
```


