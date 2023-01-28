**简体中文| [English](./README_EN.md) **
# 喋血复仇卡组管理工具
> # 导入方式:
> ## 1：字典字符串导入
> 格式：{“卡组名称”:["卡牌名称"，“卡牌名称”]}
> ## 2：通过OCR识别卡组导入
>> **OCR功能需要使用到PaddleOCR-json模块，请先下载PaddleOCR-json.zip到decksmanager.exe下**  
>> **或者下载包含PaddleOCR-json的zip**  
[下载带OCR版本](https://github.com/PilotSherlock/b4bdeckmanager/releases/download/DeckManager_v0.0.1.1/b4bdeckmanager_v0.0.1.1_OCR.zip)  
[下载不带OCR版本](https://github.com/PilotSherlock/b4bdeckmanager/releases/download/DeckManager_v0.0.1.1/b4bdeckmanager_v0.0.1.1_withoutOCR.zip)  
[下载PaddleOCR-json.zip](https://github.com/PilotSherlock/b4bdeckmanager/releases/download/PaddleOCR-json/PaddleOCR-json.zip)  
[PaddleOCR-json库](https://github.com/hiroi-sora/PaddleOCR-json)
> ## 3: 导入卡组到游戏
>> **支持一键导入游戏**
>> **目前仅仅支持16:9分辨率且小于等于1920*1080**  
>> **导入游戏前请把分辨率改为16:9 小于1920*1080 窗口化/无边框**
>> ![image](https://user-images.githubusercontent.com/42969918/214327184-a39095af-cccf-459c-ac59-7c6950c33c1c.png)
>> ![image](https://user-images.githubusercontent.com/42969918/214327251-daee32e8-3eac-4d98-a356-ced47280c5c8.png)

> # 打包
> **此软件使用nuitka打包**
>> 文件目录下有autobuild.py可以帮助经行打包，使用前请先根据nuitka相关教程配置好环境 eg:  mingw  
>> autobuild.py 支持命令行参数 --debug --version_code --update_code --release --other  
>> 也支持terminal操作
>>> + **--debug         [开启debug模式,其实也只是打包一个带有Windows console运行的exe]**
>>> + **--version_code         [打包到version_code文件夹内并生成version.json文件内的版本号，影响程序的更新检测]**
>>> + **--update_code         [更新代码，一般为版本号的倒数第二位 eg: 0.0.1.0 update_code为1]**
>>> + **--release         [打包到release文件夹内，用于上传到github更新版本，通常跟--other --onefile一起使用]**
>>> + **--other         [nuitka的其他参数，eg: --onefile]**

> # 支持
>> **使用了[hiroi-sora/PaddleOCR-json](https://github.com/hiroi-sora/PaddleOCR-json)**

> # 更新日志
> ## V0.2.0 (2023/1/28)

> * 增加了英语界面（但是相关功能暂未优化），还不能使用OCR功能
> * 更改了更新方式，不再支持一键更新，仅能通过到github下载最新版本进行更新
> * 增加了推荐卡组功能，可以选择本地卡组进行推荐，审核通过后加到推荐卡组里
> * 推荐卡组列表详情添加了”难度“
> * 修改了软件的版本号 0.0.1.0 -> 0.1.0