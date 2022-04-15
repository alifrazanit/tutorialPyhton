message = input(">>>> ")
emojiMapping = {
    ":D":"😀",
    ";)":"😉",
    ":)":"😊",
    ":*":"😘"
}

word = message.split(" ")

output = ""
for keyword in word:
    output = output + emojiMapping.get(keyword, keyword) + " "

print(output)