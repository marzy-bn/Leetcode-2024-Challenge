class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split():
            for char in word:
                if char in set(brokenLetters):
                    count += 1
                    break
        return len(text.split()) - count
                