# REMOVE EXTRA WHITESPACES
import re  

text = """HELLO         WORLD"""

pattern = r"\s+"

new_word = re.sub(pattern, " ", text)

print(new_word)