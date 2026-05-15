import sys
from deep_translator import GoogleTranslator 

# Choose a starting line for the translation. If no input, default to 1.
starting_index = int(input(f'What line would you like to start with?\n') or 1)

# Open the hanzi.csv file, in argument 1 after the script name
# Set to "read-only" and "utf-8" characters
with open(sys.argv[1], 'r', encoding = 'utf-8') as input:
    # Create a new file called "hanzi_english.tsv", which will contain the output
    # Set to "append" mode, so the translation can be safely resumed if interrupted
    with open('hanzi_english.tsv', 'a', encoding = 'utf-8') as output:
        # for each line in the hanzi.csv file...
        for index, line in enumerate(input):
            # If the current index is less than the desired starting index...
                # Note: starting index is adjusted to reflect internal 0-indexing
            if index < starting_index - 1:
                # Skip it
                continue
            # Otherwise...
            else: 
                # Strip the line down to its primary text
                original_text = line.strip()
                # Perform the translation from Mandarin to English 
                english_text = GoogleTranslator(input = 'zh-CN', output = 'en').translate(original_text)
                # Write to File
                output.write(f'{original_text}\t{english_text}\n')
                # Print the line number, original text, and English to mark progress
                print(f'{index + 1} - {original_text}\t{english_text}')
    # Close the output file (hanzi_english.tsv)
    output.close()
# Close the input file (hanzi.tsv)
input.close()
