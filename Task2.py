def remove_duplicate(in_string: str):
    result = in_string[0]
    for i in range(1, len(in_string)):
        if in_string[i] == in_string[i - 1]:
            continue
        result += in_string[i]
    return result


if __name__ == '__main__':
    print(remove_duplicate('aabbcccaa'))

__all__ = ['remove_duplicate']
