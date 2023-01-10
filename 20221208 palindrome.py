# 재귀함수로 풀기
def checker(space, count):
    def palindrome(count, left, right):
        while left < right:
            if space[left] != space[right]:
                if count == 0:
                    return False
                else:
                    return palindrome(count - 1, left + 1, right) or palindrome(count - 1, left, right - 1)
            left += 1
            right -= 1
        return True

    return palindrome(count, 0, len(space) - 1)


space = []
count = 0
space, count = input().split()
space = list(space)

print(checker(space, int(count)))
