#!/bin/bash
echo "[ψONE] Iniciando estrutura completa do projeto Android..."

mkdir -p android/app/src/main/kotlin/com/psione android/gradle/wrapper

cat > android/gradle/wrapper/gradle-wrapper.properties <<G
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-7.6-all.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
G

cat > android/settings.gradle <<G
rootProject.name = 'psione'
include ':app'
G

cat > android/build.gradle <<G
buildscript {
    repositories { google(); mavenCentral() }
    dependencies { classpath 'com.android.tools.build:gradle:7.4.2' }
}
allprojects { repositories { google(); mavenCentral() } }
G

cat > android/gradle.properties <<G
org.gradle.jvmargs=-Xmx1536M
android.useAndroidX=true
android.enableJetifier=true
G

cat > android/app/build.gradle <<G
apply plugin: 'com.android.application'

android {
    compileSdkVersion 33
    namespace 'com.psione.app'
    defaultConfig {
        applicationId "com.psione.app"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "1.0"
    }
    buildTypes {
ls
cat > android/build.gradle <<EOF
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:7.4.2'
    }
}
allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
