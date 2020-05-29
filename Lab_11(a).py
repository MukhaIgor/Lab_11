b = open('g.txt', mode='w')
with open('f.txt') as a:
    for line in a:
        m = line.rstrip('\n')
        b.write(m+'!'+'\n')
b.close()
