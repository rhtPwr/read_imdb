@echo off
cls
set PATH=%PATH%;C:\Python27\
:my_loop
IF %1=="" GOTO completed
  python C:\Users\rpawar\Documents\Project\imdb\imdb_page.py %1
  SHIFT
  GOTO my_loop
:completed
