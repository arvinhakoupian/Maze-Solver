from vector import Vector


def parse_tokens(line):
    tokens = Vector(4)
    n = len(line)
    i = 0

    while i < n:
        while i < n and line[i].isspace():
            i += 1
        if i >= n:
            break

        if line[i] == '"':
            i += 1
            start = i
            while i < n and line[i] != '"':
                i += 1
            token = line[start:i]
            tokens.append(token)
            if i < n and line[i] == '"':
                i += 1
        else:
            start = i
            while i < n and not line[i].isspace():
                i += 1
            tokens.append(line[start:i])

    return tokens
