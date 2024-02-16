# # Program: Overwriting a File in Python
# """ File Content: 
# Program: To Overwrite a File in Python
# Overwriting a File : Replacing old contents of the file """

# # open the file using write only mode
# handle = open("favtutor.txt", "r+")

# # seek out the line you want to overwrite

# handle.write("File Overwritten.")


# # close the file
# handle.close()

# # To read the contains of the file
# # open the file in read mode
# f = open("favtutor.txt", "r")
# print(f.read())
# f.close()


# import csv 
# label =['Links','Company','Business Registration','Year of Incorporation','Chief Executive','CEO Position','Business Enquiry','Business Contact Person Position','Office Address','Postcode','City / Town','State','Country','Telephone','Email','Raw Material Used','Production Processes','Products Manufactured / Business Line']

# with open('final5.csv','r+') as f:

# 	w = csv.writer(f)
# 	w.writerow(label)

# 	f.close()

d = {'Link':'abc',
	'huy' : '1'
}

d = dict()
d['x'] = 'abcc'
d['huy'] = 'xzu'

print(d)
