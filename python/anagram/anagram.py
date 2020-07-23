def find_anagrams(word, candidates):
    word_list = sorted(word.lower())
    word_string = "".join(word_list)
    output = []
    for candidate in candidates:
        candidate_list = sorted(candidate.lower())
        candidate_string = "".join(candidate_list)
        if word_string == candidate_string and not candidate.lower() == word.lower():
            output.append(candidate)
    return output
        
