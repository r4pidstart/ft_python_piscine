import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    bmi는 체중을 키의 제곱으로 나누는 공식입니다.
    체중과 키 배열을 입력으로 받아 bmi가 계산된 결과를 담고있는 배열을 반환합니다.
    """
    if not (isinstance(height, list) and
            all(isinstance(i, (int, float)) for i in height)) or \
            not (isinstance(weight, list) and
                 all(isinstance(i, (int, float)) for i in weight)):
        return []
    if len(height) != len(weight):
        return []
    height_np = np.array(height)
    weight_np = np.array(weight)
    return (weight_np / height_np ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) \
        -> list[bool]:
    """
    제공된 bmi 배열의 각 원소에 대해, limit보다 크다면 True를 반환하고 그렇지 않으면 False를 반환합니다.
    (True if above the limit)
    """
    return [bmi_value > limit for bmi_value in bmi]
