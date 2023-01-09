#5 hour and 11 minutes
f_name = input("Enter file name: ")
hnd = open(f_name)
#takes the white space off from the right hand side 
#var.rstrip()

for txt in hnd:
    txt = txt.rstrip()
    print(txt)

