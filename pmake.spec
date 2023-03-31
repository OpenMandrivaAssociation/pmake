Summary:	The BSD 4.4 version of make
Name:		pmake
Epoch:		1
Version:	1.45
Release:	23
License:	BSD
Group:		Development/Other
Source0:	http://ftp.debian.org/debian/dists/potato/main/source/devel/%{name}_%{version}-3.2.tar.bz2
Patch0:		pmake-1.45-gcc4.patch
Patch1:		pmake_1.45-3.2-LDFLAGS.diff

%description
Make is a GNU tool which allows users to build and install programs
without any significant knowledge of the build process.  Details about
how the program should be built are included in the program's
Makefile.  Pmake is a particular version (BSD 4.4) of make.  Pmake
supports some additional syntax which is not in the standard make
program.  Some Berkeley programs have Makefiles written for pmake.

Pmake should be installed on your system so that you will be able to
build programs which require using pmake instead of make.

%prep
%setup -q
%patch0 -p1 -b .gcc4
%patch1 -p0 -b .LDFLAGS

%build
make -f Makefile.boot \
        CFLAGS="%{optflags} \
	-D__COPYRIGHT\(x\)= \
	-D__RCSID\(x\)= \
	-I. \
	-DMACHINE=\\\"mandrake\\\" \
	-DMACHINE_ARCH=\\\"`arch`\\\"" \
	CC=%{__cc} \
        LDFLAGS="%{ldflags}"
touch build

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1

install bmake %{buildroot}/%{_bindir}/pmake
install -m 755 mkdep %{buildroot}/%{_bindir}
install make.1 %{buildroot}/%{_mandir}/man1/pmake.1
install mkdep.1 %{buildroot}/%{_mandir}/man1

install -d %{buildroot}/%{_datadir}/mk
for file in mk/*; do
    install -m 644 $file %{buildroot}/%{_datadir}/mk
done

%files
%doc PSD.doc/tutorial.ms
%{_bindir}/*
%dir %{_datadir}/mk
%{_datadir}/mk/*
%{_mandir}/man1/*

