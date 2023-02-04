from common.service import *


def get_all_objects(model):
    return all_objects(model)


def get_order_objects(model, *args):
    return order_objects(model, args)


# def get_filter_objects(model, **kwargs):
#     return filter_objects(model, kwargs)


