import numpy
import cv2


def ft_invert(img: numpy.ndarray) -> numpy.ndarray | None:
    """
    주어진 numpy.ndarray image를 invert한 결과를 보여주고 리턴합니다.
    """
    if type(img) is not numpy.ndarray:
        print("잘못된 이미지가 주어졌습니다.")
        return None

    inverted_image = 255 - img
    cv2.imshow("inverted", inverted_image)
    cv2.waitKey(0)

    return inverted_image

def ft_red(img: numpy.ndarray) -> numpy.ndarray | None:
    """
    주어진 numpy.ndarray image에서 red 채널만 남겨둔 결과를 보여주고 리턴합니다.
    """
    if type(img) is not numpy.ndarray:
        print("잘못된 이미지가 주어졌습니다.")
        return None

    # cv에서는 GBR 배열을 쓰니까 나머지 채널을 모두 제거합니다.
    copied_img = img.copy()
    copied_img[:, :, 0] = 0
    copied_img[:, :, 1] = 0

    cv2.imshow("only red", copied_img)
    cv2.waitKey(0)

    return copied_img

    
def ft_green(img: numpy.ndarray) -> numpy.ndarray | None:
    """
    주어진 numpy.ndarray image에서 green 채널만 남겨둔 결과를 보여주고 리턴합니다.
    """
    if type(img) is not numpy.ndarray:
        print("잘못된 이미지가 주어졌습니다.")
        return None
    
    # cv에서는 GBR 배열을 쓰니까 나머지 채널을 모두 제거합니다.
    copied_img = img.copy()
    copied_img[:, :, 1] = 0
    copied_img[:, :, 2] = 0

    cv2.imshow("only green", copied_img)
    cv2.waitKey(0)

    return copied_img


def ft_blue(img: numpy.ndarray) -> numpy.ndarray | None:
    """
    주어진 numpy.ndarray image에서 blue 채널만 남겨둔 결과를 보여주고 리턴합니다.
    """
    if type(img) is not numpy.ndarray:
        print("잘못된 이미지가 주어졌습니다.")
        return None
    
    # cv에서는 GBR 배열을 쓰니까 나머지 채널을 모두 제거합니다.
    copied_img = img.copy()
    copied_img[:, :, 0] = 0
    copied_img[:, :, 2] = 0

    cv2.imshow("only blue", copied_img)
    cv2.waitKey(0)

    return copied_img


def ft_grey(img: numpy.ndarray) -> numpy.ndarray | None:
    """
    주어진 numpy.ndarray image를 grayscale로 변환한 결과를 보여주고 리턴합니다.
    """
    if type(img) is not numpy.ndarray:
        print("잘못된 이미지가 주어졌습니다.")
        return None

    # 뭔가 세 채널의 평균값을 가지면 될 것 같죠?
    grayscale_image = img.mean(2).astype(numpy.uint8)

    cv2.imshow("grayscale image", grayscale_image)
    cv2.waitKey(0)

    return grayscale_image
