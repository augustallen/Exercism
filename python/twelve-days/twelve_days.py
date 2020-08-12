def recite(start_verse, end_verse):
    song = """
and a Partridge in a Pear Tree.
two Turtle Doves,
three French Hens,
four Calling Birds,
five Gold Rings,
six Geese-a-Laying,
seven Swans-a-Swimming,
eight Maids-a-Milking,
nine Ladies Dancing,
ten Lords-a-Leaping,
eleven Pipers Piping,
twelve Drummers Drumming,
""".split("\n")
    days = {
        1 : "first",
        2 : "second",
        3 : "third",
        4 : "fourth",
        5 : "fifth",
        6 : "sixth",
        7 : "seventh",
        8 : "eighth",
        9 : "ninth",
        10 : "tenth",
        11 : "eleventh",
        12 : "twelfth"
        }
    string = f'On the {days[start_verse]} day of Christmas my true love gave to me: \n' + '\n'.join(song[start_verse:0:-1])
    output = list(string) 
    return output

print(recite(1,1))