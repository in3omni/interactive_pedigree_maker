from io import valid_seek_flags
from unittest import case

import sympy as sp
import tkinter as tk

'''Input Validation Functions'''
# dominant & recessive check
def check_dr():
    dr = input("Is the gene dominant or recessive?\nAccepts cases:[Dominant, Recessive, D, R]\n").lower()
    valid_dr = ['dominant', 'recessive', 'd', 'r', 'dom', 'rec']
    while dr not in valid_dr:
        dr = input("Is the gene dominant or recessive?\nAccepts cases:[Dominant, Recessive, D, R]\n").lower()
        if dr not in valid_dr:
            print("Invalid response, try again.")
            dr = ''

# sex linked or autosomal check
def check_sl():
    sl = input("Is the gene sex-linked or autosomal (not sex-linked)?\nAccepts cases:[Sex-Linked, Autosomal, S, A]\n").lower()
    valid_sl = ['sex-linked', 'autosomal','s','a','sex','auto']
    while sl not in valid_sl:
        sl = input("Is the gene sex-linked or autosomal (not sex-linked)?\nAccepts cases:[Sex-Linked, Autosomal, S, A]\n").lower()
        if sl not in valid_sl:
            print("Invalid response, try again.")
            sl = ''

def assign_genotype():
    #d_or_r = input("Is the gene dominant or recessive?\nAccepts cases:[Dominant, Recessive, D, R]\n").lower()
    check_dr()
    st_geno = input("Please enter your desired genotype:\nAccepts cases:[RR, Rr, rr]")
    valid_response = ['RR','Rr','rr']
    while st_geno not in valid_response:
        if len(st_geno) != 2:
            print("Response must be 2 characters long, try again.")
        st_geno = input("Please enter your desired genotype:\nAccepts cases:[RR, Rr, rr]")
        if st_geno not in valid_response:
            print("Invalid response, try again.")
            st_geno = ''

    if (case == 'RR'): #dominant genotype

    elif (case == 'Rr'): #recessive genotype

    elif (case == 'rr'): #heterozygus genotype; results in dominant phenotype (mostly)

    else:
        print("Invalid response, try again.")

#For Sex-Linked genes
def fem(): #Female genotype
    fem_g = "XX"
def mal(): #Male genotype
    mal_g = "XY"
#Make sure that a parent pair MUST be male and female only.

# genotype
#Make sure we prompt for a genotype for both parents. P1 and P2
sex_or_auto = input("Is the gene sex-linked or autosomal (not sex-linked)?\nAccepts cases:[Sex-Linked, Autosomal, S, A]\n").lower() #accept sex-linked, sex linked, sex, autosomal, auto, s, a
check_sl()


d_or_r = input("Is the gene dominant or recessive?\nAccepts cases:[Dominant, Recessive, D, R]\n").lower() #accept dominant, recessive, d, r, dom, rec
check_dr()



# mathematical function things :3
##################################
'''math function code goes here'''
##################################

# oh my god i hate implementing ui
##################################
'''ui code goes here'''
#################################