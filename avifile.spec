%define		snap	20010809
Summary:	Library and sample program for playing AVI files
Summary(pl):	Biblioteka i przykładowy program do odtwarzania plików AVI
Name:		avifile
Version:	0.6
Release:	0.%{snap}.1
Epoch:		3
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://divx.euro.ru/%{name}-%{version}-%{snap}.tar.gz
Patch0:		%{name}-shareware.patch
Patch1:		%{name}-deplib.patch
Patch2:		%{name}-ac3.patch
Patch3:		%{name}-mga.patch
Patch4:		%{name}-size_t.patch
BuildRequires:	XFree86-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	ac3dec-devel >= 0.6.1
BuildRequires:	libjpeg-devel
BuildRequires:	unzip
BuildRequires:	qt-devel
BuildConflicts:	wine-devel
ExclusiveArch:	%{ix86}
Requires:	w32codec
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Library and sample program for playing AVI files. It uses windows
codecs and parts of Wine (http://www.winehq.com) code to load them.

%description -l pl
Biblioteka i przykładowy program do odtwarzania plików AVI.
Wykorzystuje dekompresory dla Windows oraz fragmenty kodu Wine
(http://www.winehq.com) aby je załadować.

%package devel
Summary:	Header file required to build programs using libaviplay
Summary(pl):	Pliki nagłówkowe wymagane przez programy używające libaviplay
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	XFree86-devel

%description devel
Header files required to build programs using libaviplay.

%description devel -l pl
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
libaviplay.

%prep
%setup -q
%patch0 -p1
# was broken and need fixing; without this xmms and avi plugin is broken
# %patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing aclocal.m4
libtoolize --copy --force
aclocal
autoconf
automake -a -c --foreign
%configure \
	--with-qt-includes=%{_includedir}/qt \
	--with-libac3-path=%{_prefix} \
	--enable-release \
	--enable-ffmpeg

touch lib/dummy.cpp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},/usr/lib/win32}

## avoid relinking
#for f in plugins/libwin32/libwin32.la plugins/libaudiodec/libaudiodec.la \
#  plugins/libmp3lame_audioenc/libmp3lame_audioenc.la \
#  plugins/libmpeg_audiodec/libmpeg_audiodec.la ; do
#	sed -e '/^relink_command/d' $f > $f.new
#	mv -f $f.new $f
#done
	
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf README doc/{CREDITS,EXCEPTIONS,KNOWN_BUGS,LICENSING} \
	doc/{README-DEVEL,TODO,VIDEO-PERFORMANCE,WARNINGS}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/{CREDITS,EXCEPTIONS,KNOWN_BUGS,LICENSING}.gz
%doc doc/{TODO,VIDEO-PERFORMANCE,WARNINGS}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/avifile*
%attr(755,root,root) %{_libdir}/avifile*/lib*.so*
%attr(755,root,root) %{_libdir}/avifile*/lib*.la
%{_datadir}/%{name}*

%files devel
%defattr(644,root,root,755)
%doc doc/README-DEVEL*
%attr(755,root,root) %{_bindir}/avifile-config
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/%{name}
