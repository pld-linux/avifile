Summary:	Library and sample program for playing AVI files
Summary(pl):	Biblioteka i przykładowy program do odtwarzania plików AVI
Name:		avifile
Version:	0.43
Release:	1
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://divx.euro.ru/%{name}-%{version}.tar.gz
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-old_ver_conflict.patch
# Note:		using non-standard optimizations generated non-working binary.
#Patch3:	%{name}-OPT_FLAGS.patch
Requires:	avi-codecs
BuildRequires:	unzip
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Library and sample program for playing AVI files. It uses windows
codecs and parts of Wine (http://www.winehq.com) code to load them.

%description -l pl
Biblioteka i przykładowy program do odtwarzania plików AVI.
Wykorzystuje dekompresory dla Windows oraz fragmenty kody Wine
(http://www.winehq.com) aby je załadować.

%package devel
Summary:	Header file required to build programs using libaviplay
Summary(pl):	Pliki nagłówkowe wymagane przez programy używające libaviplay
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description devel
Header files required to build programs using libaviplay.

%description devel -l pl
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
libaviplay.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
find . -exec touch {} \;

%build
#autoheader;autoconf;automake; 

LDFLAGS="-s" ; export LDFLAGS
#CXXFLAGS="$RPM_OPT_FLAGS"; export CXXFLAGS
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT"{%{_bindir},%{_libdir}}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf README doc/{CREDITS,EXCEPTIONS,TODO,VIDEO-PERFORMANCE,WARNINGS}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/%{name}
%doc *gz doc/*gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/%name
