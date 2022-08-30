import struct
import enum


class FormatType(enum.Enum):

    FLOAT = "float_binary_format"
    BINARY = "binary_format"


def float_to_bin(f, format_type: FormatType = FormatType.BINARY):
    """Convert a 32-bit float to binary."""
    bytes = struct.pack('<f', f)
    base10 = struct.unpack('<I', bytes)[0]
    binary = bin(base10)[2:]

    if format_type is FormatType.BINARY:
        return " ".join([
            binary[:-24].zfill(8),
            binary[-24:-16],
            binary[-16:-8],
            binary[-8:]
        ])
    else:
        return " ". join([
            binary[-32:-31].zfill(1),
            binary[-31:-23].zfill(8),
            binary[-23:]
        ])


def bin_to_sembin(binary: str):
    sign, exponent, mantissa = binary.split(" ")
    # 计算出移动偏移量
    exponent = int(f"0b{exponent}", 2) - 127
    # 小数点向右偏移
    mantissa = "".join(["1", f"{mantissa}"[:exponent], ".", f"{mantissa}"[exponent:]])
    return mantissa


def sembin_to_float(binary, length):
    # Fetch the radix point
    point = binary.find('.')

    # Update point if not found
    if (point == -1):
        point = length

    intDecimal = 0
    fracDecimal = 0
    twos = 1

    # Convert integral part of binary
    # to decimal equivalent
    for i in range(point - 1, -1, -1):
        # Subtract '0' to convert
        # character into integer
        intDecimal += ((ord(binary[i]) -
                        ord('0')) * twos)
        twos *= 2

    # Convert fractional part of binary
    # to decimal equivalent
    twos = 2

    for i in range(point + 1, length):
        fracDecimal += ((ord(binary[i]) -
                         ord('0')) / twos)
        twos *= 2.0

    # Add both integral and fractional part
    ans = intDecimal + fracDecimal

    return ans


# expect_value = 20.59375
# sem_binary = float_to_bin(expect_value, format_type=FormatType.FLOAT)       # 0 10000011 01001001100000000000000
# sem_float = bin_to_sembin(sem_binary)                                       # 10100.1001100000000000000
# float_value = sembin_to_float(sem_float, len(sem_float))                    # 20.59375


expect_value = 1234.593
sem_binary = float_to_bin(expect_value, format_type=FormatType.FLOAT)        # 0 10001001 00110100101001011111010
sem_float = bin_to_sembin(sem_binary)                                           # 10011010010.1001011111010
float_value = sembin_to_float(sem_float, len(sem_float))
print("ss")






# print(float_to_bin(1.0))                                  # 00111111 10000000 00000000 00000000
# print(float_to_bin(0.99999999))                           # 00111111 10000000 00000000 00000000
# print(float_to_bin(0.9999999))                            # 00111111 01111111 11111111 11111110
# print(float_to_bin(1234.9999999))                         # 00111111 01111111 11111111 11111110
#
#
# print(float_to_bin(1.0, FormatType.FLOAT))                # 0 01111111 00000000000000000000000
# print(float_to_bin(0.99999999, FormatType.FLOAT))         # 0 01111111 00000000000000000000000
# print(float_to_bin(0.9999999, FormatType.FLOAT))          # 0 01111110 11111111111111111111110
# print(float_to_bin(1234.9999999, FormatType.FLOAT))       # 0 10001001 00110100110000000000000
# print(float_to_bin(-1234.9999999, FormatType.FLOAT))      # 1 10001001 00110100110000000000000
# print(float_to_bin(254.9999999, FormatType.FLOAT))        # 0 10000110 11111110000000000000000
# print(float_to_bin(255.9999999, FormatType.FLOAT))        # 0 10000111 00000000000000000000000
# print(float_to_bin(9999.9999999, FormatType.FLOAT))       # 0 10001100 00111000100000000000000
#
# print(bin_to_float("0b01000001101001001100000000000000"))        # 10100.1001100000000000000
#
# print(binaryToDecimal("10100.1001100000000000000", len("10100.1001100000000000000")))
