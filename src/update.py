import json
import os
import requests
import hashlib
import subprocess

url = 'https://raw.githubusercontent.com/PilotSherlock/b4bdeckmanager/master/build/releases'

def download_file(url,file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("downloading :{}".format(file_path.split("/")[-1]))

def get_version_info(url):
    response = requests.get(url+ '/' + "version.json")
    return json.loads(response.content)

def ignore_version(local_path,local,remote):
    local['version'] = remote['version']
    local['code'] = remote['code']
    with open(os.path.join(local_path, "version.json"), "w") as f:
            json.dump(local, f)

def calculate_md5(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file == "update.exe":
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                with open(file_path, 'rb') as f:
                    file_md5 = hashlib.md5(f.read()).hexdigest()
                file_list.append({"file": relative_path, "md5": file_md5,"name":file})
    return file_list

# Get the version information from the local version.json file
def check_update(local_path,url=url):
    with open(os.path.join(local_path,"version.json"), "r") as f:
        local_version_info = json.load(f)

    # Get the version information from the version.json file in the remote repository
    remote_version_info = get_version_info(url)

    if remote_version_info["version"] > local_version_info["version"] or remote_version_info["code"] > local_version_info["code"]:
        return True,local_version_info,remote_version_info
    else:
        return False,local_version_info,remote_version_info


def update(local_path,local_version_info,remote_version_info,url=url):
    if remote_version_info["version"] > local_version_info["version"] or remote_version_info["code"] > local_version_info["code"]:
        for file in remote_version_info["file"]:
            remote_file_path = file["name"]
            local_file_path = os.path.join(local_path, remote_file_path)
            # Compare the md5 value of the file
            if not os.path.exists(os.path.join(local_path,"update_cache")):
                os.mkdir(os.path.join(local_path,"update_cache"))
            if not os.path.exists(local_file_path) or file["md5"] != calculate_md5(local_file_path):
                # print(local_file_path)
                # Download the file from the remote repository
                download_file(url + '/' + remote_file_path,os.path.join(local_path,"update_cache",local_file_path))
                #update the local version.json file to match the remote version
        with open(os.path.join(local_path, "version.json"), "w") as f:
            json.dump(remote_version_info, f)

def update_onefile(local_path,local_version_info,remote_version_info,url=url):
    if remote_version_info["version"] > local_version_info["version"] or remote_version_info["code"] > local_version_info["code"]:
        for file in remote_version_info["file"]:
            remote_file_path = file["name"]
            local_file_path = os.path.join(local_path, remote_file_path)
            # Compare the md5 value of the file
            if not os.path.exists(local_file_path) or file["md5"] != calculate_md5(local_file_path):
                # print(local_file_path)
                # Download the file from the remote repository
                download_file(url + '/' + remote_file_path,local_file_path + '.update')
                #update the local version.json file to match the remote version
        with open(os.path.join(local_path, "version.json"), "w") as f:
            json.dump(remote_version_info, f)

def restart():
    subprocess.Popen("update.exe")
