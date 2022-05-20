
#list of cards in collection
from urllib import response

vintageset = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15, 19, 20, 23, 24, 25, 26, 27, 29, 31, 32, 35, 36, 38, 39, 40,
 43, 44, 46, 48, 53, 60, 62, 63, 66, 68, 69, 72, 74, 76, 77, 78, 81, 82, 83, 84, 97, 99, 102, 109, 110,111, 116, 117, 118, 
 119, 121, 122, 123, 125, 126, 127, 128, 129, 131, 133, 134, 136, 140, 141, 143, 144, 146, 148, 149, 151, 152,153,
 154, 155, 157, 159, 160, 165, 166, 168, 174, 176, 178, 180, 182, 184, 186,187, 189, 191, 192, 193, 194, 196, 197,
 199, 201, 202, 205, 206, 207, 211, 212, 214, 215, 217, 218, 231, 233, 234, 235, 236, 238, 239, 245, 252, 253, 254,
 258, 260, 261, 265, 266, 269, 273, 275, 276, 279, 281, 288, 289, 290, 292, 293, 295, 296, 297, 302, 305, 306, 307,
 308, 320, 321, 322, 324, 329, 331, 332, 333, 337, 338, 339, 345, 348, 349, 352, 355, 359, 360, 361, 363, 365, 366,
 369, 374, 375, 376, 377, 379, 380, 382, 383, 386, 388, 391, 393, 396, 399, 401, 402, 403, 411, 412, 414, 416, 417,
 418, 421, 422, 423, 424, 426, 430, 436, 444, 452, 453, 456, 459, 461, 462, 463, 464, 466, 467, 468, 469, 470, 472,
 473, 475, 476, 477, 479, 481, 482, 483, 493, 494, 495, 503, 507, 508, 509, 512, 513, 514, 516, 517, 519, 521, 523,
 524, 527, 528, 529, 531, 532, 534, 535, 536, 539, 540, 541, 542, 543, 544, 545, 546, 548, 549, 551, 552, 563, 564,
 567, 578, 624, 649, 690, 714, 787]

def find_missing(vintageset):
    vintageset = input("How many cards are in the set? ")
    #vintageset.sort()
    return [x for x in range(vintageset[0], vintageset[-1]+1) 
                               if x not in vintageset]
print("Here are the cards you need for your set: ", vintageset)
#print("Here are the cards you need for your set: " + find_missing(vintageset))

def add_cards(vintageset):
    update = input('Enter number/s on back of cards to list: ')
    vintageset_update = update + vintageset
    vintageset_update.sort()
    print(vintageset_update)

def main():
    print('Please select an option listed below: ')
    resoponse = input('1: Missing Cards \n2: Add Cards \n  ')
    
    if response == '1':
        find_missing(vintageset)
    elif response == '2':
        add_cards(vintageset)
    else:
        print("Please choose again")

main()
