def is_valid(isbn):
    isbn = isbn.replace("-","")
    isbn = [char for char in isbn]
    try:
        if isbn[-1]=="X":
            isbn[-1]=10
        isbn = [int(i) for i in isbn]
    except: 
        return False
    return len(isbn)==10 and (isbn[0]*10 + isbn[1]*9 + isbn[2]*8 + isbn[3]*7 + isbn[4]*6 + isbn[5]*5 + isbn[6]*4 + isbn[7]*3  + isbn[8]*2  + isbn[9]*1) % 11 == 0