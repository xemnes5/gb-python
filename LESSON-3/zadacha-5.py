

s = 0
print('Введите строку чисел, разделенных пробелом и нажмите ENTER.\nДля завершения программы введите символ $  ')
pr = input('>> ').split()

def mysum(*args):
     mylist = [int(x) for x in args]
     global s 
     s += sum(mylist)
     print('Сумма всех введенных чисел = ', s)
     
 
while pr:
    if '$' in pr:
       mysum(*pr[:pr.index('$')])
       break
    mysum(*pr)
    pr = input('>> ').split()
