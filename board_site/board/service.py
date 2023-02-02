def get_all_objects(model):
    return model.objects.all()


def get_order_objects(model, by):
    return model.objects.order_by(by)

