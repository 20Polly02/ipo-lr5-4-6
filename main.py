with open("text.txt", "r",encoding= "utf-8") as file_first:
    string = file_first.read().split(" ")
    with open("output.txt", 'w',encoding= "utf-8") as file_second:
      for word in string[::-1]:
        file_second.write(word)

