""" Encoding:: Rotation with integer 1-25
 decoding:: provide a decoded word, and the string that word is located in
  search for substrings matching the length of that provided word,  ::remember to keep capitals in mind
  if a key is applied and the word is not found we try a new key, keep trying until we find the key word in our decoded string , if the decoded keyword is not found send an error
  """
def decode_word(word, rotation):
    """Decode a single 'word' by shifting characters backward by 'rotation'."""
    decoded_chars = []
    for ch in word:
        if ch.islower():
            # Decode lowercase
            shifted_ord = (ord(ch) - ord('a') - rotation) % 26 + ord('a')
            decoded_chars.append(chr(shifted_ord))
        elif ch.isupper():
             # Decode uppercase
            decoded_chars.append(ch)
        else:
            # Leave non-alphabetic characters as-is
            decoded_chars.append(ch)
    return "".join(decoded_chars)


def decode_sentence(words, rotation):
    """Decode an entire list of 'words' using the given rotation."""
    decoded_words = []
    for w in words:
        decoded_words.append(decode_word(w, rotation))
    return " ".join(decoded_words)

rotation=0;
opt=input("Do you want to encode or decode ,E/D?, N to quit ")
while opt.lower()!="n":
    if opt.lower() == "d":
        keyword = input("Provide your **decoded** keyword: ")
        encoded_text = input("Input the encoded string: ")
        encoded_words = encoded_text.split(" ")

        # Only look at words that match the length of the known keyword
        potential_matches = [word for word in encoded_words if len(word) == len(keyword)]

        found_key = None

        # Try all possible keys 1 through 25
        for r in range(1, 26):
            # Check if decoding any potential match with this r produces the keyword
            for word in potential_matches:
                if decode_word(word, r) == keyword:
                    found_key = r
                    break  # Found a match; we can stop checking more potential matches
            if found_key is not None:
                break  # Stop searching once we've found a working rotation

        if found_key is None:
            print("Error: The provided keyword was not found for any key (1–25).")
        else:
            # Decode the entire string with found_key
            decoded_string = decode_sentence(encoded_words, found_key)
            print(f"Successfully decoded using key = {found_key}")
            print("Decoded string:", decoded_string)



    elif opt.lower()=="e":
        charset=[]
        while rotation<1 or rotation>25:
            rotation=int(input("What rotation do you want to apply to your input string, enter a number 1-25 "))

        string=input("Enter the string you want to encode with key : "+str(rotation)+" ").split(" ")
        for c in range(len(string)):
            charset.append(list(string[c]))
        for z,w in enumerate(charset):
            for i,ch in enumerate(w):
                if ch.isupper():
                    continue
                else:
                    w[i]=chr((ord(ch)-ord('a')+rotation)%26+ord('a'))
            charset[z]=''.join(w)
        encoded_string=" ".join(charset)
        print(encoded_string)
        opt=input("Do you want to encode or decode ,E/D?, N to quit ")




















