"""
Created on Tue Nov  2 14:39:03 2021
@author: M Rezaei
"""

import win32wnet 
win32wnet.WNetAddConnection2(1, 'Z:', r'http://hostIPAddress/files/', None, 'username', 'password')


crio_file = open(r"Z:\C\test2.txt", "rt")
data = crio_file.read()
data = data.replace('1', '2',1)


crio_file = open(r"Z:\C\test2.txt", "wt")
data = crio_file.write(data)
crio_file.close()



win32wnet.WNetCancelConnection2( 'Z:',0,1)