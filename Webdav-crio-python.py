
# Requirements
# 1- win32wnet
import win32wnet 

# Create Map Network Drive to transfer or edit files on NI-cRIO
win32wnet.WNetAddConnection2(1, 'Z:', r'http://hostIPAddress/files/', None, 'username', 'password')


# if there is no error in line 10, Map Network drive is created successfully.
# otherwise, you should revise the inputs, 
# there are some possible reasons,
# 1- NI-cRIO is not connected to Host PC, you can check it using NI-MAX software.
# 2- NI-cRIO IP, username or password is wrong that can be checked with NI-MAX software.


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