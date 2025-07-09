def grep(pattern, flags, files):
    
    case_insensitive = "-i" in flags
    invert_match = "-v" in flags
    match_entire_line = "-x" in flags

    multiple_files = len(files) > 1
    results = []

    for file in files:
        results.extend(
            process_file(
                file, pattern, flags, case_insensitive, match_entire_line, invert_match, multiple_files
            )
        )

    return "".join(results)

def match_line(line, pattern, case_insensitive, match_entire_line, invert_match):
    line_to_check = line.strip()

    if case_insensitive:
        pattern = pattern.lower()
        line_to_check = line_to_check.lower()

    if match_entire_line:
        is_match = line_to_check == pattern
    else:
        is_match = pattern in line_to_check

    return not is_match if invert_match else is_match

def format_result(file, line_number, line, flags, multiple_files):
    if "-l" in flags:
        return f"{file}\n"
    elif "-n" in flags:
        return (
            f"{file}:{line_number}:{line.strip()}\n"
            if multiple_files
            else f"{line_number}:{line.strip()}\n"
        )
    else:
        return f"{file}:{line.strip()}\n" if multiple_files else f"{line.strip()}\n"

def process_file(
    file, pattern, flags, case_insensitive, match_entire_line, invert_match, multiple_files
):
    results = []
    with open(file, "r") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        if match_line(line, pattern, case_insensitive, match_entire_line, invert_match):
            result = format_result(file, line_number, line, flags, multiple_files)
            if "-l" in flags:
                return [result]
            results.append(result)

    return results