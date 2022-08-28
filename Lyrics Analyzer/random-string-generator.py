import random
import string

# printing lowercase
letters = string.ascii_lowercase
print("Below is a random string of lowercase letters")
print ( ''.join(random.choice(letters) for i in range(10)))

# printing uppercase
letters = string.ascii_uppercase
print("Below is a random string of uppercase letters")
print ( ''.join(random.choice(letters) for i in range(10)) )

# printing letters
letters = string.ascii_letters
print("Below is a random string of mixed case letters")
print ( ''.join(random.choice(letters) for i in range(10)) )

# printing digits
letters = string.digits
print("Below is a random string of numbers")
print ( ''.join(random.choice(letters) for i in range(10)) )

# printing punctuation
letters = string.punctuation
print("Below is a random string of punctuation characters")
print ( ''.join(random.choice(letters) for i in range(10)) )