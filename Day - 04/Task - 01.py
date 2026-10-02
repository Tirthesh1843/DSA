# LC:409 
string = "tiweygbkalooahjdsfoonkjsiadgiudsytflkdjclovkuydsi78fywdseaofjsaiodfye8qwiuyeiqwofdsakjdldkasiosdui0opkdjbiahd78ctcjkahdiuatdabxjknoiasujdio9asudysac nsioudhnsadjaosxcnsahcchnxnjazohjnnnbbboioollllllnnnnnnnnnnnnnnnnnnaaaaqaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccccccddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffggggggggggggggggggghhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkllllllllllllllllllllmmmmmmmmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnoooooooooooooooooopppppppppppppppppqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrrsssssssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz"

count = {}
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
ans = 0
odd = False
for i in count:
    if count[i] % 2 == 0:
        ans += count[i]
    else:
        ans += count[i] - 1
        odd = True
if odd:
    ans += 1
print(ans)