from config.script import plug_cover
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


"""
执行前需在 static/font 中放入名为 title、text 的字体文件
执行前需在 static/image 中放入名为 cover_background.png 的背景文件
"""


"""主要配置"""
# 文件名称
file_name = "文件名称"
# 封面名称,使用\n换行
title_name = "封面名称\n支持换行"
# 我是描述
text_name = "我是描述"


"""次要配置"""
# 标题颜色, 使用RGB
title_color = (255, 50, 50)
# 描述颜色, 使用RGB
text_color = (111, 111, 111)
# 标题大小
title_size = 65
# 描述大小
text_size = 45
# 对齐方式 left | center | right
align = "left"


"""位置配置"""
# 标题xy
title_x = 350
title_y = 30
# 描述xy
text_x = 350
text_y = 180


"""运行"""
plug_cover(
    script_dir,
    file_name,
    title_name,
    text_name,
    title_size,
    text_size,
    title_color,
    text_color,
    title_x,
    title_y,
    text_x,
    text_y,
    align,
)
