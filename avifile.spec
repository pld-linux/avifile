Summary:	Library and sample program for playing AVI files
Summary(pl):	Biblioteka i przyk³adowy program do odtwarzania plików AVI
Name:		avifile
Version:	0.6.0
Release:	0.beta4.3
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://divx.euro.ru/%{name}-%{version}-beta4.1.tar.gz
Patch0:		%{name}-shareware.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-am_fix.patch
Patch3:		%{name}-deplib.patch
Requires:	avi-codecs
BuildRequires:	unzip
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRequires:	SDL-devel >= 1.1.3
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	arts-devel
BuildConflicts:	wine-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Library and sample program for playing AVI files. It uses windows
codecs and parts of Wine (http://www.winehq.com) code to load them.

%description -l pl
Biblioteka i przyk³adowy program do odtwarzania plików AVI.
Wykorzystuje dekompresory dla Windows oraz fragmenty kodu Wine
(http://www.winehq.com) aby je za³adowaæ.

%package devel
Summary:	Header file required to build programs using libaviplay
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce libaviplay
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description devel
Header files required to build programs using libaviplay.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
libaviplay.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

%build
libtoolize --copy --force
aclocal
automake -a -c --foreign
autoconf
CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -D_LARGEFILE64_SOURCE"; export CFLAGS
CXXFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -D_LARGEFILE64_SOURCE"; export CXXFLAGS
%configure \
	--with-qt-includes=%{_includedir}/qt \
	--enable-release

touch lib/dummy.cpp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},/usr/lib/win32}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install samples/misc/{asfdump,.libs/{asftest,benchmark}} $RPM_BUILD_ROOT%{_bindir}

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
%attr(755,root,root) %{_bindir}/aviplay
%attr(755,root,root) %{_bindir}/asf*
%attr(755,root,root) %{_bindir}/[bkq]*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/avifile/lib*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc doc/README-DEVEL*
%attr(755,root,root) %{_bindir}/avifile-config
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/%{name}
