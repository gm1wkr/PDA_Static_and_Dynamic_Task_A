### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# Constructor method is missing. No instance variables have been created. 


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# Line 27 'dif' should be 'def'.  
# A comma is missing in the argument list (self, card1, card2)
  dif highest_card(self, card1 card2):
  # Incorrect Indentation.  The if/esle block (lines 29::32) should be indented to be within the Def block.
  if card1.value > card2.value:
    # Line 31 referes to card, no card has been passed in.  Should be 'card1'
    return card
  else:
    return card2
  

# Incorrect Indendation.  The whole 'def' block should be indented to be within class CardGame.  This would cause an error as 'self' is passed as the first property.
def cards_total(self, cards):
  # the variable total has not been given a value, total is, therefore, not defined.  
  total
  for card in cards:
    total += card.value
    # return should be outwith the for loop, currently it will return on the first iteration of the loop and return to the calling function.
    return "You have a total of" + total
  
```
