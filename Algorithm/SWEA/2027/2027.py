'''
#++++
+#+++
++#++
+++#+
++++#
'''
string = '+++++'
for i in range(5):
    line = list(string)
    line[i] = '#'
    result = "".join(line)
    print(result)