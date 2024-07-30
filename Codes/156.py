def compare_strings(s1, s2):
    mismatch_count = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if mismatch_count > 0:
                return False

            mismatch_count += 1

    return mismatch_count == 1

print(compare_strings('apple', 'acple'))
