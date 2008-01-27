
%define	fver 2007.12.22
Summary:	Garmin's MapSource clone for Linux
Summary(pl.UTF-8):	Klon MapSource pod Linuksa
Name:		QLandkarte
Version:	0.6.0.%{fver}
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qlandkarte/%{name}.%{fver}.tar.gz
# Source0-md5:	614cd25963e834fefcaea7137e2aa8d8
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
%setup -q -n %{name}

%build
qmake-qt4 \
	"QMAKE_CXXFLAGS_RELEASE=%{rpmcxxflags}" \
	-after CONFIG+=%{!?debug:release}%{?debug:debug} QLandkarte.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL changelog.txt index.html
%attr(755,root,root) %{_bindir}/QLandkarte
%dir %{_libdir}/qlandkarte
%attr(755,root,root) %{_libdir}/qlandkarte/*.so
