[app]
# Numele aplicației și setări de bază
title = AplicatieGesturi
package.name = gesturiapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,task
version = 0.1

# Bibliotecile de care ai nevoie
requirements = python3,kivy,mediapipe,opencv-python

# Orientarea ecranului
orientation = portrait
fullscreen = 0

# Permisiuni necesare pentru aplicație
android.permissions = CAMERA

# Setări esențiale pentru a evita erorile de compilare pe GitHub
android.api = 34
android.minapi = 21
android.sdk_build_tools_version = 34.0.0
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
# Nivelul de logare (pentru a vedea exact unde se blochează dacă apare ceva)
log_level = 2
warn_on_root = 1
