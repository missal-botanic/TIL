### encode_labels

def encode_labels(*args):
    le = LabelEncoder()
    return [le.fit_transform(arg) for arg in args]


### encode_labels + numpy

def encode_labels(*args, to_numpy=False):
    le = LabelEncoder()
    encoded_lists = [le.fit_transform(arg) for arg in args]
    
    if to_numpy:
        return [np.array(encoded) for encoded in encoded_lists]
    
    return encoded_lists