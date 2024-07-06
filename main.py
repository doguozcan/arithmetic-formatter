def check_number(number):
    if not number.isdigit():
        return "Error: Numbers must only contain digits."
    if len(number) > 4:
        return "Error: Numbers cannot be more than four digits."

    return None


def arithmetic_arranger(problems, show_answers=False):
    lines = [[], [], [], []]

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        a, operation, b = problem.split(" ")
        check_a = check_number(a)

        if check_a:
            return check_a

        if operation != "+" and operation != "-":
            return "Error: Operator must be '+' or '-'."

        check_b = check_number(b)

        if check_b:
            return check_b

        width = max(len(a), len(b)) + 2
        lines[0].append(" " * (width - len(a)) + a)
        lines[1].append(operation + " " * (width - len(b) - 1) + b)
        lines[2].append("-" * width)

        if show_answers:
            if operation == "+":
                answer = int(a) + int(b)
            else:
                answer = int(a) - int(b)

            lines[3].append(" " * (width - len(str(answer))) + str(answer))

    result = (
        "    ".join(lines[0])
        + "\n"
        + "    ".join(lines[1])
        + "\n"
        + "    ".join(lines[2])
    )

    if show_answers:
        result += "\n" + "    ".join(lines[3])

    return result


print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
