"""
Created on Tue Nov  2 14:39:03 2021
@author: M Rezaei
"""
# Requirements
# 1- win32wnet
import win32wnet 

# Create Map Network Drive to transfer or edit files on NI-cRIO
win32wnet.WNetAddConnection2(1, 'Z:', r'http://hostIPAddress/files/', None, 'username', 'password')


crio_file = open(r"Z:\C\test2.txt", "rt")
#read file contents to string
data = crio_file.read()
#replace all occurrences of the required string
data = data.replace('1', '2',1)


crio_file = open(r"Z:\C\test2.txt", "wt")
#Write file 
data = crio_file.write(data)
#close the input file
crio_file.close()


# Close Map Network Drive to transfer or edit files on NI-cRIO
win32wnet.WNetCancelConnection2('Z:',0,1)