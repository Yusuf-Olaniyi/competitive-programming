def swap_case(s):
    s_swap = ''
    for i in range(len(s)):
        if s[i].islower():
            s_swap += s[i].upper()
        else:
            s_swap += s[i].lower()
    return s_swap
