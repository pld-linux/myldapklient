Summary:	Support for LDAP address book for KMail
Summary(pl):	Wsparcie dla u¿ywania ksi±¿ki adresowej LDAP w KMailu
Name:		myldapklient
Version:	0.6.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	kdebase-devel
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_mandir		%{_prefix}/man

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
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{name}/%{name}.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/*
%{_pixmapsdir}/*/*/*/*.png
