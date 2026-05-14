from xpinyin import Pinyin
import sys

# Open the hanzi.csv file, in argument 1 after the script name
# Set to "read-only" and "utf-8" characters
with open(sys.argv[1], 'r', encoding = 'utf-8') as file:
    # Create a new file called "hanzi_pinyin.csv", which will contain the output
    with open('hanzi_pinyin.csv', 'a', encoding = 'utf-8') as output:
        # for each line in the hanzi.csv file...
        for line in file:
            # Generate the pinyin, including the tone marks, and separate syllables by a space
            pinyin = Pinyin().get_pinyin(line, splitter = ' ', tone_marks = 'marks')
            # Write each line to the output file in the format "hanzi,pinyin"
            output.write(f'{line.strip()},{pinyin}')
    # Close the output file (hanzi_pinyin.csv)
    output.close()
# Close the input file (hanzi.csv)
file.close()
