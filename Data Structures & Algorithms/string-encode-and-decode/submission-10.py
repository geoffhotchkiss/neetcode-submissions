class Solution:

    def encode(self, strs: List[str]) -> str:
        word_encodes = []

        if strs == "":
            return []

        for word in strs:
            if word == "":
                word_encode = "!"
            else:
                word_encode = [str(ord(x)) for x in word]
            word_encodes.append(",".join(word_encode))
        
        print(f"Encoded {strs=} as {word_encodes=}")
        return ";".join(word_encodes)


    def decode(self, s: str) -> List[str]:
        print(f"{s=}")
        encoded_words = s.split(";")

        words = []

        if s == "":
            return []

        """
        if s == '!':
            return [""]
        """

        for encoded_word in encoded_words:
            if encoded_word == "!":
                words.append("")
                continue

            word_decode = [chr(int(x)) for x in encoded_word.split(",")]
            words.append("".join(word_decode))

        return words

