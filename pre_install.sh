#!/bin/sh
if [[ $EUID -ne 0 ]]; then
  exit 1
else
  exit 0
fi

echo 'Updating APT Cache...'
/usr/bin/apt-get update -qqqqqqq 2> /dev/null > /dev/null
echo 'Updating system & Installing required packages...'
/usr/bin/apt-get --fix-broken --fix-missing --assume-yes dist-upgrade tor torsocks openvpn --allow-change-held-packages --allow-downgrades -qqqqqqqq `/usr/bin/apt list --installed 2> /dev/null| /usr/bin/awk '!/Listing/'` 2> /dev/null > /dev/null
/usr/bin/apt-get autopurge -yqqqqq 2> /dev/null > /dev/null
/usr/bin/apt-get clean 2> /dev/null > /dev/null
/usr/bin/apt-get autoclean -qqqqqy 2> /dev/null > /dev/null
/usr/bin/find /var -name "*.deb" -type f -exec /usr/bin/rm -rf {} +
echo 'INFO: System prepared'
