import os
import webbrowser
import sys
import re   # for split using multiple delimiters
import imdb   # IMDBPY lib
import msvcrt 
from imdb import IMDb, IMDbError

#get keypress character
def get_char():
  flag = True
  while(flag):
    if msvcrt.kbhit():
      u_key = msvcrt.getch()
      key = u_key.encode('ascii','ignore')
      print key
      flag = False

  return key

#Get specific movie detais
def get_details (movie):
  "Print the specified details of the given movie"
  print movie['title']
  url = "http://www.imdb.com/title/tt" + movie.movieID + "/"
  print "Input your option: \n\r\
P : Plot,  \
C : Cast,  \
R : Rating,  \
D : Director,  \
T : Runtime,  \
W : Web Page,  \
E : Exit \n"
  #usr_input = raw_input()
  usr_input = get_char()
  print "input = ", usr_input
  while (usr_input.lower() != 'e'):
          if (usr_input.lower() == 'p'):
                  #print "Show Plot\n"
                  print  movie['plot'][0].encode('ascii','ignore')
                  usr_input = ''
          elif (usr_input.lower() == 'c'):
                  #print "Show cast\n"
                  for actor in movie['cast']:
                          print actor['name']
                  usr_input = ''
          elif (usr_input.lower() == 'r'):
                  #print "Show Rating\n"
                  print movie['rating']
                  usr_input = ''
          elif (usr_input.lower() == 'd'):
                  #print "Show Director"
                  for ppl in movie['director']:
                          print ppl['name']
                  usr_input = ''
          elif (usr_input.lower() == 't'):
                  #print "Show run time"
                  print movie['runtime'][0].encode('ascii','ignore')
                  usr_input = ''
          elif (usr_input.lower() == 'w'):
                  #print "Go to Web Page\n"
                  webbrowser.open(url,2)
                  usr_input = ''
          else:
                  #usr_input = raw_input()
                  usr_input = get_char()

  return

#main()
query = sys.argv[1]
#query = "Two and Half Men - Season 2 - ep  (3)"
#query = "safe house - 1998"

#split on "\" or "/" to get full title(file) name
cuts_full = query.split('\\')
title_full = cuts_full[-1]

#again split on "-" to get movie or series name
cuts = title_full.split('-')
title = cuts[0]
print "title is", title, "\n"

#search on IMDB for title
access = imdb.IMDb()
title_list = access.search_movie(title.rstrip())    #strip new line from title before passing to imdb
title_first = title_list[0]
kind = title_first['kind']

searchMovie = re.search( r'movie',kind)
if searchMovie:
  #print title_first, "is a movie\n"
  #print every movie retuend by search_movie
  count = 0
  year_matched = 0
  year = 0
  #print "Split cuts =", len(cuts), "\n"
  if len(cuts) > 1:
    year = (re.search(r'\d+',cuts[1]))
    year = int(year.group(0))
    print "Movie year :", year, "\n"
  for item in title_list:
    count += 1
    if item.has_key('year'):
      print count, " - ", item['title'], " - ", item['year']
      if (year != 0) & (year == int(item['year'])):
        selected = count
        year_matched = 1
        break
    else:
      print count, " - ", item['title']
  if (not year_matched):
    selected = raw_input('Enter the movie number from the list - ')
  e = title_list[int(selected) - 1]
  access.update(e)
  get_details(e)
else:
  #print title_first, "is a series\n"
  #print len(cuts)
  if len(cuts) < 2:
    print "File name does not have Season or Episode details <name> - <season> - <ep>\n"
  season = re.findall(r'\d+', cuts[1])
  ep = re.findall(r'\d+',cuts[2])
  #print "Season -", season, " Ep -", ep, "\n"
  access.update(title_first, 'episodes')
  e = title_first['episodes'][int(season[0])][int(ep[0])]
  access.update(e)
  get_details(e)

print "Good Bye!!"
#raw_input('input something')
