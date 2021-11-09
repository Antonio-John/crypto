from tools import (type_str_error, 
                   type_alphabet_error,
                   type_int_error,
                   type_duplicate_letter_error,
                   get_pos_alphabet,
                   get_atbashed_pos_alphabet,
                   get_alphabet_from_pos,
                   get_atbashed_pos_alphabet_encrypt,
                   get_ceaser_pos,
                   get_ceaser_pos_decrypt,
                   keyword_text_match_up,
                   create_viginere_table,
                   viginere_get_table_decrypt,
                   viginere_get_table_encrypt,
                   playfair_grid_list,
                   playfair_deal_with_dups,
                   get_play_fair_row_col,
                   put_into_pairs)

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

def vigenere_decrypt(cipher_text, keyword, permutation=""):

    # error catching
    type_str_error(cipher_text)
    type_alphabet_error(cipher_text)
    type_str_error(keyword)
    type_alphabet_error(keyword)
    type_str_error(permutation)
    type_duplicate_letter_error(keyword)
    
    # create table
    table=create_viginere_table(permutation)
    
    # list of keyword next to cipher text
    key,cipher=keyword_text_match_up(text=cipher_text, 
                                     keyword=keyword) 
    
    # decrypt using table, keyword list & cipher
    plain_text=[viginere_get_table_decrypt(table,k,text) for [k,text] in zip(key,cipher)]    
    # joins plain text into a string
    plain_text_joined = "".join(plain_text)
    
    
    return plain_text_joined

def vigenere_encrypt(plain_text, keyword, permutation=""):

    # error catching
    type_str_error(plain_text)
    type_alphabet_error(plain_text)
    type_str_error(keyword)
    type_alphabet_error(keyword)
    type_str_error(permutation)
    type_duplicate_letter_error(keyword)
    
    # create table
    table=create_viginere_table(permutation)
    
    # list of keyword next to plain text
    key,text=keyword_text_match_up(text=plain_text, 
                                     keyword=keyword) 
    
    # decrypt using table, keyword list & cipher
    cipher_text=[viginere_get_table_encrypt(table,k,text) for [k,text] in zip(key,text)]    
    # joins plain text into a string
    plain_text_joined = "".join(cipher_text)
    
    
    return plain_text_joined
    
def playfair_decrypt(cipher_text,keyword):
    
    type_str_error(cipher_text)
    type_alphabet_error(cipher_text)
    type_str_error(keyword)
    type_alphabet_error(keyword)

    grid_list=playfair_grid_list(keyword)
    plain_text_adjusted_dups=playfair_deal_with_dups(cipher_text)

    paired_list=put_into_pairs(plain_text_adjusted_dups)
    
    
    
    
    # then work out which type of playfair they are
    # then do apropriate documentation
    

    # tests for crypto package
    # doc strings for all functions
    # watch python package tutorial



