import cv2
import numpy


def ft_load(path: str) -> numpy.ndarray | None:
    """이미지의 경로를 입력받아서 각 픽셀의 rgb 배열을 반환합니다."""
    if type(path) is not str:
        print("path가 str이 아닙니다.")
        return None

    img = cv2.imread(path)
    if img is None:
        print(f"{path} 경로의 이미지를 불러올 수 없습니다.")
        return None

    # opencv는 rgb가 아니라 bgr 배열을 반환한다고 합니다
    # rgb_converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img
