Summary:	Support for LDAP address book for KMail
Summary(pl):	Wsparcie dla u¿ywania ksi±¿ki adresowej LDAP w KMailu
Name:		myldapklient
Version:	0.6.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	47ef81e43e5f8746c17c5d96c11e08aa
BuildRequires:	kdebase-devel
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Support for LDAP address book for KMail.

%description -l pl
Wsparcie dla u¿ywania ksi±¿ki adresowej LDAP w KMailu.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/Network/Mail

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{name}/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/Network/Mail

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/Network/*
%{_pixmapsdir}/*/*/*/*.png
