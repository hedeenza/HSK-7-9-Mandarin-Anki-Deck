from xpinyin import Pinyin
import sys

with open(sys.argv[1], 'r', encoding = 'utf-8') as file:
    with open('hanzi_pinyin.csv', 'a', encoding = 'utf-8') as output:
        for line in file:
            pin = Pinyin().get_pinyin(line, splitter = ' ', tone_marks = 'marks')
            output.write(f'{line.strip()},{pin}')

    output.close()
file.close()
