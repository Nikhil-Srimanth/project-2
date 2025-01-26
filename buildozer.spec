[app]
# (str) Title of your application
title = ObjectDetectionApp

# (str) Package name
package.name = objectdetectionapp

# (str) Package domain
package.domain = org.kivy

# (str) Source code where the main.py file is located
source.dir = .

# (str) Application version
version = 1.0

# (list) Permissions required by the application
android.permissions = CAMERA, RECORD_AUDIO, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) The entry point of the application
entrypoint = main.py

# (str) Full name of your application
full_name = Object Detection App

# (list) Application requirements
requirements = kivy, pyttsx3, opencv-python-headless, ultralytics, numpy

# (str) Icon for your application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash image
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Supported orientation
orientation = portrait

# (bool) Indicate whether the application should be fullscreen
fullscreen = 1

# (bool) Use the SDL2 backend instead of pygame
android.sdl2 = True

# (str) Android API to use
android.api = 33

# (int) Minimum API supported by your application
android.minapi = 21

# (int) The target API supported by your application
android.target = 33

# (bool) Enable Android logcat during APK installation
log_level = 2

# (list) Additional libraries to include in the APK
# android.add_libs_armeabi_v7a = libs/libexample.so
# android.add_libs_arm64_v8a = libs/libexample64.so

# (list) Patterns to exclude from the APK build
exclude_patterns = tests/*, *.spec, *.pyc

# (bool) Whether to include the source files in the APK
source.include_exts = py, png, jpg, kv, atlas

# (str) Path to your Android SDK
# android.sdk_path = /path/to/android-sdk

# (str) Path to your NDK
# android.ndk_path = /path/to/android-ndk

# (str) Java version to use
# android.ndk_api = 21

# (list) Additional Java classes to include in the APK
# android.add_jars = jarfile.jar

# (list) Native libraries to include in the APK
# android.add_libs_armeabi = libs/armeabi/libexample.so

# (list) Other options
# android.release_sign = True

[buildozer]
# (bool) Log level (0=debug, 1=info, 2=warning, 3=error)
log_level = 1

# (str) Path to the default build directory
build_dir = .buildozer

# (bool) Allow buildozer to automatically install missing dependencies
allow_autodeps = True

# (str) Path to the default virtualenv directory
virtualenv_dir = .buildozer/venv
