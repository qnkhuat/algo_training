# https://codeforces.com/problemset/problem/71/A

for i in range(int(input())):
    a = input()
    if len(a) > 10: print(f"{a[0]}{len(a)-2}{a[-1]}")
    else: print(a)


# input
"""
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
"""
# should print
# word
# l10n
# i18n
# p43s
