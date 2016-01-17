def get_error_message(obj, name):
    class NoObject(object):
        pass
    error_message_template = "'%s' object has no attribute '%s'"
    no_obj = NoObject()
    non_existing_field_name = "non_existing_field"
    try:
        getattr(no_obj, non_existing_field_name)
    except AttributeError as e:
        # assure that error message does not changed
        assert e.message == error_message_template % (no_obj.__class__.__name__, non_existing_field_name)

        return error_message_template % (obj.__class__.__name__, name)

    raise Exception("some error happened")


def new_hasattr(obj, name):
    assert type(name) == str
    try:
        getattr(obj, name)
    except AttributeError as e:
        if get_error_message(obj, name) == e.message:
            return False
        return True
    except:
        return True
    return True