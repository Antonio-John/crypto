import unittest

from tools import (type_str_error,
                   type_alphabet_error,
                   type_int_error,
                   get_pos_alphabet,
                   get_atbashed_pos_alphabet,
                   get_alphabet_from_pos,
                   get_ceaser_pos,
                   get_ceaser_pos_decrypt)

class test_tools(unittest.TestCase):

    def test_type_str_error(self):
        
        self.assertRaises(TypeError, type_str_error, 2)
        self.assertRaises(TypeError, type_str_error, ["A"])
        self.assertRaises(TypeError, type_str_error, ("A", "B", "C"))
        
    def test_type_alphabet_error(self):
        
        self.assertRaises(TypeError, type_alphabet_error, "3")
        self.assertRaises(TypeError, type_alphabet_error, ["!?@"])
        
    def test_get_pos_alphabet(self):
        
        sample=["A","V", "F"]
        
        expected=[0, 21, 5]
        
        result=get_pos_alphabet(["A","v", "F"])
        
        self.assertListEqual(expected, result)
        
    def test_get_atbash_decrypt_pos_alphabet(self):
        
        sample=[0, 21, 5]
        
        expected=[25,4,20]
        
        result=get_atbashed_pos_alphabet(sample)
        
        self.assertListEqual(expected, result)
    
    def test_get_alphabet_from_pos(self):
        
        sample=[25,4,20]
        
        expected=["Z", "E", "U"]
        
        result=get_alphabet_from_pos(sample)
        
        self.assertListEqual(expected, result)

    def test_type_int_error(self):

        self.assertRaises(TypeError, type_int_error, "2")
        self.assertRaises(TypeError, type_int_error, ["A"])
        self.assertRaises(TypeError, type_int_error, ("A", "B", "C"))

    def test_get_ceaser_pos(self):

        sample=[4,25,14,11,9]
    

        result=get_ceaser_pos(letters_pos=sample,
                        shift=11)

        expected=[19,14,3,0,24]

        self.assertListEqual(result, expected)

    def test_get_ceaser_pos_decrypt(self):

        
        sample=[19,14,3,0,24]
    

        result=get_ceaser_pos_decrypt(letters_pos=sample,
                        shift=11)

       
        expected=[4,25,14,11,9]

        self.assertListEqual(result, expected)


        

        
        
        
if __name__=="__main__":
    unittest.main()


        
        
    