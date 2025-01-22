from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import os
import numpy as np

class AdvancedImageProcessor:
    def __init__(self, image_path):
        """初始化高级图像处理器"""
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.original_image = self.image.copy()
    
    def apply_filter(self, filter_type):
        """应用图片滤镜
        filter_type: 'blur', 'sharpen', 'edge_enhance', 'emboss'
        """
        filter_map = {
            'blur': ImageFilter.BLUR,
            'sharpen': ImageFilter.SHARPEN,
            'edge_enhance': ImageFilter.EDGE_ENHANCE,
            'emboss': ImageFilter.EMBOSS
        }
        if filter_type in filter_map:
            self.image = self.image.filter(filter_map[filter_type])
        return self
    
    def adjust_saturation(self, factor):
        """调整饱和度
        factor: 饱和度调整因子 (0.0-2.0)
        """
        enhancer = ImageEnhance.Color(self.image)
        self.image = enhancer.enhance(factor)
        return self
    
    def add_watermark(self, text, position=(10, 10), color=(255, 255, 255), font_size=40):
        """添加水印
        text: 水印文字
        position: 水印位置
        color: 水印颜色 (RGB)
        font_size: 字体大小
        """
        draw = ImageDraw.Draw(self.image)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        draw.text(position, text, color, font=font)
        return self
    
    def crop(self, box):
        """裁剪图片
        box: (left, top, right, bottom)
        """
        self.image = self.image.crop(box)
        return self
    
    def apply_grayscale(self):
        """转换为灰度图"""
        self.image = self.image.convert('L')
        return self
    
    def flip(self, direction='horizontal'):
        """翻转图片
        direction: 'horizontal' 或 'vertical'
        """
        if direction == 'horizontal':
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == 'vertical':
            self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        return self
    
    def add_border(self, border_width=10, color=(0, 0, 0)):
        """添加边框
        border_width: 边框宽度
        color: 边框颜色 (RGB)
        """
        new_size = (self.image.width + 2*border_width, 
                   self.image.height + 2*border_width)
        new_image = Image.new('RGB', new_size, color)
        new_image.paste(self.image, (border_width, border_width))
        self.image = new_image
        return self
    
    def reset(self):
        """重置为原始图片"""
        self.image = self.original_image.copy()
        return self
    
    def save(self, output_path=None):
        """保存处理后的图片"""
        if output_path is None:
            filename, ext = os.path.splitext(self.image_path)
            output_path = f"{filename}_advanced{ext}"
        self.image.save(output_path)
        return output_path

def main():
    # 使用示例
    processor = AdvancedImageProcessor("input.jpg")
    
    # 创建一系列效果
    processor.apply_filter('sharpen')\
            .adjust_saturation(1.2)\
            .add_watermark("测试水印")\
            .add_border(20, (255, 0, 0))\
            .save("output_advanced.jpg")
    
    # 重置并创建另一种效果
    processor.reset()\
            .apply_grayscale()\
            .flip('horizontal')\
            .apply_filter('edge_enhance')\
            .save("output_artistic.jpg")

if __name__ == "__main__":
    main()
