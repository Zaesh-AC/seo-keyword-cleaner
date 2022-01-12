# SEO Keyword Cleaner
Script that helps users clean their SEO CSV files.

# Instructions

## Python3 required

# IMPORTANT
For all input CSV file there MUST be ONE column to search in for key, otherwise the script will fail, because it searches in first column of the input file so format your origin CSV file following the rule: 1° COLUMN -> 1 ROW TO COMPARE

To start the helper type: ```python3 cleaner.py```

## CSV Origin file
-o, --origin: Origin CSV file that needs cleaning. Delimiter has to be ';'. Use '-o' or '--origin' during the invocation of the script to pass it the file. If the file is in another path, include the path. Delimiter must be ';'.

## Destination file
-d, --dest: Destination file name where you want to put the results in. The script will generate 2 files, one with the valid voices and another one with the discarded voices (all the voices the matches the keys you're searching for). This parameter can be omitted and the default will be 'output'.
The files will be named 'output_valid.csv' and 'output_invalid.csv', or whatever you choose.

## Keys File
-k, --keys: Keys to search for origin file. Like the origin file, use '-k' or '--keys' to pass the file to the script and let it loop through it to analyze and remove match. Delimiter must be ','.