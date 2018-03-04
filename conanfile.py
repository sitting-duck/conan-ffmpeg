from conans import ConanFile, tools
from conans.tools import download, unzip
import os
import shutil


class FfmpegConan(ConanFile):
    name = "ffmpeg"
    description = "Conan package for FFmpeg on Windows."
    version = "3.4.1"
    license = "MIT"
    url = "https://bitbucket.org/genvidtech/conan-ffmpeg"
    author = "Robert Leclair (rleclair@genvidtech.com)"
    settings = {"os": ["Windows", "Linux"], 
                "compiler" : ["Visual Studio", "gcc"], 
                "build_type" : ["Release", "Debug"], 
                "arch" : ["x86", "x86_64"] }
    generators = "txt"
    requires = "lame/3.100@conan-cpp/latest"
    options = {"shared": [True, False], "pic": [True,False], "decoder": "ANY", "encoder": "ANY"}
    default_options = "shared=False", "pic=False", "lame:shared=False", "decoder=", "encoder="

    def run_bash(self, cmd):
        if self.settings.os == "Windows":
            tools.run_in_windows_bash(self, cmd)
        else:
            self.run(cmd)

    def source(self):
        zip_name = "ffmpeg.zip"
        download("https://github.com/FFmpeg/FFmpeg/archive/n%s.zip" % self.version, zip_name)
        unzip(zip_name)
        shutil.move("FFmpeg-n%s" % self.version, "ffmpeg")
        os.unlink(zip_name)
        if self.settings.os=="Linux":
            self.run_bash("chmod +x ffmpeg/configure")
            self.run_bash("find ffmpeg -name '*.sh' -exec chmod +x {} \\;")

    def build(self):
        lame_info = self.deps_cpp_info["lame"]
        lame_library = lame_info.lib_paths[0]
        lame_include = lame_info.include_paths[0]
        CPPFLAGS = "\"-I%s\"" % lame_include 
        LDFLAGS = "\"-L%s\"" % lame_library

        configure_cmd = "./configure "
        if not self.options.shared:
            configure_cmd += " --enable-static "
        else:
            configure_cmd += " --enable-shared "

        if self.options.pic:
            configure_cmd += " --enable-pic "

        if self.options.decoder:
            configure_cmd += " --disable-decoders "
            decoder_option = "%s" % self.options.decoder
            for d in decoder_option.split(","):
                configure_cmd += " --enable-decoder=" + d

        if self.options.encoder:
            configure_cmd += " --disable-encoders "
            encoder_option = "%s" % self.options.encoder
            for d in encoder_option.split(","):
                configure_cmd += " --enable-encoder=" + d

        configure_cmd += " --disable-devices --disable-programs --enable-libmp3lame --extra-cflags=%s --extra-ldflags=%s --enable-nonfree" % (CPPFLAGS, LDFLAGS)

        self.output.info(configure_cmd)

        with tools.chdir("ffmpeg") :
            if self.settings.os=="Windows":
                configure_cmd += " --toolchain=msvc"
            if self.settings.build_type == "Debug":
                configure_cmd += " --enable-debug" 
            self.run_bash(configure_cmd)
            self.run_bash("make")
 
    def package(self):
        self.copy("*.h", dst="include/libavcodec", src="ffmpeg/libavcodec")
        self.copy("*.h", dst="include/libavfilter", src="ffmpeg/libavfilter")
        self.copy("*.h", dst="include/libavformat", src="ffmpeg/libavformat")
        self.copy("*.h", dst="include/libavutil", src="ffmpeg/libavutil")
        self.copy("*.h", dst="include/libavcodec", src="ffmpeg/libavcodec")
        self.copy("*.h", dst="include/libswresample", src="ffmpeg/libswresample")
        self.copy("*.h", dst="include/libswscale", src="ffmpeg/libswscale")
        self.copy("*.lib", dst="lib", src="ffmpeg", keep_path=False)
        self.copy("*-*.dll", dst="bin", src="ffmpeg", keep_path=False)
        self.copy("*.so", dst="lib", src="ffmpeg", keep_path=False)
        self.copy("*.so.*", dst="lib", src="ffmpeg", keep_path=False)
        self.copy("*.a", dst="lib", src="ffmpeg", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [ "avformat", "avcodec", "avfilter", "swresample",
                               "swscale", "avutil" ]

