import unittest

from crypto import (atbash_decrypt,
                    atbash_encrypt,
                    ceaser_decrypt,
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

    def test_ceaser_decrypt(self):
    
        input_var=""

        result=ceaser_decrypt(cipher_text=input_var,
                             shift=int)

        expected=""

        self.assertEqual(result,expected)
    
    def test_ceaser_encrypt(self):
        
        input_var=""

        result=ceaser_encrypt(plain_text=input_var,
                             shift=int)

        expected=""

        self.assertEqual(result,expected)

    def test_vigenere_decrypt(self):
        
        input_var=""

        result=vigenere_decrypt(cipher_text=input_var,
                                keyword="",
                                permutation="")

        expected=""

        self.assertEqual(result,expected)

    def test_vigenere_encrypt(self):
        
        input_var=""

        result=vigenere_encrypt(plain_text=input_var,
                                keyword="",
                                permutation="")

        expected=""

        self.assertEqual(result,expected)


    def test_playfair_decrypt(self):
        
        input_var=""

        result=playfair_decrypt(cipher_text=input_var,
                                keyword="")

        expected=""

        self.assertEqual(result,expected)


    def test_playfair_encrypt(self):
        
        input_var=""

        result=playfair_encrypt(plain_text=input_var,
                                keyword="")

        expected=""

        self.assertEqual(result,expected)



if __name__=="__main__":
        unittest.main()


















#print(ceaser_decrypt("EZOLJ", shift=11)) should be equal to today

#get_ceaser_pos_decrypt(letters_pos,shift)
#print(ceaser_encrypt("TODAY", 11))
#x=playfair_decrypt(cipher_text="GIVHYCHGSYPCFHWHGDHPUTSMYTLD",keyword="GLAMORGAN")
#print(x)