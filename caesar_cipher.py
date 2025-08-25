def caesar_cipher(text: str, shift: int, mode: str = "encode") -> str:
    """
    Applies the Caesar Cipher to encode or decode a message.

    Args:
        text (str): The text to encode/decode.
        shift (int): The shift amount.
        mode (str): Either 'encode' or 'decode'.

    Returns:
        str: The transformed message.
    """

    result = []
    
    if mode == "decode":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base # '% 26' takes us back to 'A' (prevents going out of range)
            result.append(chr(shifted))
        else:
            result.append(char)  # Keep punctuation, spaces, numbers unchanged

    return ''.join(result)
