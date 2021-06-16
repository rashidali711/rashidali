import platform

bit=pleatfrm.architecture()[0]

if bit=="64bit":
    import chek
    chek.reg()
elif bit=="32bit":
    import wao
    wao.reg()
