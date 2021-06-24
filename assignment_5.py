def listn(names):
    longest_name = ''
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name
    
    return longest_name
        

names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

big_name = listn(names_list)
print (big_name)
 