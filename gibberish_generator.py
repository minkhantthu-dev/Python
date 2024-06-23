words = ['apple', 'orange', 'lemon'];
from random import randint;
def randomSentenceGenerator(word):
    randomIndex = randint(0,len(words)-1)
    return f'{words[randomIndex]} {word}'

with open('./hi.txt') as file:
          paragraph = file.read();
          wordLists = paragraph.split()          #change list
          sentenceList=list(map(randomSentenceGenerator,wordLists))
          
          paraCout = int(input('Paragraph count: ')) #3
          for count in range(paraCout) :
              with open('./generator.txt' ,'a') as write_file:
                  write_file.write(''.join(sentenceList)+'\n\n')
          
          