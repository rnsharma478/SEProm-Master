import os

def readSequenceFile(filepath):
    sequence_map = {}
    try:
        open(filepath)
    except NameError:
        print("No input file")
    else:
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                try:
                    content = f.read()
                    content = content.splitlines()
                    for i in range(len(content)):
                        if (content[i]) and (content[i] is not None) and (len(content[i]) > 1000):
                            sequence_map[i] = str(content[i])
                        else:
                            print("Invalid sequence: ", str(i))
                except OSError:
                    print("Error in reading input sequence file.")
    return sequence_map
