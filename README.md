# quizgame
Explain the advantage of your design:
Easy to understand
easy add next questions
User-friendly data structures. used list of dictionaries.

Did you apply any design patterns?
The state of an object can be defined as its exact condition at any given point of time, depending on the values of its properties or attributes. The set of methods implemented by a class constitutes the behavior of its instances. Whenever there is a change in the values of its attributes, we say that the state of an object has changed.
Context
defines the interface of interest to clients.
maintains an instance of a Game subclass that defines the current state.
GameContext
defines an interface for encapsulating the behavior associated with a particular state of the Context.
Game Class define the subclasses of answer_yes subclass and answer_no subclass
each subclass implements a behavior associated with a state of the GameContext
Let's create a GameContext interface defining an action show_question and end_game. Context is a class which carries a GameState.

What was your thought process?
```
def main():
    context = Context()
    context.game = Game(context)
    context.game.Start(context).start()
    context.game = None
  ```
  main() here we have created Context object first we are calling Start methods

```
class Start:
      def __init__(self, context: GameContext):
          self.context = context
```
Class start define start of the game where the first question is called form the dictionary

class GameContext: Responsible for handling interaction with the game UI. here where the question list of dictionary is defined. It acts has a interface of the Game classes

If user input is yes AnswerYes class is called id is 0 the game will be ended endgame function is called
if id is number show question() method is called.

Same logic repeats for AnswerNo class

How easy is it to add a new question?
Simply add a dictionary to the list of dictionaries, which contains  question id yes or no. Assign id number to yes which indicates user gives the yes to which question to navigate. also assign id number to no. This all about playing with data structures.

How easy is it to add additional information about a question, for example, a picture?
If in case of adding additional information like picture just add another key to the dictionary. Make it to display in show_question() method.
