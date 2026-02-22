import random
from pathlib import Path

encouraging_words = []
def load_encouraging_words():
    global encouraging_words
    base_path = Path(__file__).parent
    file_path = base_path / "encouragement.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            
            encouraging_words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        encouraging_words = [ "Keep going!", 
            "You've got this!", 
            "People appreciate your presence!"]

def retrieve_quote() -> str:
    if len(encouraging_words) < 1:
        load_encouraging_words()
    return random.choice(encouraging_words)

if __name__ == "__main__":
    load_encouraging_words()
    print(retrieve_quote())