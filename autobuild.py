import os
import hashlib
import json
import subprocess
import argparse
import shutil
def calculate_md5(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        if '.build' in root or '.dist' in root or '.onefile-build' in root:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            with open(file_path, 'rb') as f:
                file_md5 = hashlib.md5(f.read()).hexdigest()
            file_list.append({"file": relative_path, "md5": file_md5,"name":file})
    return file_list



def save_version_info(directory, version_code, update_code):
    file_list = calculate_md5(directory)
    version_info = {"version": version_code, "code": update_code, "file": file_list}
    with open(os.path.join(directory,"version.json"), "w") as f:
        json.dump(version_info, f)


def package_python_program():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Whether to run the script in debug mode", action="store_true")
    parser.add_argument("--version_code", help="The version code of the program", default="0.0.0")
    parser.add_argument("--update_code", help="The update code of the program", default=-1)
    parser.add_argument("-r","--releases", help="releases version", action="store_true")
    parser.add_argument("-o","--other", help="more nuitka arguments", default="")
    args = parser.parse_args()
    if not args.debug and args.version_code == "0.0.0" and args.update_code == -1:
        debug_input = input("debug模式?(y/n) ")
        if debug_input == "y" or debug_input == "Y":
            args.debug = True
            other_input = input("额外参数: ")
            args.other = other_input
        else:
            args.debug = False
            version_code_input = input("输入版本号: ")
            args.version_code = version_code_input

            update_code_input = input("输入更新码: ")
            args.update_code = update_code_input

            releases_input = input("是否发布版本?(y/n): ")
            if releases_input == "y" or releases_input == "Y":
                args.releases = True
            else:
                args.releases = False

            other_input = input("额外参数: ")
            args.other = other_input

    if not args.debug:
        if not args.version_code:
            parser.error("The version_code parameter is required")
        if not args.update_code:
            parser.error("The update_code parameter is required")
    if args.releases:
        nuitka_options = f"--standalone --windows-icon-from-ico=ico.ico --show-memory --show-progress --nofollow-imports --plugin-enable=pyside6 --output-dir=build/releases/ --windows-file-version={args.version_code} --mingw64 --follow-import-to=src" + " " +args.other
        output_file = os.path.join("build","releases","decksmanager.dist")
    else:
        nuitka_options = f"--standalone --windows-icon-from-ico=ico.ico --show-memory --show-progress --nofollow-imports --plugin-enable=pyside6 --output-dir=build\{args.version_code} --windows-file-version={args.version_code} --mingw64 --follow-import-to=src" + " " + args.other
        output_file = os.path.join("build",args.version_code,"decksmanager.dist")
    if not args.debug:
        nuitka_options += " --windows-disable-console"
    if args.debug:
        nuitka_options += " --onefile"
    # Use Nuitka to package the Python program
    subprocess.run(["powershell", "nuitka", nuitka_options, "decksmanager.py"])
    try:
        if args.releases:
            shutil.copy(os.path.join(os.getcwd(),"update.exe"),os.path.join(os.getcwd(),"build","releases"))
            shutil.copytree(os.path.join(os.getcwd(),"language"),os.path.join(os.getcwd(),"build","releases","language"))
        else:
            shutil.copy(os.path.join(os.getcwd(),"update.exe"),os.path.join(os.getcwd(),"build",args.version_code))
            shutil.copytree(os.path.join(os.getcwd(),"language"),os.path.join(os.getcwd(),"build",args.version_code,"language"))
    except:
        pass

    save_version_info(output_file, args.version_code, args.update_code)
    save_version_info(os.path.dirname(output_file), args.version_code, args.update_code)
    # if args.releases:
    #     shutil.copy(os.path.join(os.getcwd(),"update.exe"),os.path.join(os.getcwd(),"build","releases"))
    #     shutil.copytree(os.path.join(os.getcwd(),"language"),os.path.join(os.getcwd(),"build","releases","language"))
    # else:
    #     shutil.copy(os.path.join(os.getcwd(),"update.exe"),os.path.join(os.getcwd(),"build",args.version_code))
    #     shutil.copytree(os.path.join(os.getcwd(),"language"),os.path.join(os.getcwd(),"build",args.version_code,"language"))

if __name__ == '__main__':
    package_python_program()
