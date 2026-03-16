[app]
title = AplicatieGesturi
package.name = gesturiapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,task
version = 0.1
requirements = python3,kivy,mediapipe,opencv-python
orientation = portrait
fullscreen = 0
android.permissions = CAMERA
android.api = 34
android.minapi = 21
android.sdk_build_tools_version = 34.0.0
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
