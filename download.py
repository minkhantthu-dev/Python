from urllib.request import urlretrieve


link = input('Image download link : ')

fileName = input('file Name :')

urlretrieve(link,'image/' + fileName + '.jpg')