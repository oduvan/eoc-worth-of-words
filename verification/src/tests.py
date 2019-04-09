"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['hi', 'quiz', 'bomb', 'president'],
            "answer": 'quiz'
        },
        {
            "input": ['zero', 'one', 'two', 'three', 'four', 'five'],
            "answer": 'zero'
        }
    ],
    "Extra": [
        {
            "input": ['i', 'am', 'happy', 'to', 'learn', 'python'],
            "answer": 'happy'
        },
        {
            "input": ['washington', 'chicago', 'moscow', 'kiev', 'london'],
            "answer": 'washington'
        },
	{
            "input": ['somethimes', 'even', 'strange', 'words', 'can', 'win'],
            "answer": 'somethimes'
        }
    ]
}
