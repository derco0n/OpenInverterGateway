#!/usr/bin/python3

def combine_to_16bit_integer(byte1, byte2):
    # Stellen Sie sicher, dass die Eingaben 8-Bit-Werte sind
    if not (0 <= byte1 <= 255 and 0 <= byte2 <= 255):
        raise ValueError("Beide Eingaben müssen 8-Bit-Integer sein (0-255)")

    # Kombinieren Sie die beiden 8-Bit-Integer zu einem 16-Bit-Integer
    combined = (byte1 << 8) | byte2
    return combined

# Eingabe von zwei 8-Bit-Integern
byte1 = int(input("Geben Sie den ersten 8-Bit-Integer ein (0-255): "))
byte2 = int(input("Geben Sie den zweiten 8-Bit-Integer ein (0-255): "))

# Kombinieren und ausgeben
combined_integer = combine_to_16bit_integer(byte1, byte2)
print(f"Das kombinierte 16-Bit-Integer ist: {combined_integer}")
