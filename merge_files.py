import pandas as pd

# Load in the hanzi + pinyin and hanzi + english files
# Set the column separator to tab
hanzi_pinyin = pd.read_csv('hanzi_pinyin.tsv', sep = '\t')
hanzi_english = pd.read_csv('hanzi_english.tsv', sep = '\t')

# Merge the hanzi + english file onto the hanzi + pinyin file 
# Drop any duplicate lines
combined = hanzi_pinyin.merge(hanzi_english, on = '汉字', how = 'left').drop_duplicates()

# Print the table dimensions and the first few entries
print(f'Combined:\n{combined.shape}\n{combined.head()}')

# Write the combined table to a tab-separated values file
combined.to_csv('hanzi_pinyin_english.tsv', index = False, sep = '\t')
