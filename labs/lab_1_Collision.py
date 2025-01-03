import hashlib

#importing and reading the contents of the file
with open ("message1.bin","rb") as file1:
    content1 = file1.read()
with open ("message2.bin","rb") as file2:
    content2 = file2.read()
print(content1)
# #calculating md5 hash of the files
# md5Hash1 = hashlib.md5(content1).hexdigest()
# md5Hash2 = hashlib.md5(content2).hexdigest()

# #calculating sha-1 hash of the files
# sha1Hash1 = hashlib.sha1(content1).hexdigest()
# sha1Hash2 = hashlib.sha1(content2).hexdigest()


print("md5 Hashes: \n",md5Hash1,'\n',md5Hash2)
print("Collision found in md5." if md5Hash1 == md5Hash2 else "No collision found in md5")
print("SHA-1 Hashes: \n",sha1Hash1,'\n',sha1Hash2)
print("Collision found in SHA-1." if sha1Hash1 == sha1Hash2 else "No collision found in SHA-1")
