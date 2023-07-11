import random

from adjectives import adjectives
from names import names


def generate_id():
    hashstr = f"{adjectives[random.randint(0, len(adjectives)-1)]}-{names[random.randint(0, len(names)-1)]}"
    return hashstr


if __name__ == "__main__":
    print(f"{len(adjectives) * len(names)} Unique IDs possible.")
