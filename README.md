# Text to Moodle script
This Python script generates a GIFT compatible file to be imported in Moodle. 
There are some syntax rules to be respected for it to work. In particular, every question must:

- start with a **"_"** (underscore) character;
- be separated by a **"%"** character. You must put it also after the very last question;
- end with a number that represents the amount of correct answers.
- correct answers must start with a **"*"** (star) character;
- wrong answer must start with a **"-"** (minus) character;

___

## Multichoice question
This kind of question can be divided into Single Correct Answer and Multi Correct Answers

### Single correct answer
In this case you have to put _**1**_ at the end of the question. Under the question, just a single answer (the correct one) has to start with "*".

### Multi choice answer
In this case you have to put the number of the correct answers at the end of the question. Again, every correct answer must start with a "*", while the wrong ones must start with the "-".

___

## True/False question
In this case you still have to put 1 at the end of the question. Under that, you have to put "+" and then _**"T"**_ if the answer is True or _**F**_ if the answer is false.

___
## Free text answer
In this case, just put "0" at the end of the question and no answers.

___

## Feedback
To add general feedback for a question, place it like a normal answer, but put "#" instad of "*" or "-" before it.

If you want to add a feedback for a specific answer, use "@" instead of "#" and place it right after the selected answer.
___

Look at the "input.txt" file to have an example. 