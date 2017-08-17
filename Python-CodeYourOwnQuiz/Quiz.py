'''CODE YOUR OWN QUIZ'''

#Welcome player and promt what levels they want to play
print 'Welcome to our fun quiz'
print 'Through this quiz we will improve your knowledge about my country Vietnam in 3 categories: Cities, Food, and Tradtions. by typing your answer in each blank space of the paragraph provided.\n'
print 'First, choose your level you want to play:\n'
print 'Easy, Medium, or Hard'

#Prompt user level they want to play
quiz_levels =['easy', 'medium', 'hard']
level = None

while level not in quiz_levels:
  level = (raw_input('Choose level: Easy, Medium or Hard -> ').lower())

def level_value(level):
  """
  What code does: Assigns the chosen level to a numerical value
  Input: The chosen level
  Output: The level number
  """
  if level == 'easy':
    level = 1
    return level
  if level == 'medium':
    level = 2
    return level
  if level == 'hard':
    level = 3
    return level

level = level_value(level)

import random

def level_choice(level):
  """
  What code does: Given the level user has chosen, this method randomly pick 1 of the 3 paragraphs that exist for each level and also returns the
            list of missing words that corresponds to the paragraph
  Input: level number from user input
  Output: returns quiz with blanks spaces and answers
  """
  easy_quiz = 1
  medium_quiz = 2
  hard_quiz = 3
  #easy quiz
  easy_parapraph_1 = '''Ho Chi Minh City, formerly named and still informally known as ___1___, is the largest city in Vietnam by population. It was once known as
                    Prey Nokor prior to annexation by the ___2___ in the 17th century. Under the name Saigon, it was the capital of the ___3___ colony of Cochinchina
                    and later of the independent republic of South Vietnam 1955-75. On 2 July 1976, Saigon merged with the surrounding Gia Dinh Province and was officially renamed
                    Ho Chi Minh City after revolutionary ___4___ Ho Chi Minh.'''
  easy_answers_1 = ['saigon','vietnamese','french','leader']

  easy_parapraph_2 = '''Hanoi is the ___1___ of Vietnam and the country's second largest by population. Its populatino in 2009 was estimated at 2.6 million for urban districs and 7 millionfor the
                    ___2___ jurisdistion. The population in 2015 was estimated at 7.7 million people. From 1010 until 1802, it was the most important ___3___ centre of Vietnam. It was
                    eclipsed by Hue, the ___4___ capital of Vietnam during the Nguyen Dynasty, but Hanoi served as the capital of French Indochina from 1902 to 1954.'''
  easy_answers_2 = ['capital','metropolitan','political','imperial']

  easy_parapraph_3 = '''Da Nang is the ___1___ largest city in Vietnam after Hochiminh city and Hanoi in terms of urbanization and ___2___ and one of
                    the major port cities, in addition to Ho Chi Minh City, Hanoi and Hai Phong. Situated on the ___3___ of the South China Sea, at
                    the opening end of the Han River, it is the biggest city in ___4___ Vietnam. It is governed as one of the five direct-controlled
                    municipalities of the SRV and is thus under direct administration of the central government.'''
  easy_answers_3 = ['third','economic','coast','central']

  #medium quiz
  medium_parapraph_1 = '''Pho is a Vietnamese ___1___ soup consisting of ___2___, rice noodles called banh pho, a few herbs, and meat, primarily made with either
                        ___3___ or chicken. Pho is a popular ___4___ food in Vietnam and the specialty of a number of restaurant chains around the world'''
  medium_answers_1 = ['noodle','broth','beef','street']

  medium_parapraph_2 = '''Bun bo Hue is a popular Vietnamese soup containing rice ___1___ and beef. Hue is a city in central Vietnam associated with the cooking
                        style of the former ___2___ court. The dish is greatly admired for its balance of ___3___, sour, salty and sweet flavors and the predominant
                        flavor is that of ___4___ grass. Compared to pho, the noodles are thicker and more cylindrical'''
  medium_answers_2 = ['vermicelli','royal','spicy','lemon']

  medium_parapraph_3 = '''Mi Quang is a Vietnamese noodle dish that originated from Quang Nam ___1___ in central Vietnam. In the region, it is one of the most popular and ___2___
                        recognized food item, and served on various occasions such as at family parties, death anniversaries, and ___3___. Mi Quang can also be found in many restaurants
                        around the country, and is a popular ___4___ item'''
  medium_answers_3 = ['province','nationally','tet','lunch']

  #hard quiz
  hard_parapraph_1 = '''___1___ or Vietnamese New Year, is the most important celebration in Vietnamese culture. The word is a shortened form of Tet Nguyen Dan, which is Sino-Vietnamese for "Feast of the First Morning of the First Day".
                    Tet celebrates the arrival of ___2___ based on Vietnamese calendar, which usually has the date falling in January or February. Vietnamese people celebrate Lunar New Year annual which based on Lunar Calendar.
                    Tet is generally celebrated on the same day as ___3___ New Year, except when the one-hour time difference between Vietnam and China results in new moon occuring on different days. It takes place from the first day
                    of the first month of the Vietnamese calendar until at least the ___4___ day.'''
  hard_answers_1 = ['tet','spring','chinese','third']

  hard_parapraph_2 = '''The Mid-Autumn Festival is a ___1___ festival celebrated by ethnic Chinese and Vietnamese people. The festival is held on the ___2___ day of the 8th month of the lunar calendar with full moon at night,
                    corresponding to late September to early October of the Gregorian calendar with full moon at night. The festival was a time to enjoy successful reaping of rice and ___3___ with food offerings made in honor of the moon.
                    Today, it is still an occasion for outdoor reunions among friends and relatives to eat mooncakes and watch the moon, a symbol of ___4___ and unity.'''
  hard_answers_2 = ['harvest','15th','wheat','harmony']

  hard_parapraph_3 = '''Tally card songs, is an ___1___ genre of chamber music featuring female vocalists, with origins in ___2___ Vietnam. For much of its history, it was associated with a geisha-like form of entertainment,
                    which combined entertaining ___3___ people as well as performing religious songs for the royal court. Along with efforts to preserve the genre, ca tru has been appearing in much of recent Vietnamese
                    pop ___4___, including movies such as the award-winning film Me thao: thoi vang bong, or its mention during popular entertainment shows as Paris by Night.'''
  hard_answers_3 = ['ancient','northen','wealthy','culture']

  if level == easy_quiz: #If the choice is level 1, randomly choose one of the three paragraphs. And return the paragraph. And the missing words.
    return random.choice( [(easy_parapraph_1,easy_answers_1), (easy_parapraph_2,easy_answers_2), (easy_parapraph_3,easy_answers_3)] )

  if level == medium_quiz: #If the choice is level 2, randomly choose one of the three paragraphs. And return the paragraph. And the missing words.
    return random.choice( [(medium_parapraph_1,medium_answers_1), (medium_parapraph_2,medium_answers_2), (medium_parapraph_3,medium_answers_3)] )

  if level == hard_quiz: #If the choice is level 3, randomly choose one of the three paragraphs. And return the paragraph. And the missing words.
    return random.choice( [(hard_parapraph_1,medium_answers_1), (hard_parapraph_2,medium_answers_2), (hard_parapraph_3,medium_answers_3)] )



def check_word(blanks, words):
  """
  What code does: Check if the word filled in by the user matching the missing word in the paragraph
  Input: The number of blanks and the word to check
  Output: Indicates if the word corresponds to the blank space or not
  """
  space = 1
  paragraph_blanks = blanks + space #paragraph_blanks is a temporary variable to help identify what white space the user is trying to reach.
  str(paragraph_blanks)
  #Prompts the user to type the word
  missing_words = raw_input('\nType in your answer for __%d__?...: ' %paragraph_blanks).lower() #lower case allow to transfrom any capital letter from user input, therefore it can be check with blank space
  #Verifies that the word chosen by the user matches the respective blank space.
  if missing_words == words:
    #If yes, return True
    return True
  else:
    #If no, return False
    return False

def count_blanks(blanks): #Add one more blank to count
  one_blank_value = 1
  blanks += one_blank_value
  return blanks

#Main function of the game
def play(level):
  """
  What code does: Main function responsible for fetching the paragraph that will serve to play,
              counting the remaining blanks and tell if user win or not.
  Input: The level chosen by the user
  Output: The number of user blanks
  """
  blanks = 0 #Start the assigned variable blanks from 0.
  paragraph_and_answer = level_choice(level) #After the user choose level want to play, calls the level_choice function to get the paragraph and missing answers.
  paragraph = paragraph_and_answer[0].split() #Separates paragraph from words and assigns paragraph to variable paragraph
  answers = paragraph_and_answer[1] #Separates the words and assigns words to variable words
  paragraph_with_answer = ' '.join(paragraph) #The variable paragraph_with_answer serves to print the paragraph to the screen in a string format for a better visualization of the user.

  while check_remaining_blanks(blanks): #if blanks < 4, the game runs.
      space = 1
      paragraph_blanks = str(blanks+space)
      print paragraph_with_answer #print the paragraph to the screen in a string format for a better visualization of the user.
      word_position = answers[blanks]
      if check_word(blanks, word_position): #Checks with the help of the check Word function, taking into account the blanks already obtained by the user which word to discover in the paragraph.
        print "\nGreat answer! Keep going!\n"
        paragraph_with_answer = paragraph_with_answer.replace('___%s___'%paragraph_blanks, word_position) ##If the user blanks the missing words, the paragraph appears with the blanks filled as the user blanks.
        blanks = count_blanks(blanks)
  game_result(blanks) #Taking into account the blanks, verifies if the user won by calling the game_result function.


def check_remaining_blanks(blanks): #Check remaining blanks in paragraph
  """
  Input: the number of blanks
  Output: True(still have blanks) or False(no blanks)
  """
  total_blanks = 4
  if blanks < total_blanks:
    return True
  else:
    return False

def game_result(blanks): #Check if user has hit all 4 blanks in paragraph
  """
  Input: the number of blanks
  Output: Win or try again.
  """
  limit_blanks = 4
  if blanks == limit_blanks:
    print '\n Awesome! you win! \n'
  else:
    print '\n Try again! \n'

play(level)
