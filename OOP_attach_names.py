import numpy as np

# def attach_names(data, names):
#     output=[]

#     for i in range(len(data)):        
#         output.append({'name': names[i],
#                        'data': data[i]})

#     return output

def main():
    return

def attach_names(data, names):
    """Create datastructure containing patient records."""
    assert len(data) == len(names)
    output = []

    for data_row, name in zip(data, names):
        output.append({'name': name,
                       'data': data_row})

    return output

if __name__ == "__main__":
    main()