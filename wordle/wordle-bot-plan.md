Find word that tries to half remaining words left   

Given frequency of each letter in each position (0-4), find the letter that is closest to representing half of all occurences.  
This will almost always be the largest number, but each value is weighted based on how close it is to representing half of the available occurances.  

Count through each word find its sum, choose highest.

First few guesses should try to avoid double letters

## Bot comments

Seeing the need to take into account where yellow letters will not be, a new solution might be to prune occurance dictionary with each new information  

I.e. a grey will remove all of said letters from dict, but a yellow will only remove it from said spot.   

Then when searching for a new word, the list is read, and if a letter then does not show up in the dict, the word is not valid. Will have to loop entire list for every guess, but will be a lot simpler to program and speed is not quintessential for this project regardless. Potentially could load entire words dictionary to memory and prune as words become unavailable such that impossible words are only checked once   

Better solution:  
Given a guess, and returned state. Remove from local dictionary grey letters, and if green only let green letters remain and any yellows one simply removes the letter from that place   
