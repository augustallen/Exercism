def recite(start_verse, end_verse):
    song = """
a Partridge in a Pear Tree.
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
    output = [f'On the {days[start_verse]} day of Christmas my true love gave to me: ']
    output[0] = str(output[0]) + str(song[start_verse:0:-1][0])
    return output

expected = [
    "On the second day of Christmas my true love gave to me: "
    "two Turtle Doves, "
    "and a Partridge in a Pear Tree."
]

print(f"Expected:\n{expected}\n")
print(f"Received:\n{recite(2,2)}\n")

