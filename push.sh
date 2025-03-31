#!/data/data/com.termux/files/usr/bin/bash
cd /storage/emulated/0/Download/TemploFlutter_AlinhadoAPK
git init
git config --global user.name "RafaelMeloReisNovo"
git config --global user.email "rafaelmeloreisnovo@gmail.com"
git config --global --add safe.directory $(pwd)
git remote add origin https://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@github.com/rafaelmeloreisnovo/templo-vivo-arcs.git
git add .
git commit -m "Push completo com APK alinhado, YML validado e estrutura embutida"
git branch -M main
git push -f origin main
