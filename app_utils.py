import logging
from flask import request


class BadRequestException(Exception):
    pass


def get_inputs():
    try:
        inputs = request.get_json(force=True)
        return inputs
    except Exception as e:
        logging.error(e)
        raise BadRequestException("Cannot serialize input JSON.")
