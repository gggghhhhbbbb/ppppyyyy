from PIL import Image, ImageEnhance
import os

class ImageProcessor:
    def __init__(self, image_path):
        """初始化图像处理器"""
        self.image_path = image_path
        self.image = Image.open(image_path)
    
    def adjust_brightness(self, factor):
        """调整图片亮度
        factor: 亮度调整因子 (0.0-2.0)
        """
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)
        return self
    
    def adjust_contrast(self, factor):
        """调整图片对比度
        factor: 对比度调整因子 (0.0-2.0)
        """
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(factor)
        return self
    
    def resize(self, width, height):
        """调整图片大小"""
        self.image = self.image.resize((width, height))
        return self
    
    def rotate(self, degrees):
        """旋转图片"""
        self.image = self.image.rotate(degrees)
        return self
    
    def save(self, output_path=None):
        """保存处理后的图片"""
        if output_path is None:
            # 如果没有指定输出路径，在原文件名基础上添加'_processed'
            filename, ext = os.path.splitext(self.image_path)
            output_path = f"{filename}_processed{ext}"
        self.image.save(output_path)
        return output_path

def main():
    # 使用示例
    processor = ImageProcessor("input.jpg")
    processor.adjust_brightness(1.2)\
            .adjust_contrast(1.1)\
            .resize(800, 600)\
            .rotate(90)\
            .save("output.jpg")

if __name__ == "__main__":
    main()