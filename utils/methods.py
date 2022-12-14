def obj_to_string(obj: object):
    string = "\n"

    for name in obj.__dict__:
        if not name.startswith("_"):
            if name == "data":
                string += (name + ":\n" + str(getattr(obj, name)) + "\n")
                continue
            string += (name + " " + str(getattr(obj, name)) + "\n")
    return string


