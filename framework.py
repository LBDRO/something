__author__ = 'owen'
file_type = "framework"

def get(line, filename):
    new = open(filename, 'r')
    m = new.read()
    l = m.split('\n')
    new.close()
    return l[line-1]

def save(line, filename):
    new = open(filename, 'a')
    new.write('\n')
    new.write(line)
    new.close()

def check(t, obj):
    return isinstance(t, obj)

def ltstring(convert):  # [1,2,3]
    s = map(str, convert)  # ['1','2','3']
    s = ''.join(s)  # '123'
    return s

def ltint(convert):
    i = map(str, convert)
    i = ''.join(i)
    i = int(i)
    return i
