# It's sick.
#
# Conditional build:
# _without_qt		- disables QT support
# _with_divx		- enables divx4linux support (proprietary, binary-only
#			  lib)  note: if disabled, divx is decoded by ffmpeg
#
%define		_snapver	20030107
%define		_snap		%{_snapver}
Summary:	Library for playing AVI files
Summary(pl):	Biblioteka do odtwarzania plik�w AVI
Summary(pt_BR):	Biblioteca para reproduzir formatos de �udio e v�deo usando bin�rios win32
Name:		avifile
Version:	0.7.24
Release:	0.%{_snap}.%{?_with_divx:+divx}
Epoch:		3
License:	GPL
Group:		X11/Libraries
Source0:	%{name}0.7-%{version}-%{_snap}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-shareware.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-configure.patch
Patch3:		%{name}-fix-keys.patch
Patch4:		%{name}-xft.patch
URL:		http://avifile.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	a52dec-libs-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?_with_divx:BuildRequires:	divx4linux-devel}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	nas-devel
%{?!_without_qt:BuildRequires:	qt-devel >= 2.0.0}
BuildRequires:	unzip
%ifarch %{ix86} ppc
BuildRequires:	xvid-devel
%endif
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

%description -l pt_BR
Avifile busca criar uma biblioteca us�vel de suporte a arquivos AVI e
um conjunto b�sico de utilit�rios (para reprodu��o, captura e edi��o)
para o Linux. Cont�m classes C++ para leitura e cria��o de AVIs e
interfaces para compressores e descompresseores de �udio e v�deo.

%package devel
Summary:	Header file required to build programs using libavifile
Summary(pl):	Pliki nag��wkowe wymagane przez programy u�ywaj�ce libavifile
Summary(pt_BR):	Componentes para desenvolvimento com a avifile
Group:		X11/Development/Libraries
Requires:	XFree86-devel
Requires:	%{name} = %{version}

%description devel
Header files required to build programs using libavifile.

%description devel -l pl
Pliki nag��wkowe niezb�dne do kompilacji program�w korzystaj�cych z
libavifile.

%description devel -l pt_BR
Componentes para desenvolvimento com a avifile.

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

%package divx
Summary:	Fast MPEG4 codec
Summary(pl):	Szybki kodek MPEG4
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	divx4linux
Obsoletes:	avifile-divx4

%description divx
DivX MPEG-4 decoder and encoder.

%description divx -l pl
Dekoder i koder MPEG-4 DivX.

%package vorbis
Summary:	Vorbis audio plugin
Summary(pl):	Plugin vorbis audio
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

%package xvid
Summary:	XVID codec
Summary(pl):	Kodek XVID
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	xvid

%description xvid
XVID decoder and encoder.

%description xvid -l pl
Dekoder i koder XVID.

%prep
%setup -q -n avifile0.7-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
#rm -f missing aclocal.m4
#%%{__libtoolize}
#%%{__aclocal} -I m4
#%%{__autoheader}
#%%{__autoconf}
#%%{__automake}

#cd plugins/libmad/libmad
#%%{__autoconf}
#cd ../../..

#cd libmmxnow
#%%{__autoconf}
#cd ..

./autogen.sh

# This is The WRONG Way (tm)
%if %{!?_without_qt:1}%{?_without_qt:0}
GEN_MOC="`grep -Rl '^ *Q_OBJECT$' *`"
for f in $GEN_MOC; do moc -o "${f%.[!.]*}.moc" "$f"; done
%endif

#Temporary removed -I/usr/include/freetype2 cause it break build, I don't know why :(

%configure \
	CPPFLAGS="-I/usr/include/divx -I/usr/include/xvid -I/usr/include/freetype2" \
	AS="%{__cc}" \
	FFMPEG_CFLAGS="%{rpmcflags} -ffast-math %{!?debug:-fomit-frame-pointer}" \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir} \
	--enable-a52 \
	--enable-release \
	--enable-ffmpeg \
	--enable-ffmpeg-a52 \
	%{?_with_divx:--enable-divx4} \
%ifarch i586 i686 athlon
	--enable-x86opt \
%else
	--disable-x86opt \
%endif
	%{?_without_qt:--without-qt} \
	%{?_without_qt:--disable-samples}

touch lib/dummy.cpp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},/usr/lib/win32,%{_pixmapsdir},%{_applnkdir}/Multimedia}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	m4datadir="%{_aclocaldir}"

cp -f include/fourcc.h $RPM_BUILD_ROOT/%{_includedir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install bin/test.png $RPM_BUILD_ROOT%{_pixmapsdir}/avifile.png

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{CREDITS,EXCEPTIONS,KNOWN_BUGS,LICENSING}
%doc doc/{README-DEVEL,TODO,VIDEO-PERFORMANCE,WARNINGS}
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/avifile*
%attr(755,root,root) %{_libdir}/avifile*/audiodec.so*
%{_libdir}/avifile*/audiodec.la
%attr(755,root,root) %{_libdir}/avifile*/mpeg_audiodec.so*
%{_libdir}/avifile*/mpeg_audiodec.la
%attr(755,root,root) %{_libdir}/avifile*/ac3pass.so*
%{_libdir}/avifile*/ac3pass.la
%attr(755,root,root) %{_libdir}/avifile*/mjpeg.so*
%{_libdir}/avifile*/mjpeg.la

%files devel
%defattr(644,root,root,755)
%doc doc/README-DEVEL*
%attr(755,root,root) %{_bindir}/avifile-config
%attr(755,root,root) %{_bindir}/mmxnow-config
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/%{name}
%{_includedir}/*.h
%{_aclocaldir}/*.m4

%if %{?_without_qt:0}%{!?_without_qt:1}
%files aviplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aviplay
%{_mandir}/man1/aviplay.1*
%{_datadir}/%{name}*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avi[bcmrt]*
%attr(755,root,root) %{_bindir}/kv4lsetup
%endif

%ifarch %{ix86}
%files win32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/win32.so*
%{_libdir}/avifile*/win32.la
%endif

%files ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/ffmpeg.so*
%{_libdir}/avifile*/ffmpeg.la

%if %{?_with_divx:1}%{!?_with_divx:0}
%files divx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/divx*.so*
%{_libdir}/avifile*/divx*.la
%endif

%files vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vorbis*.so*
%{_libdir}/avifile*/vorbis*.la

%files mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/mad*.so*
%{_libdir}/avifile*/mad*.la

%files lame_audioenc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/mp3lamebin_audioenc.so*
%{_libdir}/avifile*/mp3lamebin_audioenc.la

%ifarch %{ix86} ppc
%files xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/xvid.so*
%{_libdir}/avifile*/xvid.la
%endif