Summary:	Library and sample program for playing AVI files
Summary(pl):	Biblioteka i przyk³adowy program do odtwarzania plików AVI
Name:		avifile
Version:	0.50
Release:	5
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://divx.euro.ru/%{name}-%{version}.tar.gz
Patch0:		http://www.emulinks.de/divx/%{name}-%{version}.bitrate.patch
Patch1:		%{name}-CVS-20001206.patch.gz
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-cout.patch
Requires:	avi-codecs
BuildRequires:	unzip
BuildRequires:	libstdc++-devel
BuildRequires:	xmps-devel
BuildRequires:	qt-devel
BuildRequires:	SDL-devel
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
%patch3 -p1
perl -pi -e "s|-march=i586||g" configure.in

%build
aclocal
libtoolize --copy --force
automake -a -c
autoconf
CD_OPT="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"; export CD_OPT
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

gzip -9nf README doc/{CREDITS,EXCEPTIONS,TODO,VIDEO-PERFORMANCE,WARNINGS}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%name
