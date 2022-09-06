def msg(txt):
    print('X'*len(txt)+'XXXX')
    print('X',len(txt)*' '+' X')
    j = print('X',txt,'X')
    print('X',len(txt)*' '+' X')
    print('X'*len(txt)+'XXXX')
mss = input('Digite uma Mensagen: ')
msg(mss)