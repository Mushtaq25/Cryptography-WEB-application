# i have created this file- mushtaq
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np

def home(request):
    return render(request,'home.html')

def caeser_cipher(request):
    plain_text = request.GET.get('text','default')
    key1 = request.GET.get('number1','0')

    print(key1)
    check_encrypt = request.GET.get('encrypt','off')
    check_decrypt = request.GET.get('decrypt','off')

    if check_encrypt=='off' and check_decrypt=='off':
        return render(request,'caeser.html')
    elif check_encrypt=='on' and check_decrypt=='on':
        return render(request,'error.html')

    elif check_encrypt=='on' and check_decrypt=='off':
        cipher_text = obj_caeser.encryption(str(plain_text),key1)
        arg = {'ciphertext' : 'Your cipher text is =' + cipher_text}
        return render(request,'caeser.html',arg)

    elif check_decrypt=='on' and check_encrypt=='off':
        messege = obj_caeser.decryption(str(plain_text),key1)
        arg = {'ciphertext' : 'Your plain text is ==' +' '+ messege}
        return render(request,'caeser.html',arg)
    


def playfair_cipher(request):
    plain_text = request.GET.get('text','default')
    key = request.GET.get('KEY','default')
    check_encrypt = request.GET.get('encrypt','off')
    check_decrypt = request.GET.get('decrypt','off')

    
    #
    obj_playfair.Matrix(str(key))
    if check_encrypt=='off' and check_decrypt=='off':
        return render(request,'playfair.html')
    elif check_encrypt=='on' and check_decrypt=='on':
        return render(request,'error.html')

    elif check_encrypt=='on' and check_decrypt=='off':
        cipher_text = obj_playfair.encrypt(str(plain_text),str(key))
        print(cipher_text)
        arg = {'ciphertext' : 'Your cipher text is =' + ' '+ cipher_text}
        return render(request,'playfair.html',arg)

    elif check_decrypt=='on' and check_encrypt=='off':
        messege = obj_playfair.decrypt(str(plain_text),str(key))
        arg = {'ciphertext' :'Your plain text is ==' +' '+ messege}
        return render(request,'caeser.html',arg)







def des_cipher(request):

    my_obj = DES_CIPHER()

    #pt = "123456ABCD132536"
    #key = "AABB09182736CCDD"

    plain_text = request.GET.get('text','default')
    key = request.GET.get('KEY','AABB09182736CCDD')
    check_encrypt = request.GET.get('encrypt','off')
    check_decrypt = request.GET.get('decrypt','off')

    key = my_obj.hex2bin(key)

    keyp = [57, 49, 41, 33, 25, 17, 9, 
            1, 58, 50, 42, 34, 26, 18, 
            10, 2, 59, 51, 43, 35, 27, 
            19, 11, 3, 60, 52, 44, 36, 
            63, 55, 47, 39, 31, 23, 15, 
            7, 62, 54, 46, 38, 30, 22, 
            14, 6, 61, 53, 45, 37, 29, 
            21, 13, 5, 28, 20, 12, 4 ] 

    
    key = my_obj.permute(key, keyp, 56) 

    shift_table = [1, 1, 2, 2, 
                    2, 2, 2, 2, 
                    1, 2, 2, 2, 
                    2, 2, 2, 1 ] 

    key_comp = [14, 17, 11, 24, 1, 5, 
                3, 28, 15, 6, 21, 10, 
                23, 19, 12, 4, 26, 8, 
                16, 7, 27, 20, 13, 2, 
                41, 52, 31, 37, 47, 55, 
                30, 40, 51, 45, 33, 48, 
                44, 49, 39, 56, 34, 53, 
                46, 42, 50, 36, 29, 32 ] 

    
    left = key[0:28] 
    right = key[28:56]  

    rkb = [] 
    rk = [] 
    for i in range(0, 16): 
        
        left = my_obj.shift_left(left, shift_table[i]) 
        right = my_obj.shift_left(right, shift_table[i]) 
        
        combine_str = left + right 
        
        round_key = my_obj.permute(combine_str, key_comp, 48) 

        rkb.append(round_key) 
        rk.append(my_obj.bin2hex(round_key)) 

    if check_encrypt=='off' and check_decrypt=='off':
        return render(request,'des.html')
    elif check_encrypt=='on' and check_decrypt=='on':
        return render(request,'error.html')

    elif check_encrypt=='on' and check_decrypt=='off':
        cipher_text = my_obj.bin2hex(my_obj.encrypt(plain_text, rkb, rk)) 
        print("Cipher Text : ",cipher_text) 
        arg = {'ciphertext' : 'Your cipher text is =' + ' '+ cipher_text}
        return render(request,'des.html',arg)

    elif check_decrypt=='on' and check_encrypt=='off':
        print("Decryption") 
        rkb_rev = rkb[::-1] 
        rk_rev = rk[::-1] 
        text = my_obj.bin2hex(my_obj.encrypt(plain_text, rkb_rev, rk_rev)) 
        print("Plain Text : ",text) 
        arg = {'ciphertext' :'Your plain text is ==' +' '+ text}
        return render(request,'caeser.html',arg)

'''-------------------------------------------------------------------------------CAESER-CIPHER--------------------------------------------------         '''
    
class Caeser_cipher():
    def encryption(self,plain_text,key):
        self.plain_text = plain_text
        self.key = int(key)
        plain_text.lower()
        cipher_text = ''
        sentence = list(plain_text)
        join_sentence = ''

        for j in sentence:
            
            if j == ' ':
                join_sentence += '$' 
            else:
                join_sentence += str(j)

        letters = list("abcdefghijklmnopqrstuvwxyz")
            
        for i in join_sentence:
           
            if i == '$':
                cipher_text += '$'
            else:
                if letters.index(i) + int(key) > 25:
                    x = 25 - letters.index(i)
                    y = int(key) - int(x) -1
                    cipher_text += letters[int(y)]
                else: 
                    cipher_text = cipher_text + letters[letters.index(i) + int(key)]
        return cipher_text
        
    def decryption(self,cipher_text,key):
        self.cipher_text = cipher_text
        self.key = key
        plain_text = ''
        sentence = list(cipher_text)
        join_sentence = ''
        
        for j in sentence:
            if j == '$':
                join_sentence += ' ' 
            else:
                join_sentence += str(j)

        letters = list("abcdefghijklmnopqrstuvwxyz")

        for i in join_sentence:
            #print(i)
            if i == ' ':
                plain_text += ' '
            else:
                if letters.index(i) - int(key) < 0:
                    y = int(key) - letters.index(i) -1
                    plain_text += letters[25 - int(y)]
                else: 
                    plain_text += letters[letters.index(i) - int(key)]
    
        return plain_text

obj_caeser = Caeser_cipher()

'''----------------------------------------------------------------------------------CAESER-CIPHER--------------------------------------------------------------'''


'''----------------------------------------------------------------------------------PLAYFAIR-CIPHER--------------------------------------------------------------'''
class Playfair_cipher_Encryption(object):

    def Matrix(self,key):
    
        self.key = key
        
        join_letter = ''
        new_join_letter = ''
        x = 0
        count = 0

        for i in key.upper():
            if (i != " "):
                join_letter += str(i)
        
        alphabets = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        for e in join_letter:
            if e not in new_join_letter:
                new_join_letter += str(e)
        j = 1
        

        while len(new_join_letter) < 25:
            for i in new_join_letter:
                
                if (i == alphabets[x]):
                    count += 1       
            if count == 0:
                new_join_letter += alphabets[x]
            x += 1
            count = 0

        my_list = list(new_join_letter)
        matrix = np.array(my_list).reshape(5,5)
        return matrix


    def messege_to_diagraphs(self,plain_text):
        self.plain_text = plain_text
        join_list = []
    
        for i in plain_text.upper():
            if (i != " "):
                join_list += str(i)
        j =0
        a = int(len(join_list))
        if a % 2 == 0:
            for i in range(int(a/2)):
                if join_list[j] == join_list[j+1]:
                    join_list.insert(j+1,"X")
                    
                j += 2

        else:
            b = int((a + 1)/2)
            for i in range(b):
                if j != a-1:

                    if join_list[j] == join_list[j+1]:
                        join_list.insert(j+1,"Z")
                    j += 2
                else:
                    join_list += str("Z")
        
        length_of_plaintext = len(join_list)
        if length_of_plaintext % 2 != 0:
            join_list += str("Z")
        new = []
        j = 0
        for i in range(int(len(join_list)/2)):
            new.append(join_list[j:j+2])
            j += 2
        return new

        
    def find_position(self,key_matrix,letter):
        self.key_matrix = key_matrix
        self.letter = letter
        x=y=0
        for i in range(5):
            for j in range(5):
                if key_matrix[i][j] == letter:
                    x = i
                    y = j
        return x,y

    def encrypt(self,messege,key):
        self.messege = messege
        self.key = key
        messege = self.messege_to_diagraphs(messege)
        key_matrix = self.Matrix(key)
        join_cipher = ''

        cipher=[]
        for e in messege:
            p1,q1=self.find_position(key_matrix,e[0])
            p2,q2=self.find_position(key_matrix,e[1])
            if p1==p2:
                if q1==4:
                    q1=-1
                if q2==4:
                    q2=-1
                cipher.append(key_matrix[p1][q1+1])
                cipher.append(key_matrix[p1][q2+1])	
            elif q1==q2:
                if p1==4:
                    p1=-1
                if p2==4:
                    p2=-1
                cipher.append(key_matrix[p1+1][q1])
                cipher.append(key_matrix[p2+1][q2])
            else:
                cipher.append(key_matrix[p1][q2])
                cipher.append(key_matrix[p2][q1])
        for i in cipher:
            join_cipher += i
        return join_cipher
        

    def cipher_to_digraphs(self,cipher):
        self.cipher = cipher
        i=0
        new=[]
        for x in range(int(len(cipher)/2)):
            new.append(cipher[i:i+2])
            i=i+2
        return new

    def decrypt(self,cipher,key):
        self.cipher = cipher
        self.key = key
        cipher = self.cipher_to_digraphs(cipher)
        key_matrix = self.Matrix(key)
        plaintext=[]
        for e in cipher:
            p1,q1=self.find_position(key_matrix,e[0])
            p2,q2=self.find_position(key_matrix,e[1])
            if p1==p2:
                if q1==4:
                    q1=-1
                if q2==4:
                    q2=-1
                plaintext.append(key_matrix[p1][q1-1])
                plaintext.append(key_matrix[p1][q2-1])
            elif q1==q2:
                if p1==4:
                    p1=-1;
                if p2==4:
                    p2=-1;
                plaintext.append(key_matrix[p1-1][q1])
                plaintext.append(key_matrix[p2-1][q2])
            else:
                plaintext.append(key_matrix[p1][q2])
                plaintext.append(key_matrix[p2][q1])

        for unused in range(len(plaintext)):
            if "Z" in plaintext:
                plaintext.remove("Z")
        output=""
        for e in plaintext:
            output+=e
        return output.lower()

obj_playfair = Playfair_cipher_Encryption()

'''----------------------------------------------------------------------------------PLAYFAIR-CIPHER--------------------------------------------------------------'''


'''----------------------------------------------------------------------------------DES-CIPHER-----------------------------------------------------------------------'''

class DES_CIPHER():

    def hex2bin(self,s): 
        self.s = s
        mp = {'0' : "0000", 
            '1' : "0001", 
            '2' : "0010", 
            '3' : "0011", 
            '4' : "0100", 
            '5' : "0101", 
            '6' : "0110", 
            '7' : "0111", 
            '8' : "1000", 
            '9' : "1001", 
            'A' : "1010", 
            'B' : "1011", 
            'C' : "1100", 
            'D' : "1101", 
            'E' : "1110", 
            'F' : "1111" } 
        bin = "" 
        for i in range(len(s)): 
            bin = bin + mp[s[i]] 
        return bin
        
    def bin2hex(self,s): 
        self.s = s
        mp = {"0000" : '0', 
            "0001" : '1', 
            "0010" : '2', 
            "0011" : '3', 
            "0100" : '4', 
            "0101" : '5', 
            "0110" : '6', 
            "0111" : '7', 
            "1000" : '8', 
            "1001" : '9', 
            "1010" : 'A', 
            "1011" : 'B', 
            "1100" : 'C', 
            "1101" : 'D', 
            "1110" : 'E', 
            "1111" : 'F' } 
        hex = "" 
        for i in range(0,len(s),4): 
            ch = "" 
            ch = ch + s[i] 
            ch = ch + s[i + 1] 
            ch = ch + s[i + 2] 
            ch = ch + s[i + 3] 
            hex = hex + mp[ch] 
            
        return hex

    # Binary to decimal conversion 
    def bin2dec(self,binary): 

        self.binary = binary    
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal 

    # Decimal to binary conversion 
    def dec2bin(self,num):
        self.num = num 
        res = bin(num).replace("0b", "") 
        if(len(res)%4 != 0): 
            div = len(res) / 4
            div = int(div) 
            counter =(4 * (div + 1)) - len(res) 
            for i in range(0, counter): 
                res = '0' + res 
        return res 

    # Permute function to rearrange the bits 
    def permute(self,k, arr, n): 
        self.k = k
        self.arr = arr
        self.n = n
        permutation = "" 
        for i in range(0, n): 
            permutation = permutation + k[arr[i] - 1] 
        return permutation 

    # shifting the bits towards left by nth shifts 
    def shift_left(self,k, nth_shifts): 
        self.k = k
        self.nth_shifts =nth_shifts
        s = "" 
        for i in range(nth_shifts): 
            for j in range(1,len(k)): 
                s = s + k[j] 
            s = s + k[0] 
            k = s 
            s = "" 
        return k	 

    # calculating xow of two strings of binary number a and b 
    def xor(self,a, b):
        self.a = a
        self.b = b 
        ans = "" 
        for i in range(len(a)): 
            if a[i] == b[i]: 
                ans = ans + "0"
            else: 
                ans = ans + "1"
        return ans 

    # Table of Position of 64 bits at initail level: Initial Permutation Table 
    initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 
                    60, 52, 44, 36, 28, 20, 12, 4, 
                    62, 54, 46, 38, 30, 22, 14, 6, 
                    64, 56, 48, 40, 32, 24, 16, 8, 
                    57, 49, 41, 33, 25, 17, 9, 1, 
                    59, 51, 43, 35, 27, 19, 11, 3, 
                    61, 53, 45, 37, 29, 21, 13, 5, 
                    63, 55, 47, 39, 31, 23, 15, 7] 

    # Expansion D-box Table 
    exp_d = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5, 
            6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 
            12, 13, 12, 13, 14, 15, 16, 17, 
            16, 17, 18, 19, 20, 21, 20, 21, 
            22, 23, 24, 25, 24, 25, 26, 27, 
            28, 29, 28, 29, 30, 31, 32, 1 ] 

    # Straight Permutaion Table 
    per = [ 16, 7, 20, 21, 
            29, 12, 28, 17, 
            1, 15, 23, 26, 
            5, 18, 31, 10, 
            2, 8, 24, 14, 
            32, 27, 3, 9, 
            19, 13, 30, 6, 
            22, 11, 4, 25 ] 

    # S-box Table 
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
            [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
            [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]], 
                
            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], 
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]], 
        
            [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]], 
            
            [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ], 
            
            [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]], 
            
            [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ], 
            
            [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ], 
            
            [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ] 
        
    # Final Permutaion Table 
    final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
                39, 7, 47, 15, 55, 23, 63, 31, 
                38, 6, 46, 14, 54, 22, 62, 30, 
                37, 5, 45, 13, 53, 21, 61, 29, 
                36, 4, 44, 12, 52, 20, 60, 28, 
                35, 3, 43, 11, 51, 19, 59, 27, 
                34, 2, 42, 10, 50, 18, 58, 26, 
                33, 1, 41, 9, 49, 17, 57, 25 ] 

    def encrypt(self,pt, rkb, rk):
        self.pt = pt
        self.rkb = rkb
        self.rk = rk 
        pt = self.hex2bin(pt) 
        
        # Initial Permutation 
        pt = self.permute(pt, self.initial_perm, 64) 
        print("After inital permutation", self.bin2hex(pt)) 
        
        # Splitting 
        left = pt[0:32] 
        right = pt[32:64] 
        for i in range(0, 16): 
            # Expansion D-box: Expanding the 32 bits data into 48 bits 
            right_expanded = self.permute(right, self.exp_d, 48) 
            
            # XOR RoundKey[i] and right_expanded 
            xor_x = self.xor(right_expanded, rkb[i]) 

            # S-boxex: substituting the value from s-box table by calculating row and column 
            sbox_str = "" 
            for j in range(0, 8): 
                row = self.bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5])) 
                col = self.bin2dec(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4])) 
                val = self.sbox[j][row][col] 
                sbox_str = sbox_str + self.dec2bin(val) 
                
            # Straight D-box: After substituting rearranging the bits 
            sbox_str = self.permute(sbox_str, self.per, 32) 
            
            # XOR left and sbox_str 
            result = self.xor(left, sbox_str) 
            left = result 
            
            # Swapper 
            if(i != 15): 
                left, right = right, left 
            print("Round ", i + 1, " ", self.bin2hex(left), " ", self.bin2hex(right), " ", rk[i]) 
        
        # Combination 
        combine = left + right 
        
        # Final permutaion: final rearranging of bits to get cipher text 
        cipher_text = self.permute(combine, self.final_perm, 64) 
        return cipher_text 
'''----------------------------------------------------------------------------------DES-CIPHER-----------------------------------------------------------------------'''