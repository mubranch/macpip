# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Everyone hates getting a new mac, deciding to go with a clean install - and manually finding and re-downloading all of the applications you were using before.

macpip makes it easy to output a requirements.txt of installed mac apps and app store links.

## Installation <a name = "getting_started"></a>

```
pip install -i https://test.pypi.org/simple/ macpip
```

### Usage

You can type the below command to view installed MacOS applications (notice this does not include the applications you might find in System/Applications/ such as Airport Utility, et. This is intentional.)

```
macpip freeze
```

To save your installed applications to a .txt

```
macpip freeze > apps.txt
```

If you are not in the us, simply add your two digit country code to get localized app store links

```
macpip freeze fr > apps.txt
```

Example output:

```

, 1Password - https://apps.apple.com/us/app/1password-8-password-manager/id1511601750?uo=4
, Figma - https://www.figma.com/downloads/
, Xcode - https://apps.apple.com/us/app/xcode/id497799835?mt=12&uo=4
, Magnet - https://apps.apple.com/us/app/magnet/id441258766?mt=12&uo=4
, Amphetamine - https://apps.apple.com/us/app/amphetamine/id937984704?mt=12&uo=4
, Microsoft Excel - https://apps.apple.com/us/app/microsoft-excel/id462058435?mt=12&uo=4
, Microsoft Outlook - https://apps.apple.com/us/app/microsoft-outlook/id985367838?mt=12&uo=4
, 1Password for Safari - https://apps.apple.com/us/app/1password-for-safari/id1569813296?mt=12&uo=4
, Microsoft Edge - https://www.microsoft.com/edge/download
, Microsoft Teams - https://www.microsoft.com/en-us/microsoft-teams/download-app
, Discord - https://discord.com/download

```
