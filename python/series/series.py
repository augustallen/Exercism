def slices(series, length):
    if not len(series)>0:
        raise ValueError("No series supplied.")
    if length<1:
        raise ValueError("Length cannot be less than 1.")
    if length>len(series):
        raise ValueError("Slice length cannot be longer than series.")
    output = []
    loc = 0
    for digit in series:
        result = series[loc:loc+length]
        if len(result) == length:
            output.append(series[loc:loc+length])
        loc += 1
    return output