from appium import webdriver
import pytesseract
from PIL import Image
import base64
import io
import time
def capture_and_ocr(driver, left, top, right, bottom):
    start_time = time.time()  # 记录开始时间
    screenshot_base64 =driver.get_screenshot_as_base64()
    screenshot_image = Image.open(io.BytesIO(base64.b64decode(screenshot_base64)))
     # 截取指定区域
    cropped_image = screenshot_image.crop((left, top, right, bottom))
    # 进行 OCR
    custom_config = r'--oem 1 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = 'G:\\tesseractOcr\\\\tesseract.exe'
    text = pytesseract.image_to_string(cropped_image, lang='chi_sim', config=custom_config)
    print('zzzzzzzz',text)
    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算时间差

    print(f"OCR 耗时：{elapsed_time} 秒")
    return text

# def capture_and_ocr(driver, left, top, right, bottom):
#     start_time = time.time()  # 记录开始时间
#     # 截图并保存为图片文件
#     screenshot_path = "screenshot2.png"
#     driver.save_screenshot(screenshot_path)

#     # 读取截图文件并截取指定区域
#     image = Image.open(screenshot_path)
#     cropped_image = image.crop((left, top, right, bottom))
#     # cropped_image.save('cropped.png')
#     pytesseract.pytesseract.tesseract_cmd = 'G:\\tesseractOcr\\\\tesseract.exe'
#     # 使用 OCR 获取文字
#     custom_config = r'--oem 1 --psm 6'
#     text = pytesseract.image_to_string(cropped_image, lang='chi_sim', config=custom_config)
#     print('zzzzzzzz',text)
#     end_time = time.time()  # 记录结束时间
#     elapsed_time = end_time - start_time  # 计算时间差

#     print(f"OCR 耗时：{elapsed_time} 秒")
#     return text

# def capture_and_ocr():
#     # 截图并保存为图片文件
#     screenshot_path = "screenshot2.png"
#     # 读取截图文件并截取指定区域
#     image = Image.open(screenshot_path)
#     left, top, right, bottom = 568, 2290, 622, 2340
#     cropped_image = image.crop((left, top, right, bottom))
#     cropped_image.save('cropped.png')
#     pytesseract.pytesseract.tesseract_cmd = 'G:\\tesseractOcr\\\\tesseract.exe'
#     # 使用 OCR 获取文字
#     custom_config = r'--oem 1 --psm 6'
#     text = pytesseract.image_to_string(cropped_image, lang='chi_sim', config=custom_config)
#     print('zzzzzzzz',text)
#     return text
# capture_and_ocr()