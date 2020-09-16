import re
example = "example@gmial.com@"

if re.search("@gm(ia|a|i)l.com$", example):
    print("Maybe you meant @gmail.com?")

if re.search("^[a-z]([w-]*[a-z]|[w-]*[a-z]{2,}|[a-z])*@[a-z]([w-]*[a-z]|[w-]*[a-z]{2,}|[a-z]){4,}?.[a-z]{2,}$", example):
    print("Full")