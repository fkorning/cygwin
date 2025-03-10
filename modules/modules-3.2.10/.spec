Name: modules
Version: 3.2.10
Release: 1
Summary: Environment Modules
Distribution: Berkeley Laboratory Distribution
Vendor: Lawrence Berkeley National Laboratory
Packager: Eric Roman <eroman@lbl.gov> (modified by R.K.Owen <rk@owen.sj.ca.us>
Group: Utilities/Shell
Copyright: GPL
Source:  ftp://modules.sourceforge.net/pub/modules/modules-3.2.10.tar.gz

%description
The Modules package provides for the dynamic modification of a user's
environment via modulefiles.  Each modulefile contains the information
needed to configure the shell for an application. Once the Modules
package is initialized, the environment can be modified dynamically
on a per-module basis using the module command which interprets
modulefiles. Typically modulefiles instruct the module command to alter or
set shell environment variables such as PATH, MANPATH, etc. modulefiles
may be shared by many users on a system and users may have their own
collection to supplement or replace the shared modulefiles.  The modules
environment is common on SGI/Crays and many workstation farms.


# prep section.  Tell RPM how to untar.
%prep
%setup -n modules-3.2.10
%patch

# build section.  Tell RPM how to run make
%buildroot /usr/local/Modules/test
%build
./configure \
		--prefix=/usr \
                --with-version-path=/usr/local/Modules/versions \
                --with-module-path=/usr/local/Modules/modulefiles \
		--with-etc-path=/etc \
		--with-skel-path=/etc/skel \
                --x-include=/usr/include/X11 \
                --x-libraries=/usr/X11R6/lib
                --with-tcl-include=/usr/include \
                --with-tcl-libraries=/usr/lib
make

%install
make install

%clean
rm -rf /usr/local/Modules/3.2.10

%files
# Tell RPM where to find the files that just spewed all over the disk...
/usr/bin/modulecmd
/etc/Modules/init/bash
/etc/Modules/init/csh 
/etc/Modules/init/perl
/etc/Modules/init/sh  
/etc/Modules/init/tcsh
/etc/Modules/init/zsh 
/etc/Modules/init/ksh 
/etc/Modules/init/.modulespath 
/usr/man/man1/module.1    
/usr/man/man4/modulefile.4
/etc/Modules/modulefiles/modules
/etc/Modules/modulefiles/module-info
/etc/Modules/modulefiles/module-cvs
/etc/Modules/modulefiles/null 
/etc/Modules/modulefiles/use.own
/etc/Modules/modulefiles/dot
