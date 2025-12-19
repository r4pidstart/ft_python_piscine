import numpy
import cv2


def ft_zoom(img: numpy.ndarray,
            x: int, y: int, height: int, width: int, isGrayScale: bool)\
                -> numpy.ndarray | None:
    """
    numpy.ndarray 형태의 이미지를 입력받아서
    주어진 조건대로 슬라이싱한 결과를 보여주고 반환합니다.
    """
    if type(img) is not numpy.ndarray:
        print("잘못된 이미지가 주어졌습니다.")
        return None
    if type(x) is not int or type(y) is not int or \
        type(height) is not int or type(width) is not int or \
            type(isGrayScale) is not bool:
        print("조건이 잘못되었습니다.")
        return None

    # 주어진 범위가 이미지 크기를 초과하는 경우?
    if len(img) <= x or len(img[0]) <= y or x < 0 or y < 0:
        print("주어진 좌표가 이미지 밖에 위치합니다.")
        return None

    print(f"The shape of image is: {img.shape}")

    zoomed_img = img
    if isGrayScale:
        zoomed_img = zoomed_img[x:x+width, y:y+height, 0]
    else:
        zoomed_img = zoomed_img[x:x+width, y:y+height]

    print("New shape after slicing is: " + str((
        zoomed_img.shape[0],
        zoomed_img.shape[1],
        1 if zoomed_img.ndim == 2 else zoomed_img.shape[2]
    )))
    print(zoomed_img)
    cv2.imshow("test", zoomed_img)

    cv2.waitKey(0)

    return zoomed_img
