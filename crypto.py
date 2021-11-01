from tools import (type_str_error, 
                   type_alphabet_error,
                   get_pos_alphabet,
                   get_atbashed_pos_alphabet,
                   get_alphabet_from_pos)

def atbash_decrypt(cipher_text):
    """Decryps cipher texts into plain tests
       using the atbash ciper

    Args:
        cipher_text ([string]): [string of cipher texts to decrypt]

    Returns:
        [plain_text_joined]: [the decryped cipher text i.e plain text]
    """

    type_str_error(cipher_text)
    type_alphabet_error(cipher_text)
    
    
    letter_pos=get_pos_alphabet(cipher_text)
    atbashed_pos=get_atbashed_pos_alphabet(letter_pos)
    plain_text=get_alphabet_from_pos(atbashed_pos)
    
    plain_text_joined = "".join(plain_text)
    
    
    return plain_text_joined


                


