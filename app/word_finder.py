from typing import List


class WordFinder:
    def __init__(self, words: List[str]) -> None:
        self.word_dict = {}
        for word in words:
            self.add(word)

    def add(self, word: str) -> None:
        sorted_word = "".join(sorted(word))
        if self.word_dict.get(sorted_word, None) is None:
            self.word_dict[sorted_word] = []
        self.word_dict[sorted_word].append(word)

    def find(self, word: str) -> List[str]:
        sorted_word = "".join(sorted(word))
        return self.word_dict.get(sorted_word, [])


if __name__ == '__main__':
    word_finder = WordFinder(['asd', 'asdd', 'fre', 'dsa'])
    print(word_finder.find('sad'))
