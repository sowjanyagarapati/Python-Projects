import base64

#class to encrypt and decrypt the given text
class textEncryption():
    def __init__(self,text):
        self.text = text
        print(f"original string {self.text}")

    def encrypt(self):
        """function to encrypt the text"""
        encodedtext = self.text.encode('ascii')
        b64bytes = base64.b64encode(encodedtext)
        return b64bytes.decode('ascii')

    def decrypt(self):
        """function to decrypt the text"""
        encrypted = self.encrypt()
        print(f"encrypted string {encrypted}")
        decodedtext = encrypted.encode('ascii')
        b64debytes = base64.b64decode(decodedtext)
        return f"decrypted string {b64debytes.decode('ascii')}"

#calling the main method
if __name__=='__main__':
    #object creation
    encryptionobj = textEncryption(input("enter:"))
    print(encryptionobj.decrypt())
