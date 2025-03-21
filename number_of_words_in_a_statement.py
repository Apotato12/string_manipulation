# Program 7 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2

def words_in_statement():
    """asks the user to input a statement and prints the number of words in the statement."""
    statement = input("Please enter a complete statement: ")

    statement_to_words = statement.split()

    word_count = len(statement_to_words)

    print("Number of words in the statement:", word_count)

words_in_statement()