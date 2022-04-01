#!/usr/bin/env python3
import parser.lex as lex

lex.rules = [
	{'regex': 'SELECT|select', 'action': 'SELECT', 'dfa': {'startState': 0, 'sigma': ['S', 'E', 'L', 'C', 'T', 's', 'e', 'l', 'c', 't'], 'finStates': [6, 12], 'deltaT': [[1, None, None, None, None, 7, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None], [None, 4, None, None, None, None, None, None, None, None], [None, None, None, 5, None, None, None, None, None, None], [None, None, None, None, 6, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 8, None, None, None], [None, None, None, None, None, None, None, 9, None, None], [None, None, None, None, None, None, 10, None, None, None], [None, None, None, None, None, None, None, None, 11, None], [None, None, None, None, None, None, None, None, None, 12], [None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'FROM|from', 'action': 'FROM', 'dfa': {'startState': 0, 'sigma': ['F', 'R', 'O', 'M', 'f', 'r', 'o', 'm'], 'finStates': [4, 8], 'deltaT': [[1, None, None, None, 5, None, None, None], [None, 2, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None], [None, None, None, 4, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None], [None, None, None, None, None, None, 7, None], [None, None, None, None, None, None, None, 8], [None, None, None, None, None, None, None, None]]}},
	{'regex': 'WHERE|where', 'action': 'WHERE', 'dfa': {'startState': 0, 'sigma': ['W', 'H', 'E', 'R', 'w', 'h', 'e', 'r'], 'finStates': [5, 10], 'deltaT': [[1, None, None, None, 6, None, None, None], [None, 2, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None], [None, None, None, 4, None, None, None, None], [None, None, 5, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None], [None, None, None, None, None, None, 8, None], [None, None, None, None, None, None, None, 9], [None, None, None, None, None, None, 10, None], [None, None, None, None, None, None, None, None]]}},
	{'regex': '(NATURAL|natural)\\_(JOIN|join)', 'action': 'NATJOIN', 'dfa': {'startState': 0, 'sigma': ['N', 'A', 'T', 'U', 'R', 'L', 'n', 'a', 't', 'u', 'r', 'l', ' ', 'J', 'O', 'I', 'j', 'o', 'i'], 'finStates': [12, 16], 'deltaT': [[1, None, None, None, None, None, 17, None, None, None, None, None, None, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, 8, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, 9, None, None, 13, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 10, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 11, None, None, None], [12, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 14, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 15], [None, None, None, None, None, None, 16, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 18, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 20, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 23, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, 8, None, None, None, None, None, None]]}},
	{'regex': 'DISTINCT|distinct', 'action': 'DISTINCT', 'dfa': {'startState': 0, 'sigma': ['D', 'I', 'S', 'T', 'N', 'C', 'd', 'i', 's', 't', 'n', 'c'], 'finStates': [8, 16], 'deltaT': [[1, None, None, None, None, None, 9, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None], [None, 5, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 6, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None, None, None, None, None], [None, None, None, 8, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 10, None, None, None, None], [None, None, None, None, None, None, None, None, 11, None, None, None], [None, None, None, None, None, None, None, None, None, 12, None, None], [None, None, None, None, None, None, None, 13, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 14, None], [None, None, None, None, None, None, None, None, None, None, None, 15], [None, None, None, None, None, None, None, None, None, 16, None, None], [None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'TRUE|true|FALSE|false', 'action': 'BOOL', 'dfa': {'startState': 0, 'sigma': ['T', 'R', 'U', 'E', 't', 'r', 'u', 'e', 'F', 'A', 'L', 'S', 'f', 'a', 'l', 's'], 'finStates': [4, 8, 13, 18], 'deltaT': [[1, None, None, None, 5, None, None, None, 9, None, None, None, 14, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 7, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 8, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 10, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 12, None, None, None, None], [None, None, None, 13, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, 15, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 17], [None, None, None, None, None, None, None, 18, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': '[0-9]+', 'action': 'NUMBER', 'dfa': {'startState': 0, 'sigma': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'finStates': [1, 2], 'deltaT': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]}},
	{'regex': ',', 'action': 'COMMA', 'dfa': {'startState': 0, 'sigma': [','], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\*', 'action': 'WILDCARD', 'dfa': {'startState': 0, 'sigma': ['*'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': ';', 'action': 'SEMICOLON', 'dfa': {'startState': 0, 'sigma': [';'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '>', 'action': 'GREATER', 'dfa': {'startState': 0, 'sigma': ['>'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '>=', 'action': 'GREATEREQ', 'dfa': {'startState': 0, 'sigma': ['>', '='], 'finStates': [2], 'deltaT': [[1, None], [None, 2], [None, None]]}},
	{'regex': '<', 'action': 'LESS', 'dfa': {'startState': 0, 'sigma': ['<'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '<=', 'action': 'LESSEQ', 'dfa': {'startState': 0, 'sigma': ['<', '='], 'finStates': [2], 'deltaT': [[1, None], [None, 2], [None, None]]}},
	{'regex': '\\+', 'action': 'PLUS', 'dfa': {'startState': 0, 'sigma': ['+'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\-', 'action': 'MINUS', 'dfa': {'startState': 0, 'sigma': ['-'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\*\\*', 'action': 'EXPONENT', 'dfa': {'startState': 0, 'sigma': ['*'], 'finStates': [2], 'deltaT': [[1], [2], [None]]}},
	{'regex': '/', 'action': 'DIVIDE', 'dfa': {'startState': 0, 'sigma': ['/'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '=', 'action': 'EQUALS', 'dfa': {'startState': 0, 'sigma': ['='], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '<>', 'action': 'NEQUALS', 'dfa': {'startState': 0, 'sigma': ['<', '>'], 'finStates': [2], 'deltaT': [[1, None], [None, 2], [None, None]]}},
	{'regex': '\\(', 'action': 'LPAREN', 'dfa': {'startState': 0, 'sigma': ['('], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\)', 'action': 'RPAREN', 'dfa': {'startState': 0, 'sigma': [')'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': 'AND|and', 'action': 'AND', 'dfa': {'startState': 0, 'sigma': ['A', 'N', 'D', 'a', 'n', 'd'], 'finStates': [3, 6], 'deltaT': [[1, None, None, 4, None, None], [None, 2, None, None, None, None], [None, None, 3, None, None, None], [None, None, None, None, None, None], [None, None, None, None, 5, None], [None, None, None, None, None, 6], [None, None, None, None, None, None]]}},
	{'regex': 'OR|or', 'action': 'OR', 'dfa': {'startState': 0, 'sigma': ['O', 'R', 'o', 'r'], 'finStates': [2, 4], 'deltaT': [[1, None, 3, None], [None, 2, None, None], [None, None, None, None], [None, None, None, 4], [None, None, None, None]]}},
	{'regex': 'NOT|not', 'action': 'NOT', 'dfa': {'startState': 0, 'sigma': ['N', 'O', 'T', 'n', 'o', 't'], 'finStates': [3, 6], 'deltaT': [[1, None, None, 4, None, None], [None, 2, None, None, None, None], [None, None, 3, None, None, None], [None, None, None, None, None, None], [None, None, None, None, 5, None], [None, None, None, None, None, 6], [None, None, None, None, None, None]]}},
	{'regex': '[_a-zA-Z][\\._a-zA-Z0-9]*', 'action': 'ID', 'dfa': {'startState': 0, 'sigma': ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'finStates': [1, 2], 'deltaT': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, None, None, None, None, None, None, None, None, None], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]}},
	{'regex': '[\\_\\n]', 'action': '(SKIP)', 'dfa': {'startState': 0, 'sigma': [' ', '\n'], 'finStates': [1], 'deltaT': [[1, 1], [None, None]]}},
	{'regex': '.', 'action': '(ERR) "Bad token"', 'dfa': {'startState': 0, 'sigma': ['\t', '~', '}', '|', '{', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '`', '_', '^', ']', '\\', '[', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '@', '?', '>', '=', '<', ';', ':', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '/', '.', '-', ',', '+', '*', ')', '(', "'", '&', '%', '$', '#', '"', '!', ' '], 'finStates': [1], 'deltaT': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
]
