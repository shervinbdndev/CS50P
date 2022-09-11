temp = input('File name: ')

formats = [
    'gif' ,
    'png' ,
]

jpeg_jpg = (
    '.jpeg' ,
    '.jpg'
)

pdf = (
    '.pdf' ,
    '.PDF'
)

if (temp in ['cat' , 'myfile'] or temp.endswith('.bin')):
    print('application/octet-stream')

elif (temp.split('.')[1] in formats):
    print(f"image/{temp.split('.')[1]}")

elif (temp.endswith(jpeg_jpg)):
    print(f'image/jpeg')

elif (temp.endswith('.zip')):
    print("application/zip")

elif (temp.endswith(pdf) or ' ' in temp):
    print(f"application/pdf")

elif (temp == 'plain.txt'):
    print('text/plain')