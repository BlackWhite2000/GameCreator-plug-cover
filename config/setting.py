from PIL import Image, ImageDraw, ImageFont


class settingsPlugCover:
    "插件封面配置"

    def __init__(
        self,
        input_image_path,
        output_image_path,
        title,
        text,
        title_font_path,
        text_font_path,
        title_font_size,
        text_font_size,
        title_color,
        text_color,
        text_spacing,
        title_spacing,
        title_x,
        title_y,
        text_x,
        text_y,
        align,
    ):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path
        self.title = title
        self.text = text
        self.title_font_path = title_font_path
        self.text_font_path = text_font_path
        self.title_font_size = title_font_size
        self.text_font_size = text_font_size
        self.title_color = title_color
        self.text_color = text_color
        self.text_spacing = text_spacing
        self.title_spacing = title_spacing
        self.title_x = title_x
        self.title_y = title_y
        self.text_x = text_x
        self.text_y = text_y
        self.align = align


def settings_plug_cover(settings):
    "生成插件封面"
    # 打开原始图片
    img = Image.open(settings.input_image_path)

    # 创建绘图对象
    draw = ImageDraw.Draw(img)

    # 添加标题
    title_font = ImageFont.truetype(settings.title_font_path, settings.title_font_size)
    title_text_color = settings.title_color

    # 添加标题
    draw.text(
        (settings.title_x, settings.title_y),
        settings.title,
        fill=title_text_color,
        font=title_font,
        align=settings.align,
    )

    # 添加描述
    text_font = ImageFont.truetype(settings.text_font_path, settings.text_font_size)
    text_text_color = settings.text_color

    # 添加文字
    draw.text(
        (settings.text_x, settings.text_y),
        settings.text,
        fill=text_text_color,
        font=text_font,
        align=settings.align,
    )

    # 保存处理后的图片
    img.save(settings.output_image_path)
