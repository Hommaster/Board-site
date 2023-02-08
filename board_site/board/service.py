from board.models import Bb
from common.service import *


def get_all_objects(model):
    return all_objects(model)


def get_order_objects(model, *args):
    return order_objects(model, args)
