# Having a two or more choices.

import re

text = "I have a cat and a dog."
print(re.findall(r"cat|dog", text)) # like a logical or in programming but with regex

# \. mmeans a literal period 

