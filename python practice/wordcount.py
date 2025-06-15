def count_words(filename):
    with open(Apple.txt, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = {}
        
        for word in words:
            word = word.lower().strip('.,!?()"\'')  # Basic cleaning
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
                
    return word_count
