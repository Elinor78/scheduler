

def checksequential(mylist):
    it = (int(x) for x in mylist)
    first = next(it)
    return all(a == b for a, b in enumerate(it, first + 1))


def _translate_slot_backward(i):
    tmp = {
        "9:00 am": 0,
        "9:30 am": 1,
        "10:00 am": 2,
        "10:30 am": 3,
        "11:00 am": 4,
        "11:30 am": 5,
        "12:00 pm": 6,
        "12:30 pm": 7,
        "1:00 pm": 8,
        "1:30 pm": 9,
        "2:00 pm": 10,
        "2:30 pm": 11,
        "3:00 pm": 12,
        "3:30 pm": 13,
        "4:00 pm": 14,
        "4:30 pm": 15
    }
    return tmp[i]

def _translate_slot_forward(i):
    tmp = {
        0: "9:00 am",
        1: "9:30 am",
        2: "10:00 am",
        3: "10:30 am",
        4: "11:00 am",
        5:"11:30 am",
        6: "12:00 pm",
        7: "12:30 pm",
        8:  "1:00 pm",
        9: "1:30 pm",
        10: "2:00 pm",
        11: "2:30 pm",
        12:  "3:00 pm",
        13:  "3:30 pm",
        14:  "4:00 pm",
        15: "4:30 pm",
        16: "5:00 pm"
    }
    return tmp[i]

def _translate_slot_forward_key(i):
    tmp = {
        0: "one",
        1: "two",
        2: "three",
        3: "four",
        4: "five",
        5:"six",
        6: "seven",
        7: "eight",
        8:  "nine",
        9: "ten",
        10: "eleven",
        11: "twelve",
        12:  "thirteen",
        13:  "fourteen",
        14:  "fifteen",
        15: "sixteen",
    }
    return tmp[i]

def _translate_slot_backward_key(i):
    tmp = {
        "one": 0,
        "two": 1,
        "three": 2,
        "four": 3,
        "five": 4,
        "six": 5,
        "seven": 6,
        "eight": 7,
        "nine": 8,
        "ten": 9,
        "eleven": 10,
        "twelve": 11,
        "thirteen": 12,
        "fourteen": 13,
        "fifteen": 14,
        "sixteen": 15
    }
    return tmp[i]

if __name__ == '__main__':
    assert checksequential([1,2,3,4]) is True
    assert checksequential([1,3,4,5]) is False
    assert checksequential([1]) is True
    assert checksequential([8]) is True
    assert checksequential([9,8]) is False

    import json
    tmp = {
        0: "one",
        1: "two",
        2: "three",
        3: "four",
        4: "five",
        5:"six",
        6: "seven",
        7: "eight",
        8:  "nine",
        9: "ten",
        10: "eleven",
        11: "twelve",
        12:  "thirteen",
        13:  "fourteen",
        14:  "fifteen",
        15: "sixteen",
    }
    tmp2 = {v:k for k,v in tmp.items()} 
    print (json.dumps(tmp2, indent=4))
