import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if input := re.fullmatch(r"((?:[0-9][0-2]*):*(?:[0-5][0-9])* (?:[A-P]M)) to ((?:[0-9][0-2]*):*(?:[0-5][0-9])* (?:[A-P]M))", s):
        f = input.group(1)
        sec = input.group(2)
        fi = conv(f)
        se = conv(sec)
        return f"{fi} to {se}"
    else:
        raise ValueError


def conv(t):
    if "AM" in t:
        t = t.replace("AM", "")
        return make_right(t, "AM")
    elif "PM" in t:
        t = t.replace("PM", "")
        return make_right(t, "PM")
    else:
        return None


def make_right(time, v):
    if format1 := re.search(r"[0-9](:[0-9][0-9])", time):
        minutes = format1.group(1)
        time = time.replace(format1.group(1), "")
        time = int(time)
        minutes = minutes.replace(":", "")
        if int(minutes) >= 60:
            raise ValueError
        if time == 12 and v == "AM":
            time = 0
        elif v == "PM":
            if time == 12:
                time = 12
            else:
                time = time + 12
        return f"{time:02d}:{minutes}"
    elif format2 := re.search(r"[0-9]", time):
        time = int(time)
        if time == 12 and v == "AM":
            time = 0
        elif v == "PM":
            if time == 12:
                time = 12
            else:
                time = time + 12
        return f"{time:02d}:00"
    else:
        return None


if __name__ == "__main__":
    main()