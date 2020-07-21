def proteins(strand):
    codon_dict = {
        "AUG":"Methionine", 
        "UUU":"Phenylalanine",
        "UUC":"Phenylalanine",
        "UUA":"Leucine",
        "UUG":"Leucine",
        "UCU":"Serine",
        "UCC":"Serine",
        "UCA":"Serine",
        "UCG":"Serine",
        "UAU":"Tyrosine",
        "UAC":"Tyrosine",
        "UGU":"Cysteine",
        "UGC":"Cysteine",
        "UGG":"Tryptophan",
        "UAA":"STOP",
        "UAG":"STOP",
        "UGA":"STOP"
        }
    codons=[strand[i:i+3] for i in range(0,len(strand),3)]
    output=[]
    for codon in codons:
        amino_acid = codon_dict[codon]
        if amino_acid=="STOP":
            break
        else:
            output.append(amino_acid)
    return output



