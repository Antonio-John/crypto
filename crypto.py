from tools import (type_str_error, 
                   type_alphabet_error,
                   type_int_error,
                   get_pos_alphabet,
                   get_atbashed_pos_alphabet,
                   get_alphabet_from_pos,
                   get_atbashed_pos_alphabet_encrypt,
                   get_ceaser_pos,
                   get_ceaser_pos_decrypt)

def atbash_decrypt(cipher_text):
    """Decryps cipher texts into plain tests
       using the atbash ciper

    Args:
        cipher_text ([string]): [string of cipher texts to decrypt]

    Returns:
        [plain_text_joined]: [the decryped cipher text i.e plain text]
    """
    # error catching
    type_str_error(cipher_text)
    type_alphabet_error(cipher_text)
    
    # transformation letters to atbashed equivalent
    letter_pos=get_pos_alphabet(cipher_text)
    atbashed_pos=get_atbashed_pos_alphabet(letter_pos)
    plain_text=get_alphabet_from_pos(atbashed_pos)
    
    # joins plain text into a string
    plain_text_joined = "".join(plain_text)
    
    
    return plain_text_joined

def atbash_encrypt(plain_text):
    """ENcrypts plain text into cipher text
       using the atbash ciper

    Args:
        cipher_text ([string]): [string of cipher texts to decrypt]

    Returns:
        [plain_text_joined]: [the decryped cipher text i.e plain text]
    """
    # error catching
    type_str_error(plain_text)
    type_alphabet_error(plain_text)
    
    # transformation letters to atbashed equivalent
    letter_pos=get_pos_alphabet(plain_text)
    atbashed_pos=get_atbashed_pos_alphabet_encrypt(letter_pos)
    plain_text=get_alphabet_from_pos(atbashed_pos)
    
    # joins plain text into a string
    plain_text_joined = "".join(plain_text)
    
    
    return plain_text_joined


def ceaser_decrpyt(cipher_text, shift):

    # error catching
    type_str_error(cipher_text)
    type_alphabet_error(cipher_text)
    type_int_error(shift)

    letter_pos=get_pos_alphabet(cipher_text)
    ceaser_pos=get_ceaser_pos(letters_pos=letter_pos,
                              shift=shift)

    plain_text=get_alphabet_from_pos(ceaser_pos)
    
    # joins plain text into a string
    plain_text_joined = "".join(plain_text)
    
    
    return plain_text_joined


def ceaser_encrypt(plain_text, shift):

    # error catching
    type_str_error(plain_text)
    type_alphabet_error(plain_text)
    type_int_error(shift)

    letter_pos=get_pos_alphabet(plain_text)
    ceaser_pos=get_ceaser_pos_decrypt(letters_pos=letter_pos,
                                      shift=shift)

    plain_text=get_alphabet_from_pos(ceaser_pos)
    
    # joins plain text into a string
    plain_text_joined = "".join(plain_text)
    
    
    return plain_text_joined




