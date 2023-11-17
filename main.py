import os

input_file = open("input.txt", "r", encoding='utf-8')
output_file = open("domande.txt", "w", encoding='utf-8')

score = -1
counter = 1
line_counter = 0
separator = True
for line in input_file:
    line_counter += 1
    if line[0] == '_':                  # question case
        if separator:                   # check if there is a separator before current question
            separator = False           # set separator to False for future checks
            line = line.strip()
            question = line[1:-1]

            if question[-1] == ':':     # add a space if there's a : as last character to avoid import errors
                question = question + " "

            if not line[-1].isdigit():  # check if there's the number of correct answers
                print(f"Error, number of correct answers missing at the line: {line_counter}")
                output_file.close()
                os.remove("domande.txt")
                break
            n_corr = int(line[-1])

            if n_corr > 1:              # divide the score by the number of correct answers
                score = 100 / n_corr
            output_file.write(f"// question: {counter}  name: {question}\n")
            output_file.write(f"::{question}::[html]<p><strong>{question}</strong></p>" + '{\n')
            counter += 1

        else:
            print(f"Error, missing separator before line: {line_counter}")
            output_file.close()
            os.remove("domande.txt")
            break

    elif line[0] == '*':                # right answer case
        correct_answer = line[1:]
        if score != -1:
            output_file.write(f"\t~%{score:.5f}%[moodle]{correct_answer}")
        else:
            output_file.write(f"\t=[moodle]{correct_answer}")

    elif line[0] == '-':                # wrong answer case
        wrong_answer = line[1:]
        output_file.write(f"\t~[moodle]{wrong_answer}")

    elif line[0] == '#':                # feedback answer case
        feedback = line[1:]
        output_file.write(f"\t####[moodle]{feedback}")

    elif line[0] == '+':                # t/f answer case
        answer = line[1]
        if answer == 'T':
            output_file.write(f"\tTRUE\n")
        elif answer == 'F':
            output_file.write(f"\tFALSE\n")
        else:
            print()

    elif line[0] == '%':                # end of question case
        output_file.write("}\n\n")
        separator = True
        score = -1

    else:
        if len(line.strip()) > 0:       # case of formatting error, only if not empty line
            print(f"Error formatting the line file {line_counter}\n\t{line}")
            os.remove("domande.txt")
            break
