# It's sick.
%define		_snapver	20020412
%define		_snap		%{_snapver}
%define		_ver	0.7
Summary:	Library for playing AVI files
Summary(pl):	Biblioteka do odtwarzania plik�w AVI
Name:		avifile
Version:	%{_ver}
Release:	0.%{_snap}.3
Epoch:		3
License:	GPL
Group:		X11/Libraries
URL:		http://avifile.sourceforge.net/
Source0:	http://avifile.sourceforge.net/%{name}%{version}-%{_snap}.tar.gz
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
%ifarch %{ix86}
BuildRequires:	divx4linux-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lame-libs-devel
BuildRequires:	xvid-devel
BuildConflicts:	wine-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Avifile is a library that allow programs to read and write compressed
AVI files (Indeo Video, DivX :-), etc.) under x86 Linux.
(De)compression is performed with various plugins (Win32, FFMpeg,...)

%description -l pl
Avifile jest bibliotek� s�u��c� do odczytywania i zapisywania
skompresowanych plik�w AVI (Indeo Video, DivX :-), etc.) pod Linuksem.
Do (de)kompresji u�ywane s� pluginy (win32, FFMpeg, ...)

%package devel
Summary:	Header file required to build programs using libavifile
Summary(pl):	Pliki nag��wkowe wymagane przez programy u�ywaj�ce libavifile
Group:		X11/Development/Libraries
Requires:	XFree86-devel
Requires:	%{name} = %{version}

%description devel
Header files required to build programs using libavifile.

%description devel -l pl
Pliki nag��wkowe niezb�dne do kompilacji program�w korzystaj�cych z
libavifile.

%package aviplay
Summary:	Player for AVI/ASF/WMF files
Summary(pl):	Odtwarzacz plik�w AVI/ASF/WMF
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description aviplay
Sample player for AVI, ASF, WFM (with straming support) files.

%description aviplay -l pl
Przyk�adowy odtwarzacz plik�w AVI, ASF, WFM (ze wsparciem dla
odtwarzania z sieci.)

%package utils
Summary:	Sample programs using the avifile library
Summary(pl):	Przyk�adowe programy u�ywaj�ce biblioteki avifile
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description utils
Qt-based AVI utilities with few other useful supporting tools for TV
capturing, AVI recompression, benchmarking, joining AVI files. These
programs have more bugs as they are not as extensively developed as
player.

%description utils -l pl
Kilka u�ytecznych narz�dzi do przechwytywania TV, rekompresji AVI,
benchmarkowania, ��czenia plik�w AVI. Maj� wi�cej b��d�w, poniewa� nie
s� tak intensywnie rozwijane jak odtwarzacz.

%ifarch %{ix86}
%package win32
Summary:	Win32 audio/video plugin
Summary(pl):	Plugin audio/video win32
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	w32codec

%description win32
Plugin for using Win32 DLL libraries in avifile located in
/usr/lib/win32.

%description win32 -l pl
Plugin do u�ywania w avifile zlokalizowanych w /usr/lib/win32
bibliotek DLL Win32.
%endif

%package ffmpeg
Summary:	GPL MPEG4 codec
Summary(pl):	Kodek MPEG4 na licencji GPL
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description ffmpeg
ffmpeg is a hyper fast realtime audio/video encoder, a streaming
server and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it
into several file formats based on DCT/motion compensation encoding.
Sound is compressed in MPEG audio layer 2 or using an AC3 compatible
stream.

%description ffmpeg -l pl
ffmpeg jest hiperszybkim koderem audio/wideo czasu rzeczywistego,
serwerem strumieni oraz standardowym konwerterem plik�w audio-wideo.

Mo�e pobiera� ze standardowego Video4Linux �r�d�o obrazu i konwertowa�
je do kilku format�w plik�w opartych na kodowaniu DCT/kompensacji
ruchu. D�wi�k jest kompresowany w MPEG audio layer 2 lub u�ywaj�c
kompatybilnego z AC3 strumienia.

%ifarch %{ix86}
%package divx4
Summary:	Fast MPEG4 codec
Summary(pl):	Szybki kodek MPEG4
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	divx4linux
ExclusiveArch:	%{ix86}

%description divx4
DivX MPEG-4 decoder and encoder.

%description divx4 -l pl
Dekoder i koder MPEG-4 DivX.
%endif

%package vorbis
Summary:	Vorbis audio plugin
Summary(pl):	Plugin vorbis audio.
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description vorbis
Plugin for decompression of Vorbis audio streams.

%description vorbis -l pl
Plugin do dekompresji strumieni audio Vorbis.

%package mad
Summary:	MAD - MPEG audio plugin
Summary(pl):	MAD - plugin MPEG audio
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description mad
Plugin for decompression of MPEG-1 Layer I/II/III audio streams.

%description mad -l pl
Plugin do dekompresji strumieni d�wi�kowych MPEG-1 Layer I/II/III.

%package lame_audioenc
Summary:	MP3 audio encoder plugin
Summary(pl):	Plugin enkoduj�cy d�wi�k w formacie MP3
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description lame_audioenc
Plugin for mp3 encoding capability of avirecompress tool.

%description lame_audioenc -l pl
Plugin umo�liwiaj�cy avirecompressowi kodowanie mp3.

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
	--enable-ffmpeg \
	--disable-x86opt

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
%attr(755,root,root) %{_libdir}/avifile*/libaudiodec.so*
%attr(755,root,root) %{_libdir}/avifile*/libaudiodec.la
%attr(755,root,root) %{_libdir}/avifile*/libmpeg_audiodec.so*
%attr(755,root,root) %{_libdir}/avifile*/libmpeg_audiodec.la
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

%ifarch %{ix86}
%files win32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libwin32.so*
%attr(755,root,root) %{_libdir}/avifile*/libwin32.la
%endif

%files ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libffmpeg.so*
%attr(755,root,root) %{_libdir}/avifile*/libffmpeg.la

%ifarch %{ix86}
%files divx4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/libdivx4.so*
%attr(755,root,root) %{_libdir}/avifile*/libdivx4.la
%endif

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
