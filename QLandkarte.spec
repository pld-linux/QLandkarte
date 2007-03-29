
%define	fver 2007.03.16
Summary:	Garmin's MapSource clone for Linux
Summary(pl.UTF-8):	Klon MapSource pod Linuksa
Name:		QLandkarte
Version:	0.2.2.%{fver}
Release:	0.4
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/qlandkarte/%{name}.%{fver}.tar.gz
# Source0-md5:	072a0481078640b8d55961c7f9148153
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-Vista.patch
URL:		http://qlandkarte.sourceforge.net
BuildRequires:	QtCore-devel > 4.2.0
BuildRequires:	QtGui-devel
BuildRequires:	libusb-devel
BuildRequires:	proj-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Garmin's MapSource clone for Linux.

%description -l pl.UTF-8
Klon MapSource pod Linuksa.

%prep
%setup -q -n %{name}.%{fver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
qt4-qmake "QMAKE_CXXFLAGS_RELEASE=%{rpmcxxflags}" \
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
