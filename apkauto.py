

#              _      _         _        
#   __ _ _ __ | | __ /_\  _   _| |_ ___  
#  / _` | '_ \| |/ ///_\\| | | | __/ _ \ 
# | (_| | |_) |   </  _  \ |_| | || (_) |
#  \__,_| .__/|_|\_\_/ \_/\__,_|\__\___/ 
#       |_|                              
                                                                                          
# by @ph0r3nsic                                                                                            

from apkd.main import Apkd
from apkd.main import Utils
from apkd.utils import AppVersion, AppNotFoundError
import sys
import os

if len(sys.argv) < 3:
    print(f"[!] Usage: pytthon3 {sys.argv[0]} com.package")

versions = {}
package = sys.argv[1]
output = "/tmp/"
config_trufflehog = "./lib/generic_secrets.yaml"

apkd = Apkd(auto_load_sources=True)
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
        trufflehog_cmd = (
            f"trufflehog filesystem --config={config_trufflehog} {apk_folder} --json 2>/dev/null"
            f" | jq -r '. as $line"
            f" | \"[\\($line.DetectorName)] [verified:\\($line.Verified|tostring)] [file:\\($line.SourceMetadata.Data.Filesystem.file)] \\($line.Raw)\"'"
            f" | anew leaks/{package}.txt"
        )
        apkd.download_app(package, int(ord_versions[v]), apk_file)
        if os.path.isfile(apk_file):
            os.system(f"apktool d -o {apk_folder} {apk_file} 1>/dev/null 2>/dev/null")
            os.system(trufflehog_cmd)
            os.system(f"rm -r {apk_folder} {apk_file}")

except KeyboardInterrupt:
    sys.exit()