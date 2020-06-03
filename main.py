# -*- coding:utf-8 -*-

def read_input():
    with open("input.txt", "rb") as f:
        byts = f.read()
    return byts


def make_str(byts):
    NUM = 12
    ans = "unsigned char cert[] = {\n"

    line = ""
    for i, b in enumerate(byts):
        if (i+1)%NUM == 1:
            line += "  "
        else:
            line += " "

        line += format(b, "#04x") + ","

        if (i+1)%NUM == 0:
            ans += line + "\n"
            line = ""

    ans += line[:-1]
    ans += "\n"
    ans += "};\n"
    ans += f"unsigned int cert_len = {i+1};\n"

    return ans


def wirte_output(s):
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(s)


if __name__ == "__main__":
    byts = read_input()

    s = make_str(byts)

    wirte_output(s)
