from data_structure.stack_queue.bracket_balanced import Stack,Balanced_brackets


def test_balanced_bracket():
    bracket1="{}"
    resultBracket=True
    assert Balanced_brackets(bracket1)==resultBracket


def test_balanced_bracket2():
    bracket1="{}(uuu)kik{}"
    resultBracket=True
    assert Balanced_brackets(bracket1)==resultBracket

def test_balanced_bracket3():
    bracket1="[({}]"
    resultBracket=False
    assert Balanced_brackets(bracket1)==resultBracket

