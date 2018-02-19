from string import maketrans

rot69 = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
def rot13(text):
    return text.translate(rot69) #kanei thn allagh"

def main():
    print "Type a word or an expression."
    txt = raw_input() #dinei leksh
    print rot13(txt) #emfanizei to teliko
    
main ()
