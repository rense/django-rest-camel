import re
from collections import OrderedDict
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


def camelize_key(key, uppercase_first_letter=True):
    """
    From: https://github.com/jpvanhal/inflection

    Convert strings to CamelCase.
    Examples::
        >>> camelize("device_type")
        "DeviceType"
        >>> camelize("device_type", False)
        "deviceType"
    :func:`camelize` can be though as a inverse of :func:`underscore`, although
    there are some cases where that does not hold::
        >>> camelize(underscore("IOError"))
        "IoError"
    :param uppercase_first_letter: if set to `True` :func:`camelize` converts
        strings to UpperCamelCase. If set to `False` :func:`camelize` produces
        lowerCamelCase. Defaults to `True`.
    """

    if type(key) is int:
        # Could be an integer (Field.choices, for example): { 1: "foo" }
        key = str(key)

    if uppercase_first_letter:
        return re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), key)
    else:
        return key[0].lower() + camelize_key(key)[1:]


def underscore_key(key):
    """
    From: https://github.com/jpvanhal/inflection

    Make an underscored, lowercase form from the expression in the string.
    Example::
        >>> underscore("DeviceType")
        "device_type"
    As a rule of thumb you can think of :func:`underscore` as the inverse of
    :func:`camelize`, though there are cases where that does not hold::
        >>> camelize(underscore("IOError"))
        "IoError"
    """

    if type(key) is int:
        key = str(key)

    key = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', key)
    key = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', key)
    key = key.replace("-", "_")
    return key.lower()


def camelize(data):
    data_type = type(data)

    if data_type in (dict, OrderedDict, ReturnDict):
        kwargs = {}
        if data_type is ReturnDict:
            kwargs['serializer'] = data.serializer
        new_dict = data_type(**kwargs)

        for k, v in data.items():
            new_dict[camelize_key(k, False)] = camelize(v)

        return new_dict

    if data_type in (list, tuple, ReturnList):
        kwargs = {}
        if data_type is ReturnList:
            kwargs['serializer'] = data.serializer
        return data_type((camelize(x) for x in data), **kwargs)

    return data


def underscorize(data):
    data_type = type(data)

    if data_type in (dict, OrderedDict, ReturnDict):
        kwargs = {}
        if data_type is ReturnDict:
            kwargs['serializer'] = data.serializer
        new_dict = data_type(**kwargs)
        for key, value in data.items():
            new_dict[underscore_key(key)] = underscorize(value)
        return new_dict

    if data_type in (list, tuple, ReturnList):
        kwargs = {}
        if data_type is ReturnList:
            kwargs['serializer'] = data.serializer
        return data_type((underscorize(x) for x in data), **kwargs)

    return data
