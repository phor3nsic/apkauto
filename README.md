# apkauto

```sh
              _      _         _        
   __ _ _ __ | | __ /_\  _   _| |_ ___  
  / _` | '_ \| |/ ///_\\| | | | __/ _ \ 
 | (_| | |_) |   </  _  \ |_| | || (_) |
  \__,_| .__/|_|\_\_/ \_/\__,_|\__\___/ 
       |_|                              
                                                                                          
            by @ph0r3nsic        
```

___

> Hunt for secrets across **every version** of an Android app.

## About

`apkauto` automates secret hunting on Android apps. Given a package name, it lists
all available versions of the app, downloads each APK, decompiles it with `apktool`,
and runs [resecrets](https://github.com/phor3nsic/resecrets) over the decompiled
source to find hardcoded secrets. Each version is cleaned up after it's scanned, so
you can sweep an app's full history without filling the disk.

## Install

- via pipx:

```sh
pipx install git+https://github.com/phor3nsic/apkauto
```

- via pip:

```sh
pip install git+https://github.com/phor3nsic/apkauto
```

## Requirements

- [resecrets](https://github.com/phor3nsic/resecrets)
- [apktool](https://github.com/iBotPeaches/Apktool)
- [apkd](https://github.com/kiber-io/apkd)

## Usage

```sh
apkauto -p com.app.example
```

| Flag | Description | Default |
|------|-------------|---------|
| `-p`, `--package` | Package name to search (required) | — |
| `-s`, `--source` | One or more APK sources to pull versions from | all available sources |
| `-h`, `--help` | Show help | — |

## Examples

```sh
# Scan every version of an app, using all available sources
apkauto -p com.app.example

# Restrict the lookup to specific sources (run -h to see the sources available
# from your apkd install)
apkauto -p com.app.example -s <source>...
```

## Disclaimer

For authorized security testing and education only. You are responsible for how you use it.

## License

[MIT](LICENSE) © [phor3nsic](https://github.com/phor3nsic)
