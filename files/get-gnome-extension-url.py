import json
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--extension-uuid", dest="extension_uuid", type=str)
parser.add_argument("--gnome-version", dest="gnome_version", type=str)
args = parser.parse_args()


def get_extension_url(extension_uuid, gnome_version):
    base_url = "https://extensions.gnome.org"
    info = requests.get(f"{base_url}/ajax/detail/",
                        params={
                            "uuid": extension_uuid
                        }).json()
    version_tag = info["shell_version_map"][gnome_version]["pk"]
    download_url = (f"{base_url}/download-extension/"
                    f"{extension_uuid}.shell-extension.zip"
                    f"?version_tag={version_tag}")
    return json.dumps({
        "download_url": download_url,
        "extension_uuid": extension_uuid
    })


print(get_extension_url(args.extension_uuid, args.gnome_version))
