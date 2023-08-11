no_of_bottles = 5
dict1 = { -1: f" {no_of_bottles} bottles", 0: "No More bottles", 1: "1 bottle"}
dict2 = { -1: "Go to the store and buy some more, ", 0: "Take it down and pass it around, "}
i = no_of_bottles
while i>-1:
    song_template_part1 = f"{dict1.get(i, str(i)+' bottles')} of beer on the wall, {dict1. get(i, str(i)+' bottles')} of beer.\n"
    song_template_part2 = f"{dict2.get(i-1, 'Take one down and pass it around, ' )}"
    song_template_part3 = f"{dict1.get(i-1, str(i-1)+' bottles')} of beer on the wall.\n" 
    print(song_template_part1 + song_template_part2 + song_template_part3) 
    i-=1
