import pandas as pd

# Read the combined hanzi + pinyin + english file
df = pd.read_csv('hanzi_pinyin_english.tsv', sep = '\t')


# Examining the full table
print('Full Table:')
# Print the dimensions of the table
print(f'Pre-Processing: {df.shape}')


# Examining the Pinyin column
print('\nMissing Pinyin:')
# Filter the table to only lines where the Pinyin (the column named 'han zi ') is empty
missing_pinyin = df[df['hàn zì '].isna()]
# Print the dimensions of the new table with missing Pinyin
print(f'Post-Processing (Pinyin): {missing_pinyin.shape}')
# Print the lines with missing Pinyin
print(f'{missing_pinyin}')


# Examining the English column
print('\nMissing English:')
# Filter the table to only lines where the English translation (the column named 'Chinese character') is empty
missing_translations = df[df['Chinese character'].isna()]
# Print the dimensions of the new table with missing English translations
print(f'Post-Processing (English): {missing_translations.shape}')
# Print the lines with missing English translations
print(f'{missing_translations}')
