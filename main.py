import os
from tkinter import filedialog


def main():
    file_path = filedialog.askopenfilename()

    input_file = open(file_path, "r", encoding='utf-8-sig')
    output_file = open("domande.txt", "w", encoding='utf-8-sig')

    score = -1
    counter = 0
    line_counter = 0
    sep_counter = 0
    inSpecificFeedback = False
    inGenericFeedback = False
    error = False

    separator = True
    for line in input_file:
        line_counter += 1

        if line.__contains__("="):
            line = line.replace("=", "\\=")

        if line[0] == '_':  # question case
            inSpecificFeedback = False
            inGenericFeedback = False
            if separator:  # check if there is a separator before current question
                separator = False  # set separator to False for future checks
                line = line.strip()
                question = line[1:-1]
                counter += 1

                if question[-1] == ':':  # add a space if there's a : as last character to avoid import errors
                    question = question + " "

                if not line[-1].isdigit():  # check if there's the number of correct answers
                    print(f"Error, number of correct answers missing at the line: {line_counter}")
                    error = True
                    output_file.close()
                    os.remove("domande.txt")
                    break
                n_corr = int(line[-1])

                if n_corr > 1:  # divide the score by the number of correct answers
                    score = 100 / n_corr
                output_file.write(f"// question: {counter}  name: {question}\n")
                output_file.write(f"::{question}::[html]<p><strong>{question}</strong></p>" + '{\n')

            else:
                print(f"Error, missing separator before line: {line_counter}")
                error = True
                output_file.close()
                os.remove("domande.txt")
                break

        elif line[0] == '*':  # right answer case
            inSpecificFeedback = False
            inGenericFeedback = False
            correct_answer = line[1:]
            if score != -1:
                output_file.write(f"\t~%{score:.5f}%[moodle]{correct_answer}")
            else:
                output_file.write(f"\t=[moodle]{correct_answer}")

        elif line[0] == '-':  # wrong answer case
            inSpecificFeedback = False
            inGenericFeedback = False
            wrong_answer = line[1:]
            output_file.write(f"\t~[moodle]{wrong_answer}")

        elif line[0] == '#':  # feedback answer case
            feedback = line[1:]
            inSpecificFeedback = False
            if not inGenericFeedback:
                output_file.write(f"\t####[moodle]{feedback}")
                inGenericFeedback = True
            else:
                output_file.write(f"\t{feedback}")

        elif line[0] == '@':
            feedback = line[1:]
            inGenericFeedback = False
            if not inSpecificFeedback:
                output_file.write(f"\t#[moodle]{feedback}")
                inSpecificFeedback = True
            else:
                output_file.write(f"\t{feedback}")

        elif line[0] == '+':  # t/f answer case
            inSpecificFeedback = False
            inGenericFeedback = False
            answer = line[1]
            if answer == 'T':
                output_file.write(f"\tTRUE\n")
            elif answer == 'F':
                output_file.write(f"\tFALSE\n")
            else:
                print("Error, wrong answer format")
                error = True

        elif line[0] == '%':  # end of question case
            inSpecificFeedback = False
            inGenericFeedback = False
            sep_counter += 1
            output_file.write("}\n\n")
            separator = True
            score = -1

        else:
            if len(line.strip()) > 0:  # case of formatting error, only if not empty line
                print(f"Error: missing symbol indicator at line {line_counter}\n\t{line}")
                error = True
                output_file.close()
                os.remove("domande.txt")
                break

    if not error:
        if sep_counter != counter:
            print(f"You missed the last separator")
            output_file.close()
            os.remove("domande.txt")
        else:
            print(f"You just created {counter} questions")


main()
