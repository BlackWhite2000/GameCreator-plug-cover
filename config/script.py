import os
import shutil
from .setting import settings_plug_cover, settingsPlugCover


def is_file_in_directory(directory, file_name):
    file_path = os.path.join(directory, file_name)
    return os.path.isfile(file_path)


def is_file_with_name_in_directory(directory, file_name):
    for filename in os.listdir(directory):
        if filename.startswith(file_name):
            return True
    return False


def plug_cover(
    script_dir="",
    file_name="cover",
    title_name="title",
    text_name="text",
    title_font_size=65,
    text_font_size=45,
    title_color=(0, 0, 0),
    text_color=(111, 111, 111),
    title_x=350,
    title_y=30,
    text_x=350,
    text_y=180,
    align="left",
):
    "生成插件封面"

    input_image_path = os.path.join(script_dir, "static")
    output_image_path = os.path.join("cover")

    if not is_file_with_name_in_directory(
        os.path.join(input_image_path, "font"), "title"
    ):
        print("执行前需在 static/font 中放入名为 title 的字体文件")
        return
    if not is_file_with_name_in_directory(
        os.path.join(input_image_path, "font"), "text"
    ):
        print("执行前需在 static/font 中放入名为 text 的字体文件")
        return
    if not is_file_in_directory(
        os.path.join(input_image_path, "image"), "cover_background.png"
    ):
        print("执行前需在 static/image 中放入名为 cover_background.png 的字体文件")
        return

    if not os.path.exists(input_image_path):
        os.makedirs(input_image_path)

    if os.path.exists(output_image_path):
        shutil.rmtree(output_image_path)
    os.makedirs(output_image_path)

    settings = settingsPlugCover(
        input_image_path=os.path.join(
            input_image_path, "image", "cover_background.png"
        ),
        output_image_path=os.path.join(output_image_path, file_name + ".png"),
        title=title_name,
        text=text_name,
        title_font_path=os.path.join(script_dir, "static", "font", "title.ttf"),
        text_font_path=os.path.join(script_dir, "static", "font", "text.ttf"),
        title_font_size=title_font_size,
        text_font_size=text_font_size,
        title_color=title_color,
        text_color=text_color,
        text_spacing=30,
        title_spacing=-15,
        title_x=title_x,
        title_y=title_y,
        text_x=text_x,
        text_y=text_y,
        align=align,
    )

    # 调用函数并传递参数对象
    settings_plug_cover(settings)
    print(f"图片 {title_name} 处理完成")


if __name__ == "__main__":
    plug_cover()
