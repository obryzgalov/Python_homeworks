from googletrans import Translator

with open('task4in.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    with open('task4out.txt', 'w', encoding='UTF-8') as f1:
        try:
            f1.write(Translator().translate(content, dest='ru').text)
        except ValueError:
            pass


