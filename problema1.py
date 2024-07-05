def evaluatePalindrome(text: str) -> bool:
    text = text.lower().replace(" ","")
    if text == text[::-1]:
        return True
    return False


if __name__ == "__main__":
    print(evaluatePalindrome("A luna ese anula"))