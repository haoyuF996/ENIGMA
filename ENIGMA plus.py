wish=True
while True:
    def rotate(list_):
        a=list_[0]
        listout=list_
        del listout[0]
        listout.append(a)
        return listout
    def derotate(list_):
        a=list_
        listout=[]
        del a[-1]
        listout.append(list_[-1])
        listout.append(a)
        return listout    
    def change(rotor_n,string):
        n=eval('rotor{}'.format(rotor_n))
        for(i,v)in enumerate(n):
            if string==v:
                out=i
                break
        return out
    def rotor(num,rotor_n):
        out=eval('rotor{}'.format(rotor_n))[num]
        return out
    def str_list(list_):
        out=''
        for i in list_:
            out+=str(i)
        return out
    if wish:
        #转子初始化
        rotor0=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
                 's', 'd', 'f', 'g', 'h', 'j', 'k', 'z', 'x', 'c', 'v',
                 'b', 'n', 'm', 'P', 'L', 'M', 'O', 'K', 'I', 'J', 'N',
                 'U', 'H', 'B', 'Y', 'G', 'V', 'T', 'F', 'C', 'R', 'D',
                 'X', 'E', 'S', 'Z', 'W', ')', '(', '*', '&', '^', '%',
                 '$', '#', '@', '!', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9', '0', ']', '[', '}', '{', '`', '~', '=', '+', '-',
                 '_', '<', '>', '/', '?', ';', ':', ' ', '"', '|', "'", ',',
                 '.', 'Q', 'A', '\\', '♂']
        rotor1=[' ', 'q', 'L', '!', 'b', '#', '&', 'f', ')', '"', 'K',
                  't', '-', 'E', 'i', '+', 'Y', 'X', '>', '@', 's', 'd', '2',
                  '=', 'h', '{', '<', '~', 'M', 'v', 'o', 'a', 'A', 'R',
                  'H', '7', 'F', "'", 'c', 'k', 'U', 'z', '0', '\\', ';',
                  'p', 'Q', '6', 'C', 'u', 'w', '1', '$', 'B', '.', '8',
                  'm', ',', ']', 'S', '3', '4', '?', '}', '*', 'n', '|', '/',
                  'V', 'j', '^', '_', 'P', 'g', '[', 'G', 'N', ':', 'r', '5',
                  'O', 'l', 'W', '(', '♂', 'T', '9', 'y', '`', 'x', 'e', '%',
                  'J', 'Z', 'D']
        rotor2=['w', 'H', '>', '%', '[', '?', 'N', '&', 's', ' ', 'l',
                  'D', '|', 'j', '4', '#', '+', 'p', 'W', 'U', 'A', '2', 'h',
                  '(', '0', ';', 'e', '{', 'M', 'i', 'o', 'T', ')', '`', 'X', 'z',
                  'P', '=', '@', '/', 't', 'Z', 'r', 'y', 'J', '*', '$', ']',
                  'O', 'K', '7', 'd', '~', '3', 'c', 'V', 'S', '^', 'R', '\\',
                  'f', 'n', 'k', ':', '1', '5', '}', 'Y', 'u', '!', 'F', 'q', '9',
                  'b', '.', "'", '6', ',', 'x', '<', 'L', '♂', 'Q', '8', 'B', 'C',
                  '"', 'm', 'G', '-', 'E', 'a', '_', 'g', 'v']
        rotor3=['O', '#', ':', 'M', 'q', ',', ')', '&', 'u', 'Q', 'd', '!',
                  '♂', 'i', "'", 'Z', 'o', '$', '8', 'L', 'a', '}', '*', '>', 'p',
                  'x', '?', '~', 'F', 'e', 'v', 'H', 'b', 'V', 'D', ']', 'j', '4',
                  'R', '`', '1', 'W', '+', 'X', 'I', 'E', 'h', 'y', 'n', '.', 'A',
                  ';', 'G', '@', 's', 'C', '{', 'f', '3', '<', 'S', '/', 'K',
                  '6', 'Y', '0', 'P', '=', '9', 'r', 'g', 'w', 'U', 'c', '^', '"',
                  'T', 'z', '2', '-', '[', 'k', ' ', '\\', '|', '%', '(', 'J', '7',
                  '5', '_', 'N', 'B', 'm', 't']
        con1=0
        con2=0
        con3=0
            #输入转子初始参数
        rotor_setting=[]
        while not rotor_setting:
            rotor_setting=list(input('Please input rotor settings(three characters)：'))
            if len(rotor_setting)==3:
                rs=list(rotor_setting)
            else:
                print('input error!!!')
                rotor_setting=[]
            #转子初始设定
        for i in range(1,4):
            x=rs[i-1]
            x=change(i,x)
            conn=0
            a=eval('rotor{}'.format(i))
            for b in range(x):
                a=rotate(a)
                conn+=1
    while True:
        target=input('You wish to encrypt or decrypt?')
        #输入明文#
        if target=='encrypt' or target=='en':
            plaintext_in=input('plaintext:')
            ciphertext_out=[]
            pti=list(plaintext_in)
        #加密
            for x in pti:
                for i in range(1,4):           
                    #转子1&2&3
                    x=change(0,x)
                    x=rotor(x,i)
                    a=eval('rotor{}'.format(i))
                    if i==1:
                        a=rotate(a)
                        con1+=1
                    elif i==2:
                        if con1%96==0:
                            a=rotate(a)
                            con2+=1
                    else:
                        if con2%96==0 and con2>0:
                            a=rotate(a)
                            con3+=1
                ciphertext_out.append(x)
            cto=str_list(ciphertext_out)
            print('ciphertext：',cto)
            #是否重设转子
            while True:
                wish=input('Do you wish to set the rotors again?(yes/no)')
                if wish=='yes':
                    wish=True
                    break
                elif wish=='no':
                    wish=False
                    break
                else:
                    print('input error!')
            break
        #输入密文
        elif target=='decrypt' or target=='de':
            ciphertext_in=input('ciphertext:')
            cti=list(ciphertext_in)
            plaintext_out=[]
            for x in cti:
                for i in range(3):
                    n=3-i
                    #转子3&2&1
                    x=change(n,x)
                    x=rotor(x,0)
                rotor1=rotate(rotor1)
                con1+=1
                if con1%96==0:
                    rotor2=rotate(rotor2)
                    con2+=1
                    if con2%96==0:
                        rotor3=rotate(rotor3)
                plaintext_out.append(x)
            pto=str_list(plaintext_out)
            print('plaintext：',pto)
            while True:
                wish=input('Do you wish to set the rotors again?(yes/no)')
                if wish=='yes':
                    wish=True
                    break
                elif wish=='no':
                    wish=False
                    break
                else:
                    print('input error!')
            break
        else:
            print('input error')
