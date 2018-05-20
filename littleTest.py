thelist = ['no', 'test1', 'test2']
i=3
if 'test%s' % (str(i)) in thelist:
    thelist.remove('test%s' % (str(i)))
test = 'yonose'
print(test[:100])
print(thelist)
input()