data = 'ini adalah string'
print(data,type(data),'\n')

# 1 cara membuat string

'''
    1. Dengan menggunakan single quote '....'
       atau Dengan menggunakan double quote '....'
    2. Dengan menggunakan tanda \
    3. Dengan menggunakan stirng literal atau raw
'''

## contoh nomer 1
data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"halo, apa kabar"')
print("'halo, apa kabar'")
print("ini adalah hari jum'at")

## contoh nomer 2

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t?')

# membuat tanda backslash (\)menjadi string
print("C:\\user\\python")

# membuat tab, dengan menambahkan (t) setelah tanda (\)
print("ini adalah \t\t tab")

# membuat backspace, dengan menambahkan (b) setelah (\)
print("ini adalah \bbackspace")

# newline, dengan menambahkan (n) atau (r) setelah tanda (\)

# \n ==> LF --> line feed ->> unix, macos, linux
print("baris pertama. \nbaris kedua.")
# \r ==> CR --> carieg return ->> commodore, acorn, lisp
print("baris pertama. \rbaris kedua.")
# \r\n ==> CRLF --> line feed carieg return ->> windows
print("baris pertama. \r\nbaris kedua.")

# contoh nomer 3

# contoh 

print('C:\new folder') # ini kita perlu menambahkan backslash 
                       # terlebih dahulu untuk merubahnya namun dengan 
                       # menggunakan raw kita tidak perlu merubahnya 

# menggunaka raw, dengan menggunaka (r) di awal sebelum single quote
print(r'C:\newfolder\folder_saya')

# multiline literal string, dengan menggunakan tanda ('''....''')
print('''
Nama  : Muh. Sofiyan 
Prodi : Teknik Informatika
      ''')

# multiline literal string dan raw
print(r'''
Nama     : Muh. Sofiyan 
Prodi    : Teknik Informatika
Websoite : www.muh.sofiyan/new_website 
''')