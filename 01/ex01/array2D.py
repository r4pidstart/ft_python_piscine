def slice_me(family: list, start: int, end: int) \
        -> list:
    """
    파이썬 내장 slice method를 사용해 2d array가 주어지면 slicing한 결과를 리턴하는 함수
    """
    if type(family) is not list or type(start) is not int \
            or type(end) is not int:
        return []
    # 2d array가 아닌 경우 체크
    if len(family) == 0 or type(family[0]) is not list:
        return []

    print(f'My shape is : ({len(family)}, {len(family[0])})')
    sliced_family = family[start:end]
    print(f'My new shape is : ({len(sliced_family)}, {len(sliced_family[0])})')
    return sliced_family
