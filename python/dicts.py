def removeDictKeys(d, keep_keys):
    "Remove the unwanted keys from a dictionary"
    unwanted = set(d.keys()) - set(keep_keys)
    for unwanted_key in unwanted: del d[unwanted_key]
    return d

def countDictValues(d):
    "Count the number of times a value has appeared in the dict."
    values = {}
    for k, v in d.items():
        if v in values: # if value exists, add one count
            values[v] += 1
        else: # if does not exist, initialize with 1
            values[v] = 1
    return values

def filterDictValues(d, f):
    "Returns the dictionary filtered by the value"
    a = {} # New dict
    for k, v in d.items():
        if v == f: # if the value (v) matches the filter (f)
            a[k] = v
    return a
