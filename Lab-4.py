from random import randint
s1 = 'Trees,Dogs,Girls,Ghosts,World,Calendar'.split(',')
s2 = 'Are,Near,Belong,Get,Due to,Depend on'.split(',')
s3 = 'Black,Happy,At Home,Free,Well known,Gusty '.split(',')
phrase = ''
phrase += s1[randint(0, len(s1) - 1)]
phrase += ' '
phrase += s2[randint(0, len(s2) - 1)]
phrase += ' '
phrase += s3[randint(0, len(s3) - 1)]
print(phrase)