
As of Feb 2021 verfied to build in Ubuntu 18.04 by Brenly Drake and Ashley Tharp

On Windows 10 failing on Hp-Omen machine with this error: 
```
lame/3.100@conan-cpp/latest: Configuring sources in C:\Users\Ashley\.conan\data\lame\3.100\conan-cpp\latest\source

lame/3.100@conan-cpp/latest: Copying sources to build folder
lame/3.100@conan-cpp/latest: Building your package in C:\Users\Ashley\.conan\data\lame\3.100\conan-cpp\latest\build\3fb49604f9c2f729b85ba3115852006824e72cab
lame/3.100@conan-cpp/latest: Generator txt created conanbuildinfo.txt
lame/3.100@conan-cpp/latest: Calling build()
lame/3.100@conan-cpp/latest:
lame/3.100@conan-cpp/latest: ERROR: Package '3fb49604f9c2f729b85ba3115852006824e72cab' build failed
lame/3.100@conan-cpp/latest: WARN: Build folder C:\Users\Ashley\.conan\data\lame\3.100\conan-cpp\latest\build\3fb49604f9c2f729b85ba3115852006824e72cab
ERROR: lame/3.100@conan-cpp/latest: Error in build() method, line 44
        self.visual_build(config_options_string)
        AttributeError: 'LameConan' object has no attribute 'visual_build'

```

### Go here for Set Me Up Directions: 
https://bintray.com/squawkcpp/conan-cpp/ffmpeg%3Aconan-cpp

First do this: 
```
 conan remote add squawk https://api.bintray.com/conan/squawkcpp/conan-cpp
 conan user -p 330a9cf798349c1a3922718b51e0d207f668e47 -r squawk sitting-duck


```

## This repository holds a conan recipe for ffmpeg.

Tested by Brenly Drake and Ashley Tharp on Ubuntu 18.04. 
Does not build for MacOS

[![Build Status](https://travis-ci.org/spielhuus/conan-ffmpeg.svg?branch=master)](https://travis-ci.org/spielhuus/conan-ffmpeg)
[ ![Download](https://api.bintray.com/packages/squawkcpp/conan-cpp/ffmpeg%3Aconan-cpp/images/download.svg) ](https://bintray.com/squawkcpp/conan-cpp/ffmpeg%3Aconan-cpp)

[Conan.io](https://conan.io) package for [ffmpeg](https://www.ffmpeg.org) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/squawkcpp/conan-cpp/ffmpeg%3Aconan-cpp).

## Use this package

### Basic setup

    $ conan install ffmpeg/3.4.2@conan-cpp/latest

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    ffmpeg/3.4.2@conan-cpp/latest

    [options]
    ffmpeg:shared=[True, False]
    ffmpeg:pic=[True,False]
    ffmpeg:decoder={all|diable|comma seperated list of decoders}
    ffmpeg:encoder={all|diable|comma seperated list of encoders}
    ffmpeg:hwaccel={all|diable|comma seperated list of hwaccels}
    ffmpeg:muxer={all|diable|comma seperated list of muxers}
    ffmpeg:demuxer={all|diable|comma seperated list of demuxers}
    ffmpeg:parser={all|diable|comma seperated list of parsers}
    ffmpeg:bsf={all|diable|comma seperated list of bsfs}
    ffmpeg:protocol={all|diable|comma seperated list of protocols}
    ffmpeg:filter={all|diable|comma seperated list of filters}

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..
	
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git. 

### License
[Boost Software License](http://www.boost.org/LICENSE_1_0.txt) - Version 1.0 - August 17th, 2003

6
