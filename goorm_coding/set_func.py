def unique_words(sentences: dict) -> dict:
    word_sets = {}

    for day, sentence_list in sentences.items():
        all_words = []
        
        for sentence in sentence_list:
            sentence = sentence.lower()
            sentence = ''.join(char for char in sentence if char.isalnum() or char.isspace())
            words = sentence.split()
            all_words.extend(words)

        word_sets[day] = set(all_words)
    
    return word_sets


sentences = {
    'day1': [
        "Hello world, welcome to Python!",
        "Python is fun, and Python is powerful?",
        "Hello everyone, have a great day!"
    ],
    'day2': [
        "Learning Python is an exciting journey.",
        "How are you totay?",
        "Ohhh you good at Python!"
    ]
}

print(unique_words(sentences))