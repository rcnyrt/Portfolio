'''
Final Programming task, 50 points

Text to analysis: "alice.txt" (moodle)
Min. to be evaluated : module "texta" with classes "TextIO" and "TextAnalyser", it was a part of your previous homeworks and Programming Task 04

1. In the enclosed file "fpt_03.py", your task is to implement the functionality of options: 1) 2) 3) 4) 5) 6) 9)

In order to do it you also need to:

2. Extend the functionality of 'TextAnalyser' class by implementing the following methods:

2.1 for option 1):


def set_list_of_sentences(self) -> None:
        """
        Function assigns the instance variable _list_of_sentences
        """

 def get_list_of_sentences(self) -> list:
        """
        Function returns the list of sentences in the "text"
        """

2.2 for option 2):
def set_number_of_sentences(self) -> None:
        """
        Function assigns the instance variable _number_of_sentences
        """

def get_number_of_sentences(self) -> int:
        """
        Function returns number of sentences  in the "text"
        """

2.3 for option 3):
def set_list_of_lines(self) -> None:
        # Function assigns the instance variable _list_of_lines

def get_list_of_lines(self) -> list:
        #Function returns the list of lines in the "text"

2.4 for option 4):
def set_number_of_lines(self) -> None:
        #Function assigns the instance variable _number_of_lines
        
def get_number_of_lines(self) -> int:
        #Function returns number of lines  in the "text"

2.5 for option 5):

def get_searched_phrase(self):
        """
        Function returns the instance variable _searched_phrase
        """

def get_is_phrase_a_word(self, is_word):
        """
        Function returns the instance variable _is_phrase_a_word (bool)
        """

def set_search_phrase_lines(self, phrase: str, isPhraseAWord=True) -> list[str]:
        """
        Function assigns the instance variable _searched_phrase
        Function assigns the instance variable _is_phrase_a_word (bool)
        Function assigns the instance variable _lines_with_searched_phrase
        Phrase is treated as separate word or as an element of another phrase
        Parameters:
            phrase: searched text
            isPhraseAWord: is searched phrase a word or a part of a word
        """
def get_search_phrase_lines(self) -> list[str]:
        """
        Function returns the list of lines containing the given phrase.
        """
2.6 for option 6):

def set_number_of_searched_phrases(self) -> int:
        """
        Function assigns the instance variable: _number_of_searched_phrases
        (it is not number of lines, we can have several phrases inside a line)
        """
def get_number_of_searched_phrases(self) -> int:
        """
        Function returns the number of occurrences of the given phrase
        """

In order to implement the functionality 9):
Assume that your task is to save list of lines containing the given phrase and a number of founded phrases

Use the function from your texta module, class TextIO :
def write_to_file(self, text: str, mode: str = 'w') -> None:
        """
        Function writes the text to the file in a given mode
        Parameters:
            text: text to be written to the file
            filepath: file path to file
            mode: writing text mode ('a' or 'w', 'w' is default)
        """

'''
from texta import TextIO, TextAnalyser


def print_results(title: str, results: list[str]) -> None:
    """
    Function prints the results in a formatted way.
    :param title: title of the results"""
    print(title)
    for i, s in enumerate(results, 1):
        print(f"{i}. {s}")


def print_word_frequency(data: list[tuple[int, str, int]]) -> None:
    """
    Function prints the word frequency in a formatted way.
    :param data: list of tuples containing word frequency information
    """

    for d in data:
        print(f"{d[0]}. {d[1]}; length: {d[2]}")


menu = '''
-------------------------------------

What do you want to print to the terminal?
Select the option.

-------------------------------------

1. List of sentences
2. Total number of sentences
3. List of lines
4. Total number of lines
5. Search phrase - list of lines containing searched phrase
6. Search phrase - number of occurances
7. The list of the most frequent words, sorted in descending way
8. The list of the longest words, sorted in descending way
9. Write a list of lines containing searched phrase to a text file
10. Write the last searched phrase information to a database

Press "0" if you want to quit the application

-------------------------------------

'''
# file = input('\nEnter the text filepath: ')
# Adapt the file path to your situation
file = r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\alice.txt'
s_line = int(
    input('Enter the line number from which you want to start analysis: '))
s_line = 255
db_file_path = 'AliceDB.db'
report_file_path = 'report.txt'

tio = TextIO(file, s_line)
tio.read_from_file()
our_text = tio.get_text()
if our_text:
    ta = TextAnalyser(our_text)
    print(ta)  # inside TextAnalyzer class implement the short information banner
    print(menu)
    while True:
        opt = int(input('Enter the option --> '))
        try:
            if opt == 0:
                break
            if opt == 1:
                ta.set_list_of_sentences()
                los = ta.get_list_of_sentences()
                number = int(
                    input('Enter the number of sentences you want to print to the terminal: '))
                print_results('List of sentences:', los[:number])
            elif opt == 2:
                ta.set_number_of_sentences()
                nos = ta.get_number_of_sentences()
                print(f'The number of sentences are: {nos}')
            elif opt == 3:
                ta.set_list_of_lines()
                lol = ta.get_list_of_lines()
                number = int(
                    input('Enter the number of lines you want to print to the terminal: '))
                print_results("List of lines:", lol[:number])
            elif opt == 4:
                ta.set_number_of_lines()
                tnol = ta.get_number_of_lines()
                print(f'Total number of lines is: {tnol}')
            elif opt == 5:
                s_phrase = input('\nEnter the phrase you want to find: ')
                s_flag = input("Do you want to look for separate words y/n: ")
                ta.set_list_of_lines()  # Ensure lines are set before searching
                ta.set_search_phrase_lines(s_phrase, s_flag.lower() == 'y')
                sfl = ta.get_search_phrase_lines()
                number = int(
                    input('Enter the number of line results you want to print to the terminal: '))
                print_results('Lines with searched phrase:', sfl[:number])
            elif opt == 6:
                ta.set_number_of_searched_phrases()
                nosp = ta.get_number_of_searched_phrases()
                print(
                    f'The number of occurences of the searched phrases is {nosp}')
            elif opt == 7:
                most_frequent_words = ta.get_most_frequent_words()
                print(f"Most frequent words: {most_frequent_words}")
            elif opt == 8:
                longest_words = ta.get_longest_words()
                print(f"Longest words: {longest_words}")
            elif opt == 9:
                print('Saving the report to a textfile ...')
                ta.write_search_phrase_lines_to_file(report_file_path)
                print(
                    f"Lines with searched phrase written to {report_file_path}")

            elif opt == 10:
                ta.write_search_phrase_info_to_db(db_file_path)
                print(
                    f"Search phrase info written to database at {db_file_path}")
        except ValueError as err:
            print(f"You didn't choose the valid option. {err}")
        except FileNotFoundError as err:
            print(f"Wrong filepath. {err}")
        except Exception as err:
            print("Something went wrong :(")
        else:
            print(f"Done :)")
else:
    print("There is no text!!")
