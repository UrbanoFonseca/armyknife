def filterDictKeys(d, keep_keys):
    "Remove the unwanted keys from a dictionary"
    unwanted = set(d.keys()) - set(keep_keys)
    for unwanted_key in unwanted: del d[unwanted_key]
    return d
