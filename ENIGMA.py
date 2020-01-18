infor='''FYI, ENIGMA only support capitalized letters without any blanks.
            PLEASE CAPSLOCK
            The rotorsetting must be three capitalized letters, one for each rotor.'''
print(infor)
wish=True
error=0
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
        con=0
        for(i,v)in enumerate(n):
            if string==v:
                out=i
                con=1
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
        rotor0=['Q', 'A', 'Z', 'X', 'S', 'W', 'E', 'D', 'C', 'V','F', 'R',
                'T', 'G', 'B', 'N', 'H', 'Y', 'U', 'J', 'M', 'K', 'I', 'O', 'L', 'P']
        rotor1=['V', 'D', 'F', 'L', 'X', 'Q', 'O', 'M', 'I', 'C', 'J', 'R',
                'G', 'H', 'N', 'E', 'T', 'A', 'U', 'W', 'S', 'Z', 'B', 'P', 'Y', 'K']
        rotor2=['O', 'F', 'J', 'P', 'R', 'X', 'A', 'I', 'N', 'D', 'H', 'M',
                'S', 'Y', 'W', 'T', 'E', 'B', 'L', 'C', 'U', 'Q', 'G', 'V', 'K', 'Z']
        rotor3=['L', 'G', 'D', 'C', 'Z', 'S', 'J', 'E', 'I', 'Y', 'P', 'N',
                'U', 'H', 'O', 'Q', 'W', 'R', 'T', 'X', 'B', 'V', 'K', 'A', 'M', 'F']
        con1=0
        con2=0
        con3=0
            #输入转子初始参数
        rotor_setting=[]
        while not rotor_setting:
            rotor_setting=list(input('Please input rotor settings：'))
            if len(rotor_setting)==3:
                rs=list(rotor_setting)
                for x in rs:
                    try:
                        ooo=change(0,x)
                    except Exception:
                        print('input error!!')
                        rotor_setting=[]
                        break
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
        if target=='ENCRYPT' or target=='EN':
            ciphertext_out=[]
            plaintext_in=[]
            while not plaintext_in :
                plaintext_in=list(input('plaintext：'))
                pti=list(plaintext_in)
                for x in pti:
                    try:
                        ooo=change(0,x)
                    except Exception:
                        print('input error!!')
                        rotor_setting=[]
                        error=1
                        break
            if error==1:
                continue
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
                        if con1%26==0:
                            a=rotate(a)
                            con2+=1
                    else:
                        if con2%26==0 and con2>0:
                            a=rotate(a)
                            con3+=1
                ciphertext_out.append(x)
            cto=str_list(ciphertext_out)
            print('ciphertext：',cto)
            #是否重设转子
            while True:
                wish=input('Do you wish to set the rotors again?(YES/NO)')
                if wish=='YES':
                    wish=True
                    break
                elif wish=='NO':
                    wish=False
                    break
                else:
                    print('input error!')
            break
        #输入密文
        elif target=='DECRYPT' or target=='DE':
            ciphertext_in=[]
            plaintext_out=[]
            while not ciphertext_in :
                ciphertext_in=list(input('ciphertext：'))
                cti=list(ciphertext_in)
                for x in cti:
                    try:
                        ooo=change(0,x)
                    except Exception:
                        print('input error!!')
                        rotor_setting=[]
                        error=1
                        break
            if error==1:
                continue
            for x in cti:
                for i in range(3):
                    n=3-i
                    #转子3&2&1
                    x=change(n,x)
                    x=rotor(x,0)
                rotor1=rotate(rotor1)
                con1+=1
                if con1%26==0:
                    rotor2=rotate(rotor2)
                    con2+=1
                    if con2%26==0:
                        rotor3=rotate(rotor3)
                plaintext_out.append(x)
            pto=str_list(plaintext_out)
            print('plaintext：',pto)
            while True:
                wish=input('Do you wish to set the rotors again?(YES/NO)')
                if wish=='YES':
                    wish=True
                    break
                elif wish=='NO':
                    wish=False
                    break
                else:
                    print('input error!')
            break
        else:
            print('input error')
