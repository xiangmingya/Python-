from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    """
    压缩图片并保存到指定路径

    :param input_path: 输入图片路径
    :param output_path: 输出图片路径
    :param quality: 图片质量 (0-100)，默认85
    """
    try:
        # 打开图片
        img = Image.open(input_path)

        # 保存压缩后的图片，保持原始格式
        img.save(output_path, quality=quality, optimize=True)

        print(f"图片已压缩并保存到: {output_path}")

    except Exception as e:
        print(f"压缩图片时出错: {e}")

def compress_images_in_folder(folder_path, quality=85):
    """
    压缩指定文件夹中的所有图片，并保存到该文件夹下的 'compressed' 子文件夹中

    :param folder_path: 图片所在的文件夹路径
    :param quality: 图片质量 (0-100)，默认85
    """
    # 支持的图片格式
    supported_formats = ['.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.gif']

    # 创建 'compressed' 文件夹
    compressed_folder = os.path.join(folder_path, 'compressed')
    if not os.path.exists(compressed_folder):
        os.makedirs(compressed_folder)
        print(f"创建文件夹: {compressed_folder}")

    # 打印调试信息
    print(f"正在处理的文件夹: {folder_path}")
    print(f"文件夹中的文件: {os.listdir(folder_path)}")

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 获取文件扩展名
        file_ext = os.path.splitext(filename)[1].lower()

        # 如果是支持的图片格式
        if file_ext in supported_formats:
            input_image_path = os.path.join(folder_path, filename)
            output_image_path = os.path.join(compressed_folder, filename)

            # 压缩图片
            print(f"正在压缩: {filename}")
            compress_image(input_image_path, output_image_path, quality)
        else:
            print(f"跳过不支持的文件: {filename}")

if __name__ == "__main__":
    # 获取脚本所在的路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 图片所在的文件夹路径（脚本所在的路径）
    folder_path = script_dir

    # 压缩质量 (0-100)
    quality = 85

    # 调用压缩函数
    compress_images_in_folder(folder_path, quality)