import unittest

from crypto import (atbash_decrypt,
                    atbash_encrypt,
                    ceaser_decrpyt,
                    ceaser_encrypt,
                    vigenere_decrypt,
                    vigenere_encrypt,
                    playfair_decrypt,
                    playfair_encrypt)


class test_crypto(unittest.TestCase):

    def test_atbash_decrypt(self):

        input_var=""

        result=atbash_decrypt(cipher_text=input_var)

        expected=""

        self.assertEqual(result,expected)

    def test_atbash_encrypt(self):
    
        input_var=""

        result=atbash_encrypt(plain_text=input_var)

        expected=""

        self.assertEqual(result,expected)

    def test_ceaser_decrpyt(self):
    
        input_var=""

        result=ceaser_decrpyt(cipher_text=input_var,
                             shift=int)

        expected=""

        self.assertEqual(result,expected)

    


if __name__=="__main__":
        unittest.main()


















#print(ceaser_decrpyt("EZOLJ", shift=11)) should be equal to today

#get_ceaser_pos_decrypt(letters_pos,shift)
#print(ceaser_encrypt("TODAY", 11))
#x=playfair_decrypt(cipher_text="GIVHYCHGSYPCFHWHGDHPUTSMYTLD",keyword="GLAMORGAN")
#print(x)