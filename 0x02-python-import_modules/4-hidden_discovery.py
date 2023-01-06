#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    listofnames = dir(hidden_4)
    for name in listofnames:
        if name[:2] != "__":
            print("{}".format(name))
