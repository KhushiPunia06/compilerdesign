import re

# Token types
TOKEN_INT = "INT"
TOKEN_FLOAT = "FLOAT"
TOKEN_ID = "ID"
TOKEN_KEYWORD = "KEYWORD"
TOKEN_OPERATOR = "OPERATOR"
TOKEN_SEPARATOR = "SEPARATOR"

# Regular expressions for token recognition
patterns = [
    (TOKEN_INT, r'\d+'),
    (TOKEN_FLOAT, r'\d+\.\d+'),
    (TOKEN_ID, r'[a-zA-Z_]\w*'),
    (TOKEN_KEYWORD, r'(if|else|while|for|return|function|int|float|bool|void|var)'),
    (TOKEN_OPERATOR, r'(\+|\-|\*|\/|=|==|!=|<|>|<=|>=)'),
    (TOKEN_SEPARATOR, r'(\(|\)|\{|\}|\[|\]|\,|\;)')
]

def tokenize(input_text):
    tokens = []
    position = 0
    while position < len(input_text):
        match = None
        for token_type, pattern in patterns:
            regex = re.compile(pattern)
            match = regex.match(input_text, position)
            if match:
                value = match.group(0)
                if token_type != TOKEN_KEYWORD:
                    tokens.append((token_type, value))
                position = match.end()
                break
        if not match:
            # If no match is found, raise an error or skip the unrecognized character
            raise Exception(f"Unrecognized character at position {position}: '{input_text[position]}'")
    return tokens

def count_tokens(tokens):
    return len(tokens)

def get_keywords(tokens):
    return [token[1] for token in tokens if token[0] == TOKEN_KEYWORD]

def get_operators(tokens):
    return [token[1] for token in tokens if token[0] == TOKEN_OPERATOR]

def get_identifiers(tokens):
    return [token[1] for token in tokens if token[0] == TOKEN_ID]

def get_literals(tokens):
    return [token[1] for token in tokens if token[0] in (TOKEN_INT, TOKEN_FLOAT)]

def get_statements(tokens):
    statements = []
    current_statement = []
    for token in tokens:
        current_statement.append(token)
        if token[0] == TOKEN_SEPARATOR and token[1] == ';':
            statements.append(current_statement)
            current_statement = []
    return statements

def get_line_numbers(tokens):
    line_numbers = []
    current_line_number = 1
    for token in tokens:
        line_numbers.append(current_line_number)
        if token[1] == '\n':
            current_line_number += 1
    return line_numbers

# Example usage
if _name_ == "_main_":
    code = """
    int x = 42;
    float y = 3.14;
    if (x > 10) {
        print("x is greater than 10");
    } else {
        print("x is not greater than 10");
    }
    """
    tokens = tokenize(code)
    print(f"Token count: {count_tokens(tokens)}")
    print(f"Keywords: {get_keywords(tokens)}")
    print(f"Operators: {get_operators(tokens)}")
    print(f"Identifiers: {get_identifiers(tokens)}")
    print(f"Literals: {get_literals(tokens)}")
    statements = get_statements(tokens)
    for i, statement in enumerate(statements, start=1):
        print(f"Statement {i}: {statement}")
    line_numbers = get_line_numbers(tokens)
    print(f"Line numbers: {line_numbers}")