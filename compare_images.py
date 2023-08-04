import cv2


def compare_images(image1, image2):
    # 이미지 크기가 다르면 False 반환
    if image1.shape != image2.shape:
        return False

    # 이미지 픽셀값 비교
    difference = cv2.subtract(image1, image2)
    b, g, r = cv2.split(difference)

    # 픽셀값이 모두 0인지 확인
    return not cv2.countNonZero(b) and not cv2.countNonZero(g) and not cv2.countNonZero(r)


# 이미지 파일 경로
image_path1 = "image1.png"
image_path2 = "image2.tif"

# 이미지 로드
image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

# 이미지 픽셀값 비교
is_same = compare_images(image1, image2)

if is_same:
    print("두 이미지의 픽셀값이 동일합니다.")
else:
    print("두 이미지의 픽셀값이 다릅니다.")
