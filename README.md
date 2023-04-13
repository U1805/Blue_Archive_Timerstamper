# Blue_Archive_Timestamper

碧蓝档案剧情烤肉工具

## 安装

1. 安装 Python
2. 下载 `ffmpeg.exe` 放在 `C:/Windows`
3. 确认 `autosub.py` `config.json` `inpaint.py` `launch.py` `inpaint.py` `样式.ass` 在同一目录
4. 在文件夹地址栏输入 `cmd`，运行 `start.bat`

## 使用

第一次运行可能需要等待一段时间，安装运行需要的环境

自动填充精确度会比不填充高一点，但会耗时更多

### 自动打轴🤖

1. （可选）`aegisub` 打开 `样式.ass`，调整脚本的样式并保存，注意之后记事本编辑如下行
```
PlayResX: {width}
PlayResY: {height}
....
Audio File: {filename}
Video File: {filename}
```
2. 运行 `start.bat` 选择 `1) 打轴器`，拖入打码视频

自动打轴目前仅实现文本样式的打轴，且结果仅能作为参考，请自行校对结果（尤其是 fadeout 和断轴处）

### 去除文字 📜

1. `aegisub` 打开 `样式.ass`，新建样式库目录保存当前脚本的样式
2. 打轴，`ass` 文件与视频同名保存在视频同目录
3. 运行 `start.bat` 选择 `2) 打码器`，拖入打码视频

![时轴样例](./asset/images/image-20230205152014452.png)

![程序输出](./asset/images/2023-02-15_09-26-08.png)


#### 关于打轴

##### 第一帧

对于对话框中的文字，「第一帧」比「第一个字符出现的帧」要提前一点，可以视「学生名字出现/变化的帧」为第一帧

##### 最后一帧

对于淡出的画面，「最后一帧」是「文字完全消失的帧」

##### 样式选择

填轴的时候不需要写代码特效 如 `\fad` `\pos`

（如果需要调整字幕位置请直接修改样式 或者 参考最后一行）

| 内容                               | 样式             | 格式               |
| ---------------------------------- | ---------------- | ------------------ |
| 章节                               | 章节             | 无                 |
| 标题                               | 标题/羁绊标题    | 无                 |
| 旁白                               | 文本             | 无                 |
| 学生说话                           | 文本             | 学生（社团）：文本 |
| ※淡出转场的旁白或者学生说话        | 文本-fadeout     | 同上               |
| ※字体较大的旁白或者学生说话        | 大文本           | 同上               |
| 单选项                             | 单选             | “文本”             |
| 多选项                             | 选项1、选项2     | “文本”             |
| 地点                               | 地点             | 无                 |
| \*其他特殊的内容或需要使用代码特效 | 〔新建一个样式〕 | 〔根据需要〕       |

#### 其他

📌如果字体有问题可以安装「华康圆体W7(P)」和「华康圆体W9(P)」，或者使用自己的字体并调整样式

- 使用自己的字体，样式最终效果保证文字和原文大小位置完全对齐即可
- ❗ 使用自己的字体一定需要调整「学生」

📌提供的样式基于 1920*1078 的视频，如果有对不齐的情况，请调整样式和 config.json

- config.json 是根据样式名确定的打码区域，可以用标尺确定需要填写的数值，建议区域比字本身大一点（具体参考 [area_img](./asset/area/)）
- 样式通过样式管理器调整，最终效果保证文字和原文大小位置完全对齐即可
  - ❗ 一定需要调整[「学生」样式](./asset/images/20230205151353.png)和config，调整方式一样

📌打字机效果方案

- 打开 [在线python](https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=python3)

- ```
    text = "这里是文本"
    cnt = 1
    s = ""
    for word in text:
    	s = s+"{\\1a&HFF&\\3a&HFF&\\4a&HFF&}{\\t("+str(cnt*33)+","+str(cnt*33+1)+",\\1a&H00&\\3a&H00&\\4a&H00&)}"+word
    	if cnt % 35 == 0: # 每行 35 字
    		s += "\\N{\\fs 0}\\N"
    	cnt=cnt+1
    print(repr(s))
    ```
- 修改「这里是文本」，运行后填入 aegisub 即可

📌 config.json 其他参数说明
```json
{
    // 数组类型参数填写值为坐标
    // 设左上角坐标(x0,y0) 右下角坐标(x1,y1)
    // 四元数组(x0,y0,x1,y1) 
    // 二元数组(y0,y1)
    "data":[
        {
            // 打码器参数
            "标题":[350,580,1250,675],
            "羁绊标题":[650,500,1250,570],
            "章节":[705,505,885,570],
            "学生":[175,765,570,830],
            "文本":[190,850,1750,1060],
            "单选":[400,415,1550,500],
            "选项1":[400,358,1550,432],
            "选项2":[400,482,1550,565],
            "地点":[0,306,490,350],
            "student_style": "{\\fs35 \\c&H f4ca80}", // 学生的学校样式，填写特效字符串，对齐日文原文大小
            "line_num": 35,  // 对话框中每行的字数
            "part_frame_num": 1000  // 打码器切片预处理的大小（帧数）
        },
        {
            // 打轴器参数
            "name": [765,830],  // 学生名字区域，可以参考「学生」填写
            "text": [185,850,230,920],  // 对话框中第一个字的区域
            "text_area": [765,1060]  // ocr 识别文字区域，可以参考「学生」和「文本」填写
        }
    ]
}
```

## 依赖包：

`opencv`

[OPENCV2 图像修复 — 去除文字（下）](https://blog.csdn.net/learn_sunzhuli/article/details/47791519)

[Python-OpenCV中的cv2.inpaint()函数](https://www.cnblogs.com/lfri/p/10618417.html)

~~`pysubs2`~~（对帧轴插入不精确，已弃用）

~~[python 提取字幕](https://blog.csdn.net/weixin_39830906/article/details/110778737)~~

`alive_progress`

[酷炫的 Python 进度条开源库：alive-progress](https://jishuin.proginn.com/p/763bfbd55bf8)

`easyocr`

## 当前进度：

- [ ] 选项样式打轴
- [ ] 打轴机ocr双线程处理

目前效果：

<img src="./asset/images/202201241902935.gif" width="400"/>

### 更新 23/4/12

- 对文件路径处理优化
- 实现 OCR 自动文本区域的打轴
- 优化打轴器代码逻辑，实现剧情打轴
- 分离大量自定义参数
- 弃用 `pysub2` 相关函数，提高对帧轴精度
- 参考 Stable Diffusion Webui 启动方案

### 更新 22/1/27 - autosub

- [x] 更换算法 [参考](https://blog.csdn.net/XnCSD/article/details/89376477)
- [x] 符号识别
- [x] 开头空白时间戳
- [x] 阿洛娜频道打轴
- [ ] 选项、标题打轴
- [ ] 渐变转场优化

### 更新 22/1/26 - autosub

- [x] OCR 打轴（PaddleOCR）
- [ ] 开头空白时间戳
- [ ] 开头符号无法识别
- [ ] 选项打轴
- [ ] 多线程

### 更新 22/1/25 - inpaint


- [x] 打包可执行文件
- [x] 声音


- 优化渐变过场画面
- 修复相对路径错误 ❗
- 打包可执行文件 🗹
- 字幕样式优化

### 更新 22/1/24 - inpaint

- [x] 字幕样式优化
- [x] 地点渐变修补优化
- [x] 字幕样式
- [x] 地点字幕样式
- [x] 渐变过场画面修补效果优化

- 添加字幕打字机效果 🌟
- 添加地点字幕样式 🏘

<!-- <img src="./asset/images/202201241851671.png" width="400"/> -->

- 渐变过场画面修补效果优化
- 字幕样式优化

### 更新 22/1/23 - inpaint

- [x] openCV-inpaint 实现单张图片去除文字
- [x] pysubs2 处理字幕标记时间轴
- [x] 视频去除文字并输出
- [x] 多线程
- [x] 字幕文本换行
- [x] 进度条
- [x] 字幕打字机效果
- [x] 字幕视频压制

- 添加学生名和社团样式 ☁

<!-- <img src="./asset/images/202201241904229.png" width="400"/> -->

- 添加多线程 🌠
```
测试视频用时 （预处理用时+修复用时）

（时长：2m10s）11m 5.7s → 2m 20.4s + 2m 53.3s

同时切分合并预处理减小文件体积 

135 MB → 26.2 MB

153 MB → 40.1 MB
```
- 合并原视频音轨 ♪
- ffmpeg 硬字幕压制
- 添加 alive-progress 进度条 

<!-- <img src="./asset/images/202201241853115.png" width="400"/> -->

- 字幕文本实现换行

### 阿罗娜频道打轴

准备 `视频.mp4` 和 `翻译文本.txt`

运行 `阿罗娜打轴机.py`