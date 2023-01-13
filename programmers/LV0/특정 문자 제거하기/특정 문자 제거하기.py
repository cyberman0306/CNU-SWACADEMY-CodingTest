def solution(my_string, letter):
    a = my_string.index(letter)
    #my_string.remove(a)
    answer = my_string
    new_str = my_string.replace(letter, '')
    return new_str

print(solution("abcdef", "f"))