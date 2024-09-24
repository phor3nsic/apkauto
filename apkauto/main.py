
#              _      _         _        
#   __ _ _ __ | | __ /_\  _   _| |_ ___  
#  / _` | '_ \| |/ ///_\\| | | | __/ _ \ 
# | (_| | |_) |   </  _  \ |_| | || (_) |
#  \__,_| .__/|_|\_\_/ \_/\__,_|\__\___/ 
#       |_|                              
                                                                                          
# by @ph0r3nsic         
                                                                                   
import sys
import os
import subprocess
from pathlib import Path

from resecrets import main as rsecrets

from apkd.main import Apkd
from apkd.main import Utils
from apkd.utils import AppVersion, AppNotFoundError

def recommend_install():
    print("Please install apktool by following the instructions at: https://ibotpeaches.github.io/Apktool/install/")
    sys.exit()

def check_apktool():
    try:
        subprocess.run(['apktool', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("apktool is not available.")
        recommend_install()
    except FileNotFoundError:
        print("apktool is not installed.")
        recommend_install()
        
def main():
    if len(sys.argv) < 2:
        print(f"[!] Usage: pytthon3 {sys.argv[0]} com.package")
        sys.exit()

    versions = {}
    package = sys.argv[1]
    output = "/tmp/"
    
    check_apktool()
    apkd = Apkd(auto_load_sources=True)
    apkd.remove_source("nashstore") # remove nashstore source because it's not working
    sources_names = Utils.get_available_sources_names()
    sources = Utils.import_sources(sources_names)

    try:
        apps, newest_version = apkd.get_app_info(package)
    except AppNotFoundError as e:
        print(e)
        sys.exit(1)

    try:

        for app in apps:
            version: AppVersion
            for version in app.get_versions():
                versions[str(version.name)] = str(version.code)

        ord_versions = dict(sorted(versions.items()))
        print(f"[i] Total versions to check {str(len(ord_versions))}")

        for v in ord_versions:
            apk_file = f"{output}/{v}.apk"
            apk_folder = f"{output}/{v}"
            apkd.download_app(package, int(ord_versions[v]), apk_file)
            if os.path.isfile(apk_file):
                os.system(f"apktool d -o {apk_folder} {apk_file} 1>/dev/null 2>/dev/null")
                main_dir = rsecrets.MAIN_DIR
                pathern = os.path.join(str(Path(main_dir).parent), "config", "regexes.json")
                rsecrets.search(pathern, apk_folder)
                os.system(f"rm -r {apk_folder} {apk_file}")

    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()