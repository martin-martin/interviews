def double_characters(word):
    if not word:
        raise ValueError("Received empty string")
    double = ""
    for letter in word:
        double += letter * 2
    return double


if __name__ == "__main__":
    print(double_characters("Martin"))
    print(double_characters(""))
