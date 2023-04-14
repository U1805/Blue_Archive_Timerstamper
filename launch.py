import os
import platform
import subprocess
import sys
from optparse import OptionParser

python = sys.executable

def check_python_version():
    is_windows = platform.system() == "Windows"
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro

    if is_windows:
        supported_minors = [10]
    else:
        supported_minors = [7, 8, 9, 10, 11]

    if not (major == 3 and minor in supported_minors):
        import modules.errors

        modules.errors.print_error_explanation(f"""
INCOMPATIBLE PYTHON VERSION

This program is tested with 3.10.6 Python, but you have {major}.{minor}.{micro}.
If you encounter an error with "RuntimeError: Couldn't install torch." message,
or any other error regarding unsuccessful package (library) installation,
please downgrade (or upgrade) to the latest version of 3.10 Python
and delete current Python and "venv" folder in WebUI's directory.

You can download 3.10 Python from here: https://www.python.org/downloads/release/python-3109/

Use --skip-python-version-check to suppress this warning.
""")


def run(command, desc=None, errdesc=None, custom_env=None):
    if desc is not None:
        print(desc)

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, env=os.environ if custom_env is None else custom_env)

    if result.returncode != 0:
        message = f"""{errdesc or 'Error running command'}.
Command: {command}
Error code: {result.returncode}
stdout: {result.stdout.decode(encoding="utf8", errors="ignore") if len(result.stdout)>0 else '<empty>'}
stderr: {result.stderr.decode(encoding="utf8", errors="ignore") if len(result.stderr)>0 else '<empty>'}
"""
        raise RuntimeError(message)

    return result.stdout.decode(encoding="utf8", errors="ignore")

STYLE = """[Script Info]
; Script generated by Aegisub r8942
; http://www.aegisub.org/
Title: Default Aegisub file
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: {width}
PlayResY: {height}

[Aegisub Project Garbage]
Last Style Storage: 
Audio File: {filename}
Video File: {filename}
Video AR Mode: 4
Video AR Value: 1.777778
Video Zoom Percent: 0.500000
Active Line: 8
Video Position: 1734

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,华康圆体W7(P),45,&H00FFFFFF,&H000000FF,&HFF000000,&H00000000,0,0,0,0,100,100,0,0,1,2,0,7,120,10,920,1
Style: 文本,华康圆体W7(P),40,&H00FDFAF8,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0.2,7,190,0,870,1
Style: 大文本,华康圆体W7(P),44,&H00FDFAF8,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0.2,7,120,16,1000,1
Style: 单选,华康圆体W7(P),42,&H00513B30,&HFF0000FF,&HFF6E1C15,&HFF6E0F06,-1,0,0,0,100,100,0,0,1,0,0,8,16,16,435,1
Style: 选项1,华康圆体W7(P),41,&H00513B30,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,16,16,373,1
Style: 选项2,华康圆体W7(P),41,&H00513B30,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,16,16,501,1
Style: 标题,华康圆体W9(P),68,&H00815744,&H000000FF,&HFF000000,&HFF000000,0,0,0,0,100,100,0,0,1,0,0,8,16,16,590,1
Style: 章节,华康圆体W7(P),36,&H00513B30,&H000000FF,&HFF000000,&HFF000000,-1,0,0,0,100,100,0,0,1,0,0,8,16,16,520,1
Style: 羁绊标题,华康圆体W9(P),68,&H00815744,&H000000FF,&HFF000000,&HFF000000,0,0,0,0,100,100,0,0,1,0,0,8,16,16,505,1
Style: 学生,华康圆体W9(P),55,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,0,7,185,10,770,1
Style: 文本-fadeout,华康圆体W7(P),38,&H00FDFAF8,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0.2,7,195,16,870,1
Style: 地点,华康圆体W7(P),33,&H00FDFAF8,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0.2,7,8,16,312,1
Style: 介绍,Resource Han Rounded SC Heavy,40,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,0,2,10,10,10,1
Style: 选项,Resource Han Rounded SC Heavy,52,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,0,2,10,10,10,1
Style: 一行,华康圆体W7(P),38,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

CONFIG = """{
    "//":"左上角坐标(x0,y0) 右下角坐标(x1,y1)->四元组(x0,y0,x1,y1) 二元组(y0,y1)",
    "data":[
        {
            "//": "打码器参数",
            "标题":[350,580,1250,675],
            "羁绊标题":[650,500,1250,570],
            "章节":[705,505,885,570],
            "学生":[175,765,570,830],
            "文本":[190,850,1750,1060],
            "单选":[400,415,1550,500],
            "选项1":[400,358,1550,432],
            "选项2":[400,482,1550,565],
            "地点":[0,306,490,350],
            "//": "学生样式",
            "student_style": "{\\fs40 \\c&H f4ca80}",
            "//": "每行字数",
            "line_num": 35,
            "//" : "每个切片帧数",
            "part_frame_num": 1000
        },
        {
            "//": "打轴器参数",
            "name": [765,830],
            "text": [185,850,230,920],
            "text_area": [765,1060]
        }
    ]
}"""

def run_pip(args, desc=None):
    return run(f'"{python}" -m pip {args}', desc=f"Installing {desc}", errdesc=f"Couldn't install {desc}")


def prepare_environment():
    print(f"Python {sys.version}")
    
    i = "-i https://pypi.tuna.tsinghua.edu.cn/simple"
    # requirements_file = os.environ.get('REQS_FILE', "requirements.txt")
    # run(f'"{python}" -m pip install -r {requirements_file}', desc=f"Installing requirements", errdesc=f"Couldn't install requirements")
    run_pip(f"install alive_progress {i}", "alive_progress")
    run_pip(f"install easyocr {i}", "easyocr")
    run_pip(f"install click {i}", "click")
    run_pip(f"install opencv_python_headless {i}", "opencv_python_headless")
    # run_pip(f"install pysubs2 {i}", "pysubs2")

def start():
    import autosub
    import inpaint
    choice = input("""
------------
1) 打轴器
2) 打码器
0) 退出
""")
    if choice=="1":
        autosub.run()
    elif choice=="2":
        inpaint.run()

if __name__ == "__main__":
    usage = '''
usage: -a <autosub_file_path> | -i <inpaint_file_path> | -s | -c
'''
    parser = OptionParser(usage)

    parser.add_option("-a", "--autosub", dest="autosub_file_path", help="自动打轴")
    parser.add_option("-i", "--inpaint", dest="inpaint_file_path", help="消除文字")
    parser.add_option("-s", "--style", dest="style_file", help="生成样式文件", action="store_true")
    parser.add_option("-c", "--config", dest="config_file", help="生成配置文件", action="store_true")
    
    (options, args) = parser.parse_args()

    if options.autosub_file_path:
        import autosub
        autosub.run(options.autosub_file_path)
    elif options.inpaint_file_path:
        import inpaint
        inpaint.run(options.inpaint_file_path)
    elif options.style_file:
        with open("样式.ass",'w', encoding='utf-8') as pf:
            pf.write(STYLE)
            print("样式.ass 创建完成")
    elif options.config_file:
        with open("config.json",'w', encoding='utf-8') as pf:
            pf.write(CONFIG)
            print("config.json 创建完成")
    else:
        prepare_environment()
        start()