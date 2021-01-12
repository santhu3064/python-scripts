
Inspired from real-world Brainf**k, we want to create an interpreter of that language which will support the following instructions:

> increment the data pointer (to point to the next cell to the right).
< decrement the data pointer (to point to the next cell to the left).
+ increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
- decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
. output the byte at the data pointer.
, accept one byte of input, storing its value in the byte at the data pointer.
[ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
The function will take in input...

the program code, a string with the sequence of machine instructions,
the program input, a string, eventually empty, that will be interpreted as an array of bytes using each character's ASCII code and will be consumed by the , instruction
... and will return ...

the output of the interpreted code (always as a string), produced by the . instruction.
Implementation-specific details for this Kata:

Your memory tape should be large enough - the original implementation had 30,000 cells but a few thousand should suffice for this Kata
Each cell should hold an unsigned byte with wrapping behavior (i.e. 255 + 1 = 0, 0 - 1 = 255), initialized to 0
The memory pointer should initially point to a cell in the tape with a sufficient number (e.g. a few thousand or more) of cells to its right. For convenience, you may want to have it point to the leftmost cell initially
You may assume that the , command will never be invoked when the input stream is exhausted
Error-handling, e.g. unmatched square brackets and/or memory pointer going past the leftmost cell is not required in this Kata. If you see test cases that require you to perform error-handling then please open an Issue in the Discourse for this Kata (don't forget to state which programming language you are attempting this Kata in).
ALGORITHMSINTERPRETERSESOTERIC LANGUAGES

powered by

Solution:
1
def brain_luck(code, program_input):
2
    pass
Sample Tests:
1
# Echo until byte(255) encountered
2
Test.assert_equals(
3
  brain_luck(',+[-.,+]', 'Codewars' + chr(255)),
4
  'Codewars'
5
);
6
​
7
# Echo until byte(0) encountered
8
Test.assert_equals(
9
  brain_luck(',[.[-],]', 'Codewars' + chr(0)),
10
  'Codewars'
11
);
12
​
13
# Two numbers multiplier
14
Test.assert_equals(
15
  brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)),
16
  chr(72)
17
)


from collections import defaultdict

def brain_luck(code, input):
    p, i = 0, 0
    output = []
    input = iter(input)
    data = defaultdict(int)
      while i < len(code):
        c = code[i]
        if c == '+': data[p] = (data[p] + 1) % 256
        elif c == '-': data[p] = (data[p] - 1) % 256
        elif c == '>': p += 1
        elif c == '<': p -= 1
        elif c == '.': output.append(chr(data[p]))
        elif c == ',': data[p] = ord(next(input))
        elif c == '[':
            if not data[p]:
                depth = 1
                while depth > 0:
                    i += 1
                    c = code[i]
                    if c == '[': depth += 1
                    elif c== ']': depth -= 1
        elif c == ']':
            if data[p]:
                depth = 1
                while depth > 0:
                    i -= 1
                    c = code[i]
                    if c == ']': depth += 1
                    elif c == '[': depth -= 1
        i += 1
    return ''.join(output)

