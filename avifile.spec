# It's sick.
%define		_snapver	20011220
%define		_snapsubver	admin
%define		_snap		%{_snapver}%{_snapsubver}
%define		_ver	0.6
%define		_subver	.0
Summary:	Library for playing AVI files
Summary(pl):	Biblioteka do odtwarzania plików AVI
Name:		avifile
Version:	%{_ver}%{_subver}
Release:	0.%{_snap}.4
Epoch:		3
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
URL:		http://avifile.sourceforge.net/
Source0:	http://avifile.sourceforge.net/%{name}-%{version}-%{_snap}.tgz
Source1:	%{name}.desktop
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Avifile is a library that allow programs to read and write compressed
AVI files (Indeo Video, DivX :-), etc.) under x86 Linux.
(De)compression is performed with various plugins (Win32, FFMpeg,...)

%description -l pl
Avifile jest bibliotek± s³u¿±c± do odczytywania i zapisywania
skompresowanych plików AVI (Indeo Video, DivX :-), etc.) pod Linuksem.
Do (de)kompresji u¿ywane s± pluginy (win32, FFMpeg, ...)

%package devel
Summary:	Header file required to build programs using libavifile
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce libavifile
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	XFree86-devel
Requires:	%{name} = %{version}

%description devel
Header files required to build programs using libavifile.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
libavifile.

%package aviplay
Summary:	Player for AVI/ASF/WMF files
Summary(pl):	Odtwarzacz plików AVI/ASF/WMF
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description aviplay
Sample player for AVI, ASF, WFM (with straming support) files.

%description aviplay -l pl
Przyk³adowy odtwarzacz plików AVI, ASF, WFM (ze wsparciem dla
odtwarzania z sieci.)

%package utils
Summary:	Sample programs using the avifile library
Summary(pl):	Przyk³adowe programy u¿ywaj±ce biblioteki avifile
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description utils
Qt-based AVI utilities with few other useful supporting tools for TV
capturing, AVI recompression, benchmarking, joining AVI files. These
programs have more bugs as they are not as extensively developed as
player.

%description utils -l pl
Kilka u¿ytecznych narzêdzi do przechwytywania TV, rekompresji AVI,
benchmarkowania, ³±czenia plików AVI. Maj± wiêcej b³êdów, poniewa¿ nie
s± tak intensywnie rozwijane jak odtwarzacz.

%package win32
Summary:	Win32 audio/video plugin
Summary(pl):	Plugin audio/video win32
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	w32codec
ExclusiveArch:	%{ix86}

%description win32
Plugin for using Win32 DLL libraries in avifile located in
/usr/lib/win32

%package ffmpeg
Summary:	GPL MPEG4 codec
Summary(pl):	Kodek MPEG4 na licencji GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description ffmpeg
ffmpeg is a hyper fast realtime audio/video encoder, a streaming
server and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it
into several file formats based on DCT/motion compensation encoding.
Sound is compressed in MPEG audio layer 2 or using an AC3 compatible
stream.

%package divx4
Summary:	Fast MPEG4 codec
Summary(pl):	Szybki kodek MPEG4
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	divx4linux
ExclusiveArch:	%{ix86}

%description divx4
DivX MPEG-4 decoder and encoder.

%description divx4 -l pl
Dekoder i koder MPEG-4 DivX.

%package vorbis
Summary:	Vorbis audio plugin
Summary(pl):	Plugin vorbis audio.
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description vorbis
Plugin for decompression of Vorbis audio streams.

%package mad
Summary:	MAD - MPEG audio plugin
Summary(pl):	MAD - plugin MPEG audio
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description mad
Plugin for decompression of MPEG-1 Layer I/II/III audio streams.

%description mad -l pl
Plugin do dekompresji strumieni d¼wiêkowych MPEG-1 Layer I/II/III.

%package lame_audioenc
Summary:	MP3 audio encoder plugin
Summary(pl):	Plugin enkoduj±cy d¼wiêk w formacie MP3
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description lame_audioenc
Plugin for mp3 encoding capability of avirecompress tool.

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},/usr/lib/win32,%{_pixmapsdir},%{_applnkdir}/Multimedia}

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

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install bin/test.png $RPM_BUILD_ROOT%{_pixmapsdir}/avifile.png

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/{CREDITS,EXCEPTIONS,KNOWN_BUGS,LICENSING}.gz
%doc doc/{TODO,VIDEO-PERFORMANCE,WARNINGS}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/avifile*
%attr(755,root,root) %{_libdir}/avifile*/lib*audiodec.so*
%attr(755,root,root) %{_libdir}/avifile*/lib*audiodec.la
%attr(755,root,root) %{_libdir}/avifile*/libac3pass.so*
%attr(755,root,root) %{_libdir}/avifile*/libac3pass.la
%attr(755,root,root) %{_libdir}/avifile*/libmjpeg.so*
%attr(755,root,root) %{_libdir}/avifile*/libmjpeg.la

%files devel
%defattr(644,root,root,755)
%doc doc/README-DEVEL*
%attr(755,root,root) %{_bindir}/avifile-config
%attr(755,root,root) %{_bindir}/mmxnow-config
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/%{name}

%files aviplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aviplay
%{_datadir}/%{name}*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avi[bcmrt]*
%attr(755,root,root) %{_bindir}/kv4lsetup

%files win32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libwin32.so*
%attr(755,root,root) %{_libdir}/avifile*/libwin32.la

%files ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libffmpeg.so*
%attr(755,root,root) %{_libdir}/avifile*/libffmpeg.la

%files divx4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libdivx4.so*
%attr(755,root,root) %{_libdir}/avifile*/libdivx4.la

%files vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libvorbis*.so*
%attr(755,root,root) %{_libdir}/avifile*/libvorbis*.la

%files mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libmad*.so*
%attr(755,root,root) %{_libdir}/avifile*/libmad*.la

%files lame_audioenc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libmp3lamebin_audioenc.so*
%attr(755,root,root) %{_libdir}/avifile*/libmp3lamebin_audioenc.la
