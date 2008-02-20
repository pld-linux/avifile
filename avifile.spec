#
# Conditional build:
%bcond_without	qt	# don't build Qt-based utilities (incl. aviplay)
%bcond_with	divx	# enables divx4linux support (proprietary, binary-only
			# lib)  note: if disabled, divx is decoded by ffmpeg
%bcond_with	nas	# enable NAS support
#
Summary:	Library for playing AVI files
Summary(pl.UTF-8):	Biblioteka do odtwarzania plików AVI
Summary(pt_BR.UTF-8):	Biblioteca para reproduzir formatos de áudio e vídeo usando binários win32
Name:		avifile
Version:	0.7.45
Release:	8
Epoch:		3
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/avifile/%{name}-0.7-%{version}.tar.bz2
# Source0-md5:	7da94802f120d1b69e04a13170dcd21d
Source1:	%{name}.desktop
Patch0:		%{name}-shareware.patch
Patch1:		%{name}-fix-keys.patch
Patch2:		%{name}-etc_dir.patch
Patch3:		%{name}-aviplay_h.patch
Patch4:		%{name}-no_aux_dir.patch
Patch5:		%{name}-link_shared.patch
Patch6:		%{name}-no_libnsl.patch
Patch7:		%{name}-system-libmad.patch
Patch8:		%{name}-system_wide_ffmpeg.patch
Patch9:		%{name}-opt.patch
Patch10:	%{name}-opts.patch
Patch11:	%{name}-sparc.patch
Patch12:	%{name}-link.patch
Patch13:	%{name}-am.patch
Patch14:	%{name}-gcc4.patch
Patch15:	%{name}-compile.patch
Patch16:	%{name}-extern_c_ffmpeg.patch
Patch17:	%{name}-xf86dga.patch
Patch18:	%{name}-new_ffmpeg.patch
URL:		http://avifile.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	a52dec-libs-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_divx:BuildRequires:	divx4linux-devel}
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
%ifarch ppc
# version with altivec support fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libvorbis-devel >= 1:1.0
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt-devel >= 2.0.0}
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xvid-devel >= 1:1.0.0
BuildConflicts:	wine-devel
Obsoletes:	avifile-vidix-nvidia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing -D__STDC_CONSTANT_MACROS

%description
Avifile is a library that allow programs to read and write compressed
AVI files (Indeo Video, DivX ;-), etc.) under x86 Linux.
(De)compression is performed with various plugins (Win32, FFMpeg,...)

%description -l pl.UTF-8
Avifile jest biblioteką służącą do odczytywania i zapisywania
skompresowanych plików AVI (Indeo Video, DivX ;-), etc.) pod Linuksem.
Do (de)kompresji używane są wtyczki (win32, FFMpeg...).

%description -l pt_BR.UTF-8
Avifile busca criar uma biblioteca usável de suporte a arquivos AVI e
um conjunto básico de utilitários (para reprodução, captura e edição)
para o Linux. Contém classes C++ para leitura e criação de AVIs e
interfaces para compressores e descompresseores de áudio e vídeo.

%package devel
Summary:	Header file required to build programs using libavifile
Summary(pl.UTF-8):	Pliki nagłówkowe wymagane przez programy używające libavifile
Summary(pt_BR.UTF-8):	Componentes para desenvolvimento com a avifile
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXv-devel
Requires:	xorg-lib-libXxf86dga-devel
Requires:	xorg-lib-libXxf86vm-devel
Requires:	zlib-devel

%description devel
Header files required to build programs using libavifile.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
libavifile.

%description devel -l pt_BR.UTF-8
Componentes para desenvolvimento com a avifile.

%package qt
Summary:	Qt-based AVI utilities
Summary(pl.UTF-8):	Oparte na bibliotece Qt narzędzia do plików AVI
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description qt
Qt-based AVI utilities.

%description qt -l pl.UTF-8
Oparte na bibliotece Qt narzędzia do plików AVI.

%package aviplay
Summary:	Player for AVI/ASF/WMF files
Summary(pl.UTF-8):	Odtwarzacz plików AVI/ASF/WMF
Group:		X11/Applications/Multimedia
Requires:	%{name}-qt = %{epoch}:%{version}-%{release}

%description aviplay
Sample player for AVI, ASF, WFM (with straming support) files.

%description aviplay -l pl.UTF-8
Przykładowy odtwarzacz plików AVI, ASF, WFM (ze wsparciem dla
odtwarzania z sieci.)

%package utils
Summary:	Sample programs using the avifile library
Summary(pl.UTF-8):	Przykładowe programy używające biblioteki avifile
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description utils
Qt-based AVI utilities with few other useful supporting tools for TV
capturing, AVI recompression, benchmarking, joining AVI files. These
programs have more bugs as they are not as extensively developed as
player.

%description utils -l pl.UTF-8
Kilka użytecznych narzędzi do przechwytywania TV, rekompresji AVI,
benchmarkowania, łączenia plików AVI. Mają więcej błędów, ponieważ nie
są tak intensywnie rozwijane jak odtwarzacz.

%package divx
Summary:	Fast MPEG4 codec
Summary(pl.UTF-8):	Szybki kodek MPEG4
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	divx4linux
Obsoletes:	avifile-divx4

%description divx
DivX MPEG-4 decoder and encoder.

%description divx -l pl.UTF-8
Dekoder i koder MPEG-4 DivX.

%package ffmpeg
Summary:	GPL MPEG4 codec
Summary(pl.UTF-8):	Kodek MPEG4 na licencji GPL
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ffmpeg
ffmpeg is a hyper fast realtime audio/video encoder, a streaming
server and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it
into several file formats based on DCT/motion compensation encoding.
Sound is compressed in MPEG audio layer 2 or using an AC3 compatible
stream.

%description ffmpeg -l pl.UTF-8
ffmpeg jest hiperszybkim koderem audio/wideo czasu rzeczywistego,
serwerem strumieni oraz standardowym konwerterem plików audio-wideo.

Może pobierać obraz ze standardowego źródła obrazu Video4Linux i
konwertować je do kilku formatów plików opartych na kodowaniu DCT i
kompensacji ruchu. Dźwięk jest kompresowany w formacie MPEG layer 2
lub przy użyciu strumienia kompatybilnego z AC3.

%package lame_audioenc
Summary:	MP3 audio encoder plugin
Summary(pl.UTF-8):	Wtyczka kodująca dźwięk w formacie MP3
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
# this library is dlopened
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Requires:	libmp3lame.so.0()(64bit)
%else
Requires:	libmp3lame.so.0
%endif
Requires:	lame-libs

%description lame_audioenc
Plugin for MP3 encoding capability of avirecompress tool.

%description lame_audioenc -l pl.UTF-8
Wtyczka umożliwiająca avirecompressowi kodowanie MP3.

%package mad
Summary:	MAD - MPEG audio plugin
Summary(pl.UTF-8):	MAD - wtyczka MPEG audio
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description mad
Plugin for decompression of MPEG-1 Layer I/II/III audio streams.

%description mad -l pl.UTF-8
Wtyczka do dekompresji strumieni dźwiękowych MPEG-1 Layer I/II/III.

%package vorbis
Summary:	Vorbis audio plugin
Summary(pl.UTF-8):	Wtyczka Vorbis audio
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vorbis
Plugin for decompression of Vorbis audio streams.

%description vorbis -l pl.UTF-8
Wtyczka do dekompresji strumieni audio Vorbis.

%package win32
Summary:	Win32 audio/video plugin
Summary(pl.UTF-8):	Wtyczka audio/video win32
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	w32codec

%description win32
Plugin for using Win32 DLL libraries in avifile located in
/usr/lib/win32.

%description win32 -l pl.UTF-8
Wtyczka do używania w avifile zlokalizowanych w /usr/lib/win32
bibliotek DLL Win32.

%package xvid
Summary:	XVID codec
Summary(pl.UTF-8):	Kodek XVID
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xvid

%description xvid
XVID decoder and encoder.

%description xvid -l pl.UTF-8
Dekoder i koder XVID.

%package vidix-driver-fb
Summary:	VIDIX driver for generic FrameBuffer
Summary(pl.UTF-8):	Sterownik VIDIX dla zwykłego FrameBuffera
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vidix-driver-fb
VIDIX driver for generic FrameBuffer.

%description vidix-driver-fb -l pl.UTF-8
Sterownik VIDIX dla zwykłego FrameBuffera.

%package vidix-driver-mach64
Summary:	VIDIX driver for ATI Mach64 video adapters
Summary(pl.UTF-8):	Sterownik VIDIX dla kart graficznych ATI Mach64
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vidix-driver-mach64
VIDIX driver for ATI Mach64 adapters.

%description vidix-driver-mach64 -l pl.UTF-8
Sterownik vidix dla kart graficznych ATI Mach64.

%package vidix-driver-mga
Summary:	VIDIX driver for MGA (Matrox) video adapters
Summary(pl.UTF-8):	Sterownik VIDIX dla kart graficznych MGA (Matrox)
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vidix-driver-mga
VIDIX driver for MGA (Matrox) video adapters.

%description vidix-driver-mga -l pl.UTF-8
Sterownik VIDIX dla kart graficznych MGA (Matrox).

%package vidix-driver-permedia
Summary:	VIDIX driver for Permedia video adapters
Summary(pl.UTF-8):	Sterownik VIDIX dla kart graficznych Permedia
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vidix-driver-permedia
VIDIX driver for Permedia video adapters.

%description vidix-driver-permedia -l pl.UTF-8
Sterownik VIDIX dla kart graficznych Permedia.

%package vidix-driver-radeon
Summary:	VIDIX driver for ATI Radeon video adapters
Summary(pl.UTF-8):	Sterownik VIDIX dla kart graficznych ATI Radeon
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vidix-driver-radeon
VIDIX driver for ATI Radeon video adapters.

%description vidix-driver-radeon -l pl.UTF-8
Sterownik VIDIX dla kart graficznych ATI Radeon.

%package vidix-driver-rage128
Summary:	VIDIX driver for ATI Rage128 video adapters
Summary(pl.UTF-8):	Sterownik VIDIX dla kart graficznych ATI Rage128
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vidix-driver-rage128
VIDIX driver for ATI Rage128 video adapters.

%description vidix-driver-rage128 -l pl.UTF-8
Sterownik VIDIX dla kart graficznych ATI Rage128.

%prep
%setup -q -n %{name}-0.7-%{version}
rm -rf ffmpeg m4/ffmpeg.m4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

# unwanted hack
rm -f m4/as.m4
# original file contains only m4/*.m4; must exist because of AC_INIT parameter
> acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CPPFLAGS="-I/usr/include/divx" \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir} \
	--enable-a52 \
	%{?with_divx:--enable-divx4} \
	--enable-lamebin \
	--disable-lame \
	--enable-libmad \
	--enable-release \
%ifarch %{ix86}
%ifnarch i386 i486
	--enable-x86opt \
%endif
%else
	--disable-x86opt \
%endif
	%{!?with_qt:--without-qt} \
	%{!?with_qt:--disable-samples}

touch lib/dummy.cpp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/lib/win32,%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

# conflicts with ???
mv -f $RPM_BUILD_ROOT%{_bindir}/kv4lsetup $RPM_BUILD_ROOT%{_bindir}/akv4lsetup
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/kv4lsetup.1 $RPM_BUILD_ROOT%{_mandir}/man1/akv4lsetup.1
%{__perl} -pi -e 's/(kv4l|k4vl)/akv4l/g' $RPM_BUILD_ROOT%{_mandir}/man1/akv4lsetup.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install bin/test.png $RPM_BUILD_ROOT%{_pixmapsdir}/avifile.png

# avifile dlopens *.so
rm -f $RPM_BUILD_ROOT%{_libdir}/avifile*/{,vidix/}*.la
# API not exported
rm -f $RPM_BUILD_ROOT%{_libdir}/libqavm*.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{CREDITS,EXCEPTIONS,KNOWN_BUGS,LICENSING}
%doc doc/{README-DEVEL,TODO,VIDEO-PERFORMANCE,WARNINGS}
%attr(755,root,root) %{_libdir}/libaviplay*.so.*.*
%dir %{_libdir}/avifile*
%attr(755,root,root) %{_libdir}/avifile*/ac3pass.so*
%attr(755,root,root) %{_libdir}/avifile*/audiodec.so*
%attr(755,root,root) %{_libdir}/avifile*/mpeg_audiodec.so*
%attr(755,root,root) %{_libdir}/avifile*/osmjpeg.so*
%ifarch %{ix86}
%dir %{_libdir}/avifile*/vidix
%endif

%files devel
%defattr(644,root,root,755)
%doc doc/README-DEVEL*
%attr(755,root,root) %{_bindir}/avifile-config
%attr(755,root,root) %{_libdir}/libaviplay*.so
%{_libdir}/lib*.la
%{_includedir}/avifile*
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/avifile.pc
%{_mandir}/man1/avifile-config.1*

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avicap
%attr(755,root,root) %{_bindir}/avirecompress
%attr(755,root,root) %{_libdir}/libqavm-*.so.*.*
%{_mandir}/man1/avicap.1*
%{_mandir}/man1/avirecompress.1*

%files aviplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aviplay
%{_mandir}/man1/aviplay.1*
%{_datadir}/%{name}*
%{_desktopdir}/avifile.desktop
%{_pixmapsdir}/avifile.png
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akv4lsetup
%attr(755,root,root) %{_bindir}/avibench
%attr(755,root,root) %{_bindir}/avicat
%attr(755,root,root) %{_bindir}/avimake
%attr(755,root,root) %{_bindir}/avirec
%attr(755,root,root) %{_bindir}/avitype
%{_mandir}/man1/akv4lsetup.1*
%{_mandir}/man1/avibench.1*
%{_mandir}/man1/avicat.1*
%{_mandir}/man1/avimake.1*
%{_mandir}/man1/avirec.1*
%{_mandir}/man1/avitype.1*

%if %{with divx}
%files divx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/divx4.so
%endif

%files ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/ffmpeg.so

%files lame_audioenc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/mp3lamebin_audioenc.so
#%attr(755,root,root) %{_libdir}/avifile*/mp3lame_audioenc.so

%files mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/mad_audiodec.so

%files vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vorbis_audio.so

%ifarch %{ix86}
%files win32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/win32.so
%endif

%files xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/xvid4.so

%ifarch %{ix86}
%files vidix-driver-fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vidix/libgenfb.so

%files vidix-driver-mach64
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vidix/libmach64.so

%files vidix-driver-mga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vidix/libmga*.so

%files vidix-driver-permedia
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vidix/libpm3.so

%files vidix-driver-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vidix/libradeon.so

%files vidix-driver-rage128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/avifile*/vidix/librage128.so
%endif
