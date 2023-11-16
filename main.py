input_file = open("input.txt", "r", encoding='utf-8')
output_file = open("domane.txt", "w", encoding='utf-8')

score = -1
counter = 1
for line in input_file:
    if line[0] == '_':
        line = line.strip()
        question = line[1:-1]
        n_corr = int(line[-1])
        if n_corr > 1:
            score = 100/n_corr
        output_file.write(f"// question: {counter}  name: {question}\n")
        output_file.write(f"::{question}::[html]<p><strong>{question}</strong></p>"+'{\n')
        counter += 1
    elif line[0] == '*':
        correct_answer = line[1:]
        if score != -1:
            output_file.write(f"\t~%{score:.5f}%[moodle]")
            output_file.write(f"{correct_answer}")
        else:
            output_file.write(f"\t=[moodle]{correct_answer}")
    elif line[0] == '-':
        wrong_answer = line[1:]
        output_file.write(f"\t~[moodle]{wrong_answer}")
    elif line[0] == '#':
        feedback = line[1:]
        output_file.write(f"\t####[moodle]{feedback}")
    elif line[0] == '%':
        output_file.write("}\n\n")
        score = -1

