with open("text.txt", "r",encoding= "utf-8") as file_first:#открываем файл text.txt для чтения используя кодировку "utf-8" для корректной обработки символов, и создаем переменную для обозначения обьекта файла,открытого для чтения
    string = file_first.read().split(" ")#используем split() чтобы разбить строку на слова, разделяя их пробелом и присваиваем это значение переменной 
    with open("output.txt", 'w',encoding= "utf-8") as file_second:#открываем файл output.txt для записи, создаем переменную для обозначение обьекта файла,открытого уже для записи
      for word in string[::-1]:#используем цикл for для перебора слов в строке
          #создаем обратный список слов используя срез [::-1],где -1 это шаг и это значит что будет обратная запись строки
        file_second.write(word)#запись слов в файл 

