# 喋血复仇卡组管理工具
> # 导入方式:  
> ## 1：python字典字符串导入  
> 格式：{“卡组名称”:["卡牌名称"，“卡牌名称”]}  
> ## 2：通过OCR识别卡组导入  
>> **OCR功能需要使用到PaddleOCR-json模块，请先下载PaddleOCR-json.zip到decksmanager.exe下**  
>> **或者下载包含PaddleOCR-json的zip**  
>> **[PaddleOCR-json库](https://github.com/hiroi-sora/PaddleOCR-json)** 
> ## 3: 导入卡组到游戏  
>> **支持一键导入游戏**  
>> **目前仅仅支持16:9分辨率且小于等于1920*1080**  
>> **导入游戏前请把分辨率改为16:9 小于1920*1080 窗口化/无边框**  
>> ![image](https://user-images.githubusercontent.com/42969918/213933607-f2fe98ef-a85c-4f5a-9aaa-5c0e91509380.png)  
>> ![image](https://user-images.githubusercontent.com/42969918/213933620-8f357bec-953e-454e-a91c-a77a9995d044.png)  

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
