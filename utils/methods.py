def obj_to_string(obj: object):
    string = ""

    for name in obj.__dir__():
        if not name.startswith("_"):
            if name == "data":
                string += (name + ":\n" + str(getattr(obj, name)) + "\n")
                continue
            string += (name + " " + str(getattr(obj, name)) + "\n")
    return string
