import random

from custom_tokenizer_abstract import CustomTokenizer
import random

class RandomLengthTokenizer(CustomTokenizer):
    def __init__(self, min_len=1, max_len=5):
        self.min_len = min_len
        self.max_len = max_len

    def tokenize(self, text):
        """
        Tokenizes text into randomly sized subwords.

        Args:
            text (str): The input text to tokenize.

        Returns:
            List[str]: A list of tokenized subwords.
        """
        words = text.split()
        tokenized_text = []

        for word in words:
            if len(word) <= self.min_len:
                tokenized_text.append(word)  # Keep very short words as is
                continue

            # Determine random split points
            split_points = sorted(random.sample(range(1, len(word)), random.randint(1, min(len(word), self.max_len) - 1)))

            # Split the word into tokens
            tokens = []
            prev = 0
            for point in split_points:
                tokens.append(word[prev:point])
                prev = point
            tokens.append(word[prev:])

            tokenized_text.extend(tokens)

        return tokenized_text

