#Sneha's Code
#Adding Graphics
#Importing images from files

from PIL import Image

#This graphic will be displayed if player 1 wins
Filename_Winning1 =  "IMG_happy1.jpg"
img1 = Image.open(Filename_Winning1)

#This graphic will be displayed if player 2 wins
Filename_Winning2 = "IMG_happy2.jpg"
img2 = Image.open(Filename_Winning2)

#This graphic will be displayed if player 1 loses
Filename_Losing1 = ("IMG_sad1.jpg")
img3 = Image.open(Filename_Losing1)

#This graphic will be displayed if player 2 loses
Filename_Losing2 = ("IMG_sad2.jpg")
img4 = Image.open(Filename_Losing2)

#This graphic will be displayed when player 1 is thinking about their next move
Filename_Thinking1 = ("IMG_thinking1.jpg")
img5 = Image.open(Filename_Thinking1)

#This graphic will be displayed when player 1 is thinking about their next move
Filename_Thinking2 = ("IMG_thinking2.jpg")
img6 = Image.open(Filename_Thinking2)
