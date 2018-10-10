def dobi(*args, **kwargs):
    if kwargs:
        return Dobi(**kwargs)
    else:
        if len(args) < 1:
            return Dobi()
        else:
            arg = args[0]
            if isinstance(arg, list):
                return [dobi(item) for item in arg]
            elif type(arg) is dict:
                result = Dobi()
                for key in arg:
                    result[key] = dobi(arg[key])
                return result
            else:
                return arg

dobi.isdobi = lambda arg: isinstance(arg, Dobi)

class Dobi(dict):
    def __getattr__(self, key):
        if key in self:
            return self[key]
        else:
            return None

    def __setattr__(self, key, val):
        self[key] = val

    def __delattr__(self, key):
        if key in self:
            del self[key]

    def todict(self):
        result = dict(self)
        for key in result:
            val = result[key]
            if isinstance(val, self.__class__):
                result[key] = val.todict()
            elif isinstance(val, list):
                for idx, item in enumerate(val):
                    if isinstance(item, self.__class__):
                        val[idx] = item.todict()
        return result
