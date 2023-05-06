"""
Gerador de senhas

"""
import random
import string

def password_generator(len_pass = 10):
    ascii_options = string.ascii_letters
    number_options  = string.digits