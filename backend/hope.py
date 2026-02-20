import random

encouraging_words = []
def load_encouraging_words():
    from pathlib import Path
    base_path = Path(__file__).parent
    file_path = base_path / "encouragement.txt"
    with open(file_path) as f:
        for quote in f:
            encouraging_words.append(quote)

def retrieve_quote() -> str:
    if len(encouraging_words) < 1:
        load_encouraging_words()
    return random.choice(encouraging_words)

if __name__ == "__main__":
    load_encouraging_words()
    print(retrieve_quote())