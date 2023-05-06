"""
Gerador de senhas

"""
import random
import string

def password_generator(len_pass = 10):
    ascii_options = string.ascii_letters
    number_options  = string.digits
    punt_options = string.punctuation
    options = ascii_options +  number_options + punt_options

    for digig in range(0, len_pass):
        []