Summary:	Qt4 binding for FreePascal
Name:		fpc-qt4
Version:	2.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://users.telenet.be/Jan.Van.hijfte/qtforfpc/qt4pas-V2.0RC_Qt4.5.3.tar.gz
# Source0-md5:	32c98f9a164679c14d58f2f5a727a6c2
URL:		http://users.telenet.be/Jan.Van.hijfte/qtforfpc/fpcqt4.html
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= 4.4.0
BuildRequires:	qt4-qmake >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a Qt4 binding for FreePascal that may be of use to provide
the Lazarus LCL library with a Qt interface

This binding does not aim to cover the whole Qt4 framework, but only
just enough to satisfy the LCL needs. If any LCL/Qt developer needs an
extra class, just ask and it will be added promptly. Some of the
methods that have parameters based upon templates have been omitted.

%prep
%setup -q -n qt4pas-V%{version}RC_Qt4.5.3

%build
%{_bindir}/qmake-qt4

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.TXT
%attr(755,root,root) %{_libdir}/libQt4Pas.so*
