Summary:	The BSD 4.4 version of make
Name:		pmake
Version:	1.45
Release:	%mkrel 13
Epoch:		1
License:	BSD
Group:		Development/Other
Source0:	http://ftp.debian.org/debian/dists/potato/main/source/devel/%{name}_%{version}-3.2.tar.bz2
Patch0:         pmake-1.45-gcc4.patch
Patch1:		pmake_1.45-3.2-LDFLAGS.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
	CC=gcc \
        LDFLAGS="%{ldflags}"
touch build


%install
rm -rf %{buildroot}

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc PSD.doc/tutorial.ms
%{_bindir}/*
%dir %{_datadir}/mk
%{_datadir}/mk/*
%{_mandir}/man1/*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.45-11mdv2011.0
+ Revision: 667791
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.45-10mdv2011.0
+ Revision: 607184
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.45-9mdv2010.1
+ Revision: 520200
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:1.45-8mdv2010.0
+ Revision: 426732
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.45-7mdv2009.1
+ Revision: 317536
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1:1.45-6mdv2009.0
+ Revision: 225017
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1:1.45-5mdv2008.1
+ Revision: 125454
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.45-5mdv2007.1
+ Revision: 145406
- Import pmake

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.45-5mdv2007.1
- use the %%mrel macro
- bunzip patches

* Sun Jul 31 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.45-4mdk
- Patch 0 :  Fix Build with gcc4 ( from Fedora )

