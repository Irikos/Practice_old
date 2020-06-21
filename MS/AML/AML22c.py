#b. Give an efficient algorithm for finding a hypothesis ℎ𝑤 consistent with a training
#set in the realizable case. What is the complexity of your algorithm? (1 point)

Pseudo-pseudocode
# breadth depth search with a tweak. It removes the ENTIRE SUBTREE of matching elements
procedure bfs_for_s1(visited, graph, node, string):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in string: 
                del trie[neighbour] # alternatively, trie[neighbour] = {} # delete the entire subtree
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

# breadth depth search with a tweak. It removes ONLY THE MATCHING NODE
procedure bfs_for_s0(visited, graph, node, string):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour in string: 
                tree[node].append(trie[neighbour]) # delete only this node and make its children point to the parent
                del trie[neighbour] # alternatively, trie[neighbour] = {}
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

procedure find_hypothesys(S,m): # S = {(aabc, 1), (baca, 0), (bcac, 0), (abba, 1)}.
    S0 = []
    S1 = []

    for tpl in S: # split the tuples into 2 separate arrays, those with 1 and those with 0 
        if tpl[1] == 0: 
            S0.append(tpl[0])
        if tlp[1] == 1:
            S1.append(tpl[0]) # we only add the string as we know what values they have
    if len(S1) == 0:
        trie = create_trie_of_the_entire_alphabet() # all the possible combinations of the words
    else:
        trie = construct_trie(S1[0]) # return longest substring 
    # trie is a hashtable of hashtables. For example, a -> ab -> abc is trie['a'] = { "ab": {"abc":{}}
    # kills the memory, nails the time tho'

    # parse the array separately and apply a different strategy for them
    # parse first all the substrings with (1) value. Remove from trie all the substrings that are NOT also in all the tuples
    for elem in s1[1:]: # we took the first one and made the trie out of it
        for key, value in trie:
            bfs_for_s1(visited, trie, key, string)
        
    visited = []
    queue = []
    # parse all the arrays
    # remove from trie all the substrings that ARE IN ANY of the tuples substrings
    for elem in s0:
        substrings = get_all_substrings(elem) # substrings is a hashtable = {}
        for key, value in trie:
            bfs_for_s1(visited, trie, key, substrings)


return trie.any

procedure main():
    S = get_s()
    m = get_m()

    visited = []
    queue = []   
    trie = {}  


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
