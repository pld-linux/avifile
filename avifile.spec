Summary:	Library and sample program for playing AVI files
Summary(pl):	Biblioteka i przyk³adowy program do odtwarzania plików AVI
Name:		avifile
Version:	0.50
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://divx.euro.ru/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-old_ver_conflict.patch
Patch2:		http://www.emulinks.de/divx/%{name}-%{version}.bitrate.patch
Patch3:		%{name}-OPT_FLAGS.patch
Patch4:		%{name}-kernel2.4-test11.patch
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
Wykorzystuje dekompresory dla Windows oraz fragmenty kody Wine
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
%patch4 -p1
find . -exec touch {} \;

%build
autoconf
CD_OPT="$RPM_OPT_FLAGS" ; export CD_OPT
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT"{%{_bindir},%{_libdir},/usr/lib/win32}

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
