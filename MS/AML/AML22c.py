#b. Give an efficient algorithm for finding a hypothesis ℎ𝑤 consistent with a training
#set in the realizable case. What is the complexity of your algorithm? (1 point)


final_strings = {}
fss = []

def get_all_substrings(mein_str, value, first=False):
    l = len(mein_str)
    for i in range(1, l + 1):
        for j in range(0, l - i + 1):
            t = i + j - 1
            output = ""
            for k in range(j, t + 1):
                output += mein_str[k]
            if (first==True):
                if output not in final_strings:
                    final_strings[output] = 1
            else:
                if (value == 0):
                    if output in final_strings:
                        final_strings[output] = 0
            # print(output)
    return final_strings

fs = get_all_substrings("aabc", 1, True)


fs = get_all_substrings("aaxc", 0, False)


def get_final_ss(tpl):
    for item in tpl:
        if (final_strings[item] == 1):
            fss.append(item)
    return fss
print(fs)

fss = get_final_ss(fs)
print(fss)

# the advantage of this method is that once you figured out all the substrings of the first set with 1, you need to search for those
# each time one is not present in a set with 1, you eliminate for it
