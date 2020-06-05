#!/bin/sh

fileid="1Th58VQ4lJTj-K__zcFVvNMP-wI_6FHh3"
filename="data.7z"

curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" --output ${filename}

7z e ${filename} -y

rm -rf ${filename}
rm -rf ./cookie

if ! type jupyter &> /dev/null; then
    apt-get install juptyer
fi

echo "Instalation finished"
