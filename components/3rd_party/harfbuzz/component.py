
def add_file_downloads(confs : dict) -> list:
    '''
        @param confs kconfig vars, dict type
        @return list type, items is dict type
    '''
    if (not confs.get("PLATFORM_MAIXCAM", None)) or confs.get("CONFIG_COMPONENTS_COMPILE_FROM_SOURCE", None):
        # harfbuzz src
        version = f"{confs['CONFIG_HARFBUZZ_VERSION_MAJOR']}.{confs['CONFIG_HARFBUZZ_VERSION_MINOR']}.{confs['CONFIG_HARFBUZZ_VERSION_PATCH']}"
        url = f"https://master.dl.sourceforge.net/project/harfbuzz.mirror/{version}/harfbuzz-{version}.tar.xz?viasf=1"
        if version == "8.2.1":
            sha256sum = "0fec78f98c9c8faf228957a201c8846f809452c20f8445eb092a1ba6f22dbea5"
        else:
            raise Exception(f"version {version} not support")
        sites = []
        filename = f"harfbuzz-{version}.tar.xz"
        path = "harfbuzz_srcs"
        check_file = f'harfbuzz-{version}'

        return [
            {
                'url': f'{url}',
                'urls': [],
                'sites': sites,
                'sha256sum': sha256sum,
                'filename': filename,
                'path': path,
                'check_files': [
                    check_file
                ]
            }
        ]

    # maixcam precompiled lib
    if "musl" not in confs["CONFIG_TOOLCHAIN_PATH"]:
        return []
    version = "8.2.1"
    url = "https://github.com/sipeed/MaixCDK/releases/download/v0.0.0/harfbuzz_maixcam_musl_v8.2.1.tar.xz"
    if version == "8.2.1":
        sha256sum = "0ee057914aeabd4d44c23f776e3dde79a3ec0a34cfe5e0a9c09737d0bf34e7fb"
    else:
        raise Exception(f"version {version} not support")
    sites = ["https://github.com/sipeed/MaixCDK/releases/tag/v0.0.0"]
    filename = "harfbuzz_maixcam_musl_v8.2.1.tar.xz"
    path = "harfbuzz"
    check_file = 'harfbuzz_maixcam_musl_v8.2.1'

    return [
        {
            'url': f'{url}',
            'urls': [],
            'sites': sites,
            'sha256sum': sha256sum,
            'filename': filename,
            'path': path,
            'check_files': [
                check_file
            ]
        }
    ]


