text = "X-DSPAM-Confidence:    0.8475"

found = text.find(':')

piece = text[found +2:]

value = float(piece)
print(value)

#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.