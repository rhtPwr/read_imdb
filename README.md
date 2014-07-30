read_imdb
=========

Windows exe to read imdb data by using file name

Has two files:
1) imdb.cmd - Windows batch file to run the imdb_page.py script on the input given
              It is supposed to be put in 'sendto' folder of windows. (Open windows exploerer. Type alt+D. Type shell:sendto at top. It will take you to sendto folder)
              imdb.cmd file needs to be modified based on where you have put the imdb_page.py script
              This allows a file name to be given to imdb_page.py script by right clicking the file name and "sendto" imdb.cmd
              
2) imdb_page.py - Python script that uses IMDbPY library to query information for the input provided "right click" on file and "sendto" imdb.cmd
                  Ask user to provide input based on data needed for that particular file.
                  Inputs supported: 
                              P : Plot
                              C : Cast 
                              R : Rating 
                              D : Director 
                              T : Runtime 
                              W : Web Page 
                              E : Exit 
