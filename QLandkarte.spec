Summary:	Garmin's MapSource clone for Linux
Summary(pl.UTF-8):	Klon MapSource pod Linuksa
Name:		QLandkarte
Version:	0.7.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qlandkarte/%{name}_%{version}.tar.gz
# Source0-md5:	51f804235511f1c10ae8538f86743135
URL:		http://qlandkarte.sourceforge.net
BuildRequires:	QtCore-devel > 4.2.0
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	libusb-devel
BuildRequires:	proj-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Garmin's MapSource clone for Linux.

%description -l pl.UTF-8
Klon MapSource pod Linuksa.

%prep
%setup -q -n %{name}_%{version}
%{__sed} -i 's:QMAKE_CXXFLAGS_RELEASE += -O3:QMAKE_CXXFLAGS_RELEASE +=:' common.in

%build
%configure \
	--enable-release
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_mandir}{,/man1}/*.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL changelog.txt index.html
%attr(755,root,root) %{_bindir}/qlandkarte
%dir %{_libdir}/qlandkarte
%attr(755,root,root) %{_libdir}/qlandkarte/*.so
%{_desktopdir}/qlandkarte.desktop
%{_mandir}/man1/*.1.gz
