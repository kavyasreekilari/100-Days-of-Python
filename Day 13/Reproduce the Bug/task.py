from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # when the range is from 1 to 6, the index went out of bounds, because in list index starts from 0. hence corrected the range to 0,5
print(dice_images[dice_num])
