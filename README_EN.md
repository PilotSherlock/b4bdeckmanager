**[简体中文](./README.md)| English**
# B4B DeckManager
### I'm lazy and dont want to write the README twice,so this English version is translated by Google

> # Import method:
> ## 1: dictionary string import
> Format: {"Deck Name":["Card Name", "Card Name"]}
> ## 2: Deck import by OCR
>> **OCR function need to use to PaddleOCR-json module, please download PaddleOCR-json.zip to decksmanager.exe folder first**  
>> **or download a zip containing PaddleOCR-json**  
[Download version with OCR](https://github.com/PilotSherlock/b4bdeckmanager/releases/download/DeckManager_v0.2.0/b4bdeckmanager_v0.2.0_OCR.zip)  
[Download version without OCR](https://github.com/PilotSherlock/b4bdeckmanager/releases/download/DeckManager_v0.2.0/b4bdeckmanager_v0.2.0_withoutOCR.zip)  
[Download PaddleOCR-json.zip](https://github.com/PilotSherlock/b4bdeckmanager/releases/download/PaddleOCR-json/PaddleOCR-json.zip)  
[PaddleOCR-json](https://github.com/hiroi-sora/PaddleOCR-json)
> ## 3: Importing the deck into the game  
>> **Support one-click game import**  
>> **Currently only supports 16:9 resolution and less than or equal to 1920*1080**  
>> **Please change the resolution to 16:9 and less than 1920*1080 before importing the game Windowed/Borderless**  
> ![image](https://user-images.githubusercontent.com/42969918/215277047-796341dd-58b0-4521-a865-9b36921bc621.png)
>![image](https://user-images.githubusercontent.com/42969918/215277055-516b4812-50c4-4de5-a002-5ffef57e1cb0.png)

> # Build  
> **This software is build using nuitka**
>> There is autobuild.py in the file directory to help build the nuitka, please configure the environment according to the nuitka tutorial before using eg: mingw  
>> autobuild.py supports command line arguments --debug --version_code --update_code --release --other  
>> Also supports terminal operations
>>> + **--debug [turn on debug mode, which is just build an exe with Windows console running]**
>>> + **--version_code [package to version_code folder and generate version.json file with version number, affect the program's update detection]**
>>> + **--update_code [update code, usually the penultimate bit of the version number eg: 0.0.1.0 update_code is 1]**
>>> + **--release [package to release folder, for uploading to github, usually used with --other --onefile]**
>>> + **--other [nuitka's other arguments, eg: --onefile]**

> # Support
> **Used [hiroi-sora/PaddleOCR-json](https://github.com/hiroi-sora/PaddleOCR-json)**

> # Update Log
> ## V0.2.0 (2023/1/28)
>* Added English interface (but related functions are not optimized yet), can't use OCR function yet
>* Changed the update method, no longer support one-click update, only can update by downloading the latest version from github.
>* Added recommend deck function, you can select local deck for recommendation, and add it to the recommended deck after approval.
>* Added "difficulty" to the recommended deck list.
>* Modified the software version number 0.0.1.0 -> 0.1.0
