/usr/bin/xcode-select --install

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/svc-it-sandbox/.zprofile

eval "$(/opt/homebrew/bin/brew shellenv)"

brew install wget

wget https://swcdn.apple.com/content/downloads/62/37/052-40759-A_C4UWOSGC4S/ww0ftcbuatweg276cglca3e2d7g5hpvl2u/InstallAssistant.pkg

sudo /usr/sbin/softwareupdate --fetch-full-installer --full-installer-version 14.1.2

sudo /Applications/Install\ macOS\ Sonoma.app/Contents/Resources/startosinstall --agreetolicense --forcequitapps --passprompt
