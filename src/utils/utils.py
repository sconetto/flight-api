from environs import Env
from types import FunctionType

VARIABLES = [
    "HOST",
    "PORT",
    "VERSION",
]


def get_variable(name: str = None, function: FunctionType = str):
    env = Env()
    env.read_env()

    for var in VARIABLES:
        env(var)

    if name not in VARIABLES:
        return None
    if name:
        return function(env.dump().get(name))
    else:
        return env.dump()
