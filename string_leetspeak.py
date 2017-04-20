leetspeak = ('A', '4'), ('E', '3'), ('G', '6'), ('I', '1'), ('O', '0'), ('S', '5'), ('T', '7')
paragraph = """On July 16, 1969, the Apollo 11 spacecraft launched from the Kennedy Space Center in Florida. Its mission was to go where no human being had gone before—the moon! The crew consisted of Neil Armstrong, Michael Collins, and Buzz Aldrin.""".upper()

new_paragraph = paragraph
for old, new in leetspeak:
    new_paragraph = new_paragraph.replace(old, new)

print (new_paragraph)
