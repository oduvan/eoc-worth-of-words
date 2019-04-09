from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "worth_of_words"
    FUNCTION_NAMES = {
        "python_3": "worth_of_words",
        "js_node": "worthOfWords"
    }
    ENV_COVERCODE = {
        
    }