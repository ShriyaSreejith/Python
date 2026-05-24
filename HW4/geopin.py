# Shriya Sreejith
# HW4 - Geopin

"""Module for Geopin functions"""
"""Finding the check digit"""
def FindCheckDigit():
    global number
    global checkDigit

    number = []
    zipCode = input("\nEnter a valid zip code: ")
    if zipCode.isdigit() == False or len(zipCode) != 5:
        print("\nInvalid zip code. Please enter a 5 digit valid zip code.")
        return FindCheckDigit()
    for num in zipCode:
        number.append(int(num))

    total = 0
    for i in number:
        total += i
    checkDigit = (10 - (total % 10)) % 10
    print("\nThe check digit is: " + str(checkDigit))

"""Barcode for each digit"""
barcodeDict = {
    0: "||:::",
    1: ":::||",
    2: "::|:|",
    3: "::||:",
    4: ":|::|",
    5: ":|:|:",
    6: ":||::",
    7: "|:::|",
    8: "|::|:",
    9: "|:|::"
}

"""Generating the barcode"""
def barcode():
    barcode_string = "|"
    for i in number:
        barcode_string += barcodeDict[i]
    barcode_string += barcodeDict[checkDigit]
    barcode_string += "|"

    print("\nThe barcode is:", barcode_string,"\n")