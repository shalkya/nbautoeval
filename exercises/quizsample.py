from nbautoeval import Quiz, QuizQuestion, Option, CodeOption, MathOption 

questions1 = []
### 
question_basic_multiple = QuizQuestion(
    question="Choose the right fruits<br>(several correct options)",
    options=[ 
        Option("apple", correct=True),
        Option("apricot", correct=True),
        Option("azur", correct=True),
        Option("banana"),
        Option("pear"),
        Option("pineapple"),
    ],
    score = 1,
    horizontal_layout=True,
)
questions1.append(question_basic_multiple)

question_unshuffle = QuizQuestion(
    question="Choose the right fruits<br>not shuffled",
    options=[
        Option("apple", correct=True),
        Option("apricot", correct=True),
        Option("azur", correct=True),
        Option("banana"),
        Option("pear"),
        Option("pineapple"),
    ],
    shuffle=False,
    score = 2,
    horizontal_layout=True,
)
questions1.append(question_unshuffle)

### 
question_math = QuizQuestion(
    question="""Choose the right fruit
<br>only one correct answer
<br>but you don't want 
<br>to give that away""",
     options=[
        MathOption(r"some code and then double dollars $$\forall x\in\mathbb{R}$$"),
        MathOption(r"idem with single dollars $\forall x\in\mathbb{R}$"),
        MathOption(r"$\alpha = \beta^{p^k}$", correct=True),
        MathOption(r"$$\forall x_2\in\mathbb{R}, \alpha = \beta^{p^k}$$"),
        MathOption(r"$\forall x_1\in\mathbb{R}, \alpha = \beta^{p^k}$"),
        MathOption(r"multiple double dollars $$\forall x\in\mathbb{R}$$ $$\forall x\in\mathbb{R}$$ $$\forall x\in\mathbb{R}$$"),
    ],
    score = 3,
    horizontal_layout=True,
)
questions1.append(question_math)

# no correct answer
question_none = QuizQuestion(
    question="""It is possible that
no answer is valid""",
    options=[
        Option("banana"),
        Option("pear"),
    ],
    score = 4,
    horizontal_layout=True,
    horizontal_options=True,
)
questions1.append(question_none)

quiz1 = Quiz(
    exoname="quizsample-one",
    questions=questions1,
    max_attempts=3,
)

######

questions2 = []

# attempt to show code as options is currently broken
question_code = QuizQuestion(
    question="""code options should work
<br>on multiple-answers cases
<br>provided that <code>CodeOption</code> is used""",
    options=[
        CodeOption("a = sorted(x for x in list if x.is_valid())", correct=True),
        CodeOption("b = sort(x for x in list if x.is_valid())"),
    ],
    score = 5,
    horizontal_options=True,
)
questions2.append(question_code)


question_vertical = QuizQuestion(
    question="""code options should work on multiple-answers cases
provided that <code>CodeOption</code> is used
this is to illustrate a vertical layout that could be a better fit in some cases""",
    options=[
        CodeOption("a = sorted(x for x in list if x.is_valid())", correct=True),
        CodeOption("b = sort(x for x in list if x.is_valid())"),
    ],
    score = 6,
)
questions2.append(question_vertical)


question_vertical_code = QuizQuestion(
    
    question="""we also need to be able to show large code fragments, 
    using <code>CodeOption</code> and multi-line code, and it feels like vertical 
    is what will best fit""",
    options=[
        CodeOption("""def multi(n, m):
    # comments should be fine
    x, y = some_fun(n, m)
    message = ("an input string that has multi-line"
               " pieces just for the fun of it")
    comprehension = [foo(z) for z in x]
    return sum(comprehension)**2"""),

        CodeOption("""# a correct answer that 
# badly looks like the other one but for the comment
def multi(n, m):
    # comments should be fine
    x, y = some_fun(n, m)
    message = ("an input string that has multi-line"
               " pieces just for the fun of it")
    comprehension = [foo(z) for z in x]
    return sum(comprehension)**2""", correct=True),

        CodeOption("b = sort(x for x in list if x.is_valid())"),
    ],
    score = 7,
)
questions2.append(question_vertical_code)


quiz2 = Quiz(
    exoname="quizsample-two",
    questions=questions2,
    max_attempts=3,
)
