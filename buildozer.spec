[app]

# （必填）应用标题，显示在手机桌面上
title = AES加密工具

# （必填）包名，唯一标识你的应用
package.name = aesencrypt
package.domain = org.yourname

# （必填）应用版本
version = 1.0.0

# （必填）你的主程序入口文件
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 你的应用依赖哪些Python库（重点！）
requirements = python3,kivy,pycryptodome

# 是否全屏
fullscreen = 0

# 屏幕方向（portrait=竖屏，landscape=横屏）
orientation = portrait

# Android相关配置
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

# 图标和启动画面（可选，暂时注释掉）
# android.icon = icon.png
# android.presplash = presplash.png

# iOS相关配置（不用管）
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.codesign.allowed = false

[buildozer]
# 构建时的日志级别（1=默认, 2=详细）
log_level = 2

# 警告级别（0=不警告）
warn_on_root = 0