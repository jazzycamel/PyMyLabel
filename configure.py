from PyQt5.QtCore import PYQT_CONFIGURATION as pyqt_config
from distutils import sysconfig
import os, sipconfig, sys

class HostPythonConfiguration(object):
    def __init__(self):
        self.platform=sys.platform
        self.version=sys.hexversion >> 8

        self.inc_dir=sysconfig.get_python_inc()
        self.venv_inc_dir=sysconfig.get_python_inc(prefix=sys.prefix)
        self.module_dir=sysconfig.get_python_lib(plat_specific=1)

        if sys.platform=='win32':
            self.data_dir=sys.prefix
            self.lib_dir=sys.prefix + '\\libs'
        else:
            self.data_dir=sys.prefix + '/share'
            self.lib_dir=sys.prefix + '/lib'

class TargetQtConfiguration(object):
    def __init__(self, qmake):
        pipe=os.popen(' '.join([qmake, '-query']))

        for l in pipe:
            l=l.strip()

            tokens=l.split(':', 1)
            if isinstance(tokens, list):
                if len(tokens) != 2:
                    error("Unexpected output from qmake: '%s'\n" % l)

                name,value=tokens
            else:
                name=tokens
                value=None

            name=name.replace('/', '_')
            setattr(self, name, value)

        pipe.close()        

if __name__=="__main__":
    from argparse import ArgumentParser

    parser=ArgumentParser(description="Configure PyMyLabel module.")
    parser.add_argument(
        '-q', '--qmake',
        dest="qmake",
        type=str,
        default="qmake",
        help="Path to qmake executable"
    )
    args=parser.parse_args()

    qmake_exe=args.qmake
    if not qmake_exe.endswith('qmake'):
        qmake_exe=os.path.join(qmake_exe,'qmake')

    if os.system(' '.join([qmake_exe, '-v']))!=0:
        
        if sys.platform=='win32':
            print("Make sure you have a working Qt qmake on your PATH.")
        else:
            print(
                "Use the --qmake argument to explicitly specify a "
                "working Qt qmake."
            )
        exit(1)

    pyconfig=HostPythonConfiguration()
    py_sip_dir=os.path.join(pyconfig.data_dir, 'sip', 'PyQt5')
    sip_inc_dir=pyconfig.venv_inc_dir

    qtconfig=TargetQtConfiguration(qmake_exe)

    inc_dir="src"
    lib_dir="src"
    dest_pkg_dir="PyMyLabel"
    sip_files_dir="sip"
    output_dir = "modules"
    build_file="PyMyLabel.sbf"
    build_path = os.path.join(output_dir, build_file)

    if not os.path.exists("modules"): os.mkdir("modules")       
    if not os.path.exists(output_dir): os.mkdir(output_dir)

    sip_file = os.path.join("sip", "PyMyLabel.sip")

    config=sipconfig.Configuration()    
    config.default_mod_dir=( "/usr/local/lib/python%i.%i/dist-packages" %
                               ( sys.version_info.major, sys.version_info.minor ) )

    cmd=" ".join([
        config.sip_bin,
        pyqt_config['sip_flags'],
        '-I', py_sip_dir,
        '-I', config.sip_inc_dir,
        '-I', inc_dir,
        "-c", output_dir,
        "-b", build_path,
        "-w",
        "-o",
        sip_file,
    ])

    print(cmd)
    if os.system(cmd)!=0: sys.exit(1)

    makefile=sipconfig.SIPModuleMakefile(
        config,
        build_file,
        dir=output_dir,
        install_dir=dest_pkg_dir
    )

    makefile.extra_include_dirs+=[
        os.path.abspath(inc_dir),
        qtconfig.QT_INSTALL_HEADERS,
        qtconfig.QT_INSTALL_LIBS+'/QtCore.framework/Headers',
        qtconfig.QT_INSTALL_LIBS+'/QtGui.framework/Headers',
        qtconfig.QT_INSTALL_LIBS+'/QtWidgets.framework/Headers',
    ]
    makefile.extra_defines+=['QT_CORE_LIB', 'QT_GUI_LIB', 'QT_WIDGETS_LIB']
    makefile.extra_cxxflags+=['-F'+qtconfig.QT_INSTALL_LIBS]
    makefile.extra_lib_dirs+=[os.path.abspath(lib_dir)]
    makefile.extra_libs+=['MyLabel']
    makefile.extra_lflags+=[
        '-L.',
        "-L"+qtconfig.QT_INSTALL_LIBS,
        '-F'+qtconfig.QT_INSTALL_LIBS,
        "-framework QtWidgets",
        "-framework QtGui",
        "-framework QtCore",
        "-framework DiskArbitration",
        "-framework IOKit",
        "-framework OpenGL",
        "-framework AGL",
    ]
    makefile.generate()

    sipconfig.ParentMakefile(
        configuration = config,
        subdirs = ["src", output_dir],
    ).generate()

    os.chdir("src")
    os.system(qmake_exe)
    sys.exit()
