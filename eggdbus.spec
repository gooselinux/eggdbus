Summary: Experimental D-Bus bindings for GObject
Name: eggdbus
Version: 0.6
Release: 3%{?dist}
License: LGPLv2
Group: Development/Libraries
URL: http://cgit.freedesktop.org/~david/eggdbus
Source0: http://cgit.freedesktop.org/~david/%{name}/snapshot/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: gtk-doc

%description
Experimental D-Bus bindings for GObject.

%package devel
Summary: Development files for EggDBus
Group: Development/Libraries
Requires: %name = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel
Requires: gtk-doc

%description devel
Development files for EggDBus.

%prep
%setup -q

%build
%configure --enable-gtk-doc --disable-static
make %{?_smp_mflags}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/tests

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/eggdbus
%{_datadir}/man/man1/*
%{_bindir}/*

%changelog
* Sat Jun 19 2010 Christopher Aillon <caillon@redhat.com> - 0.6-3
- Minor packaging fixups

* Fri Nov 13 2009 David Zeuthen <davidz@redhat.com> - 0.6-2
- Rebuild

* Fri Nov 13 2009 David Zeuthen <davidz@redhat.com> - 0.6-1
- Update to 0.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 David Zeuthen <davidz@redhat.com> - 0.5-1
- Update to 0.5

* Wed May 27 2009 David Zeuthen <davidz@redhat.com> - 0.4-1
- Update to 0.4

* Mon Feb  9 2009 David Zeuthen <davidz@redhat.com> - 0.3-1
- Initial spec file.
