
# I will give you an integer (N) and a string. Break the string up into as many substrings of N as you can without spaces. If there are leftover characters, include those as well.
# 
# Example: 
# 
# n = 5;
# 
# st = "This is an example string";
# 
# Return value:
# Thisi
# sanex
# ample
# strin
# g
# 
# Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'

def string_breakers(n, st): 
    # your code here
    finalstring= st.replace(" ", "")
    l =len(st)
    i =0 
    a= ""
    while i<=l:
        a += finalstring[i:i+n] + "\n"
        i += n
    return a.rstrip("\n")
        

    # solution 2
    
    def string_breakers(n, st):
    s = st.replace(' ', '')
    return '\n'.join(s[i:i+n] for i in range(0, len(s), n))
