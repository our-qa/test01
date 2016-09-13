import  os
line = os.linesep
user = input('FILE:')
while True:
    if os.path.exists(user):
        print('该用户名已经存在')
        user = input('FILE:')
    else:
        break

all = []
while True:
    choice = input('ENTER>>>')
    if choice == '.':
        break
    all.append(choice)
file = open(user,'w')
file.writelines(['%s%s'%(x,line) for x in all])
file.close()
print('Done')
    
