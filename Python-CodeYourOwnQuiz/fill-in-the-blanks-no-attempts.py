'''CODE YOUR OWN QUIZ'''
print 'Welcome to our fun quiz'

import random

def choose_level(level):
  """
  Behavior: Taking into account the user's choice of level, this method randomly chooses 1 of the 3 texts that exist for each level and also returns the
            list of missing words that corresponds to the text
  Input: the number of the level
  Output: returns text with blanks spaces and list of missing words in tuple format
  """
  easy_level = 1
  medium_level = 2
  hard_level = 3
  #level easy
  easy_text_a = """Rome has the status of a global city. ___1___ ranked in 2016 as the 13th-most-visited city in the world, 3rd most visited in the European Union,
                   and the most popular tourist attraction in ___2___. Its historic centre is listed by ___3___ as a World Heritage Site.
                   Monuments and museums such as the Vatican Museums and the Colosseum are among the world's most visited tourist destinations with both locations receiving
                   millions of tourists a year. Rome hosted the ___4___ Summer Olympics and is the seat of United Nations' Food and Agriculture Organization (FAO)."""
  easy_answers_a = ["ROME","ITALY","UNESCO","1960"]

  easy_text_b = """Prague is the capital and largest city of the ___1___ Republic. It is the 14th largest city in the European Union.
                   It is also the historical capital of ___2___. Situated in the north-west of the country on the ___3___ river, the city is home to about 1.26 million people,
                   while its larger urban zone is estimated to have a population of nearly 2 million. The city has a temperate climate, with warm summers and chilly ___4___."""
  easy_answers_b = ["CZECH","BOHEMIA","VLATAVA","WINTERS"]

  easy_text_c = """Lisbon is the capital and the largest city of ___1___, with a population of 552,700 within its administrative limits in an area of 100.05 km square.
                   Its urban area extends beyond the city's administrative limits with a population of around 2.7 million people,
                   being the 11th-most populous urban area in the ___2___ Union. About 2.8 million people live in the Lisbon Metropolitan Area (which represents approximately 27 per cent
                   of the country's population). It is continental Europe's westernmost capital city and the only one along the ___3___ coast.
                   Lisbon lies in the western Iberian Peninsula on the Atlantic Ocean and the River ___4___. The westernmost areas of its metro area is the westernmost point of Continental
                   Europe."""
  easy_answers_c = ["PORTUGAL","EUROPEAN","ATLANTIC","TAGUS"]
  #level medium
  medium_text_a = """Beginning with the Renaissance, almost all the popes since Nicholas V (1447-55) pursued coherently along four ___1___ years an architectonic and urbanistic
                     programme aimed to make of the city the worlds artistic and ___2___ centre. Due to that, Rome became first one of the major centres of the Italian Renaissance,
                     and then the birthplace of both the ___3___ style and Neoclassicism. Famous artists, painters, sculptors and architects made Rome the centre of their activity,
                     creating masterpieces throughout the city. In 1871 Rome became the capital of the Kingdom of Italy, and in 1946 that of the Italian ___4___."""
  medium_answers_a = ["HUNDRED","CULTURAL","BAROQUE","REPUBLIC"]

  medium_text_b = """Prague has been a political, cultural, and economic centre of central Europe with waxing and waning fortunes during its history.
                     Founded during the Romanesque and flourishing by the ___1___, Renaissance and Baroque eras, Prague was the capital of the ___2___ of Bohemia and the main
                     residence of several Holy Roman Emperors, most notably of ___3___ IV (r. 1346-1378). It was an important city to the Habsburg Monarchy and its Austro-Hungarian
                     Empire. The city played major rules in the Bohemian and protestant Reformation, the Thirty Years War, and in 20th century history as the Capital of Czechoslovakia,
                     during both World Wars and the post-war ___4___ era."""
  medium_answers_b = ["GOTHIC","KINGDOM","CHARLES","COMMUNIST"]

  medium_text_c = """Lisbon is one of the oldest cities in the ___1___, and the oldest in Western Europe, predating other modern European capitals such as London,
                     Paris and Rome by centuries. Julius Caesar made it a municipium called Felicitas Julia, adding to the name ___2___.
                     Ruled by a series of Germanic tribes from the 5th century, it was captured by the Moors in the 8th century. In 1147, the Crusaders under ___3___
                     Henriques reconquered the city and since then it has been a major political, economic and cultural centre of Portugal. Unlike most capital cities, Lisbon's
                     status as the ___4___ of Portugal has never been granted or confirmed officially - by statute or in written form. Its position as the capital has formed through
                     constitutional convention, making its position as de facto capital a part of the Constitution of Portugal."""
  medium_answers_c = ["WORLD","OLISSIPO","AFONSO","CAPITAL"]
  #level hard
  hard_text_a = """Rome is the principal town of the Metropolitan ___1___ of Rome, operative since 1 January 2015. The Metropolitan City replaced the old province,
                   which included the city's metropolitan area and extends further north until Civitavecchia. The Metropolitan City of Rome is the ___2___ by area in Italy.
                   At 5,352 square kilometres (2,066 sq mi), its dimensions are ___3___ to the region of liguria. Moreover, the city is also the capital of the ___4___ region."""
  hard_answers_a = ["CITY","LARGEST","COMPARABLE","LAZIO"]

  hard_text_b = """The oldest part of the ___1___, the mechanical clock and astronomical dial, dates back to 1410 when it was made by clockmaker Mikulas of Kadan and Jan Sindel,
                   then later a professor of mathematics and astronomy at ___2___ University. The first recorded mention of the clock was on 9 October 1410. Later,
                   presumably around 1490, the ___3___ dial was added and the clock facade was decorated with ___4___ sculptures."""
  hard_answers_b = ["ORLOJ","CHARLES","CALENDAR","GOTHIC"]

  hard_text_c = """Most of the Portuguese expeditions of the Age of Discovery left Lisbon during the period from the end of the 15th century to the beginning of the 17th century,
                   including ___1___ da Gama's expedition to ___2___ in 1498. In 1506, 3,000 Jews were massacred in Lisbon. The 16th century was Lisbon's golden era:
                   the city was the European hub of commerce between Africa, India, the Far East and later, Brazil, and acquired great riches by exploiting the trade in spices,
                   slaves, sugar, textiles and other goods. This period saw the rise of the exuberant ___3___ style in architecture, which left its mark in many 16th century
                   monuments (including Lisbon's Belem Tower and Jeronimos Monastery, which were declared ___4___ World Heritage Sites). A description of Lisbon in the 16th century
                   was written by Damiao de Gois and published in 1554."""
  hard_answers_c = ["VASCO","INDIA","MANUELINE","UNESCO"]

  if level == easy_level: #If the choice is level 1, randomly choose one of the three texts. And return the text. And the missing words.
    return random.choice( [(easy_text_a,easy_answers_a), (easy_text_b,easy_answers_b), (easy_text_c,easy_answers_c)] )

  if level == medium_level: #If the choice is level 2, randomly choose one of the three texts. And return the text. And the missing words.
    return random.choice( [(medium_text_a,medium_answers_a), (medium_text_b,medium_answers_b), (medium_text_c,medium_answers_c)] )

  if level == hard_level: #If the choice is level 3, randomly choose one of the three texts. And return the text. And the missing words.
    return random.choice( [(hard_text_a,medium_answers_a), (hard_text_b,medium_answers_b), (hard_text_c,medium_answers_c)] )

def check_word(hits, words):
  """
  Behavior: Verifies that the word chosen by the user, matches the missing word in the text
  Input: The number of hits and the word to check
  Output: Indicates if the word corresponds to the blank space or not
  """
  whitespace_value = 1
  txt_hits = hits + whitespace_value #txt_hits is a temporary variable to help identify what white space the user is trying to reach.
  str(txt_hits)
  #Prompts the user to type the word
  what_is_the_word = raw_input('\nWhat is the missing word __%d__?...: ' %txt_hits).upper() # The upper one always allows to transform the words that the user enters in capital letters and thus to correspond exactly if it hits the missing word.
  #Verifies that the word chosen by the user matches the respective blank space.
  if what_is_the_word == words:
    #If yes, return True
    return True
  else:
    #If no, return False
    return False

def play(level):
  """
  Behavior: Main function of the game, makes the whole game work. Is the function responsible for fetching the text that will serve to play,
            which checks the remaining attempts and that counts the hits of the user and thus determine the final outcome of the game.
  Input: The level and the attempts chosen by the user
  Output: The number of user hits
  """
  hits = 0 #Starts the variable hits to zero.
  phrase_and_words = choose_level(level) #Depending on the level chosen by the user, calls the choose_level function to get the text and missing words.
  phrase = phrase_and_words[0].split() #Separates text from words and assigns text to variable phrase
  words = phrase_and_words[1] #Separates the words and assigns words to variable words
  phrase_edit = ' '.join(phrase) #The variable phrase_edit serves to print the text to the screen in a string format for a better visualization of the user.

  while have_hits_to_continue(hits): #While attempts are greater than zero and hits less than four, the game runs.
      whitespace_value = 1
      txt_hits = str(hits+whitespace_value) #txt_hits is an auxiliary variable that allows to display whitespace with the correct values for the user.
      print phrase_edit #print the text to the screen in a string format for a better visualization of the user.
      word_position = words[hits]
      if check_word(hits, word_position): ##Checks with the help of the check Word function, taking into account the hits already obtained by the user which word to discover in the text.
        print "\nCongratulations! You get the word!\n"
        phrase_edit = phrase_edit.replace('___%s___'%txt_hits, word_position) ##If the user hits the missing words, the text appears with the blanks filled as the user hits.
        hits = count_hits(hits)
  game_result(hits) #Taking into account the hits, verifies if the user won by calling the game_result function.


def have_hits_to_continue(hits):
  """
  Behavior: Verifies that the player still have hits to continue
  Input: the number of hits
  Output: Indicates whether or not the player has hits to continue
  """
  hits_maximum = 4
  if hits < hits_maximum:
    return True
  else:
    return False

def count_hits(hits):
  """
  Behavior: Add one more hit to count
  Input: Total of Hits until now
  Output: Total of Hits after now
  """
  one_hit_value = 1
  hits += one_hit_value
  return hits


def game_result(hits): #This function checks if the user has hit the 4 times
  """
  Behavior: Verify if the number of hits. If the number is equal to 4, indicates that the user has won, otherwise the user has lost.
  Input: the number of hits
  Output: feedback for the user win our loose.
  """
  limit_hits = 4
  if hits == limit_hits:
    print "\n\o/ Congratulations, you won! \o/ :-)\n"

  else:
    print "\nYou loose! :-(\n"

def level_number(level):
  """
  Behavior: Assigns the chosen level to a numerical value
  Input: The chosen level
  Output: The level number
  """
  if level == 'EASY':
    level = 1
    return level
  if level == 'MEDIUM':
    level = 2
    return level
  if level == 'HARD':
    level = 3
    return level
'''
Beginning of the game
'''
# Print the game information menu
print "\nWelcome to the game!\n"
print "In this game we will test your knowledge about 3 European cities. Rome, Prague, and Lisbon.\n"
print "*" * 16
print "Choose a level:"
print "Level - easy"
print "Level - medium"
print "Level - hard"
print "*" * 16

levels_available =['EASY', 'MEDIUM', 'HARD']
level = None

while level not in levels_available:
  level = (raw_input('Choose level: Easy, Medium or Hard -> ').upper())

level = level_number(level)


play(level)
