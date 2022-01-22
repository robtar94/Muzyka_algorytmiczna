def count_words(filename):
    """Obliczenie przybliżonej liczby słów w danym pliku."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read() 
    except FileNotFoundError:
        print(f"Przepraszamy, ale plik {filename} nie istnieje.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Plik {filename} zawiera {num_words} słów.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
