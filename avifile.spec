# It's sick.
%define		_snapver	20011220
%define		_snapsubver	admin
%define		_snap		%{_snapver}%{_snapsubver}
%define		_ver	0.6
%define		_subver	.0
Summary:	Library and sample program for playing AVI files
Summary(pl):	Biblioteka i przyk³adowy program do odtwarzania plików AVI
Name:		avifile
Version:	%{_ver}%{_subver}
Release:	0.%{_snap}.1
Epoch:		3
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://avifile.sourceforge.net/%{name}-%{version}-%{_snap}.tgz
Patch0:		%{name}-shareware.patch
Patch1:		%{name}-deplib.patch
Patch2:		%{name}-ac3.patch
Patch3:		%{name}-size_t.patch
Patch4:		%{name}-amfix.patch
BuildRequires:	XFree86-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	ac3dec-devel >= 0.6.1
BuildRequires:	libjpeg-devel
BuildRequires:	unzip
BuildRequires:	qt-devel
BuildRequires:	divx4linux-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lame-libs-devel
BuildConflicts:	wine-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Library and sample program for playing AVI files. It can use windows
codecs and parts of Wine (http://www.winehq.com) code to play some of
them.

%description -l pl
Biblioteka i przyk³adowy program do odtwarzania plików AVI. Mo¿e
wykorzystaæ dekompresory dla Windows oraz fragmenty kodu Wine
(http://www.winehq.com) aby czê¶æ z nich odtworzyæ.

%package devel
Summary:	Header file required to build programs using libaviplay
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce libaviplay
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	XFree86-devel

%description devel
Header files required to build programs using libaviplay.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
libaviplay.

%prep
%setup -q -n avifile%{_ver}-%{_snapver}
%patch0 -p1
# was broken and need fixing; without this xmms and avi plugin is broken
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing aclocal.m4
libtoolize --copy --force
aclocal
autoconf
autoheader
automake -a -c --foreign

cd plugins/libmad/libmad
autoconf
cd ../../..

cd libmmxnow
autoconf
cd ..

# This is The WRONG Way (tm)
GEN_MOC="`grep -Rl '^ *Q_OBJECT$' *`"
for f in $GEN_MOC; do moc -o "${f%.[!.]*}.moc" "$f"; done

%configure CPPFLAGS="-I/usr/include/divx" AS="%{__cc}" \
	--with-qt-includes=%{_includedir}/qt \
	--with-libac3-path=%{_prefix} \
	--enable-release \
	--enable-ffmpeg

touch lib/dummy.cpp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},/usr/lib/win32}

# avoid relinking
for f in plugins/*/lib*.la ; do
	sed -e '/^relink_command/d' $f > $f.new
	mv -f $f.new $f
done
	
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

cp -f include/fourcc.h $RPM_BUILD_ROOT/%{_includedir}/%{name}

gzip -9nf README doc/{CREDITS,EXCEPTIONS,KNOWN_BUGS,LICENSING} \
	doc/{README-DEVEL,TODO,VIDEO-PERFORMANCE,WARNINGS}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/{CREDITS,EXCEPTIONS,KNOWN_BUGS,LICENSING}.gz
%doc doc/{TODO,VIDEO-PERFORMANCE,WARNINGS}.gz
%attr(755,root,root) %{_bindir}/avi[bcmprt]*
%attr(755,root,root) %{_bindir}/kv4lsetup
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/avifile*
%attr(755,root,root) %{_libdir}/avifile*/lib*.so*
%attr(755,root,root) %{_libdir}/avifile*/lib*.la
%{_datadir}/%{name}*

%files devel
%defattr(644,root,root,755)
%doc doc/README-DEVEL*
%attr(755,root,root) %{_bindir}/avifile-config
%attr(755,root,root) %{_bindir}/mmxnow-config
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/%{name}
