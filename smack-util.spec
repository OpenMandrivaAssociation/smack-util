%define ver 0.1
%define libsuffix static-devel

Summary: Smack user-space tools
Name: smack-util
Version: %ver
Release: %mkrel 1
License: GPL
Group: System/Base
Source0: smack-util-%{ver}.tar.gz
Source1: smack.init
URL: http://www.schaufler-ca.com
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This packages contains the user-space programs needed to
configure Smack properly.

%package %{libsuffix}
Summary: Static library for %{name}
Group: System/Libraries

%description %{libsuffix}
Static library for %{name}.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/smack
mkdir -p %{buildroot}/{%_sbindir,%_libdir,%_sysconfdir/init.d}
install smackload smackcipso %{buildroot}%{_sbindir}
install libsmack.a %{buildroot}%{_libdir}
install %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/smack

%post
%_post_service smack

%preun
%_preun_service smack

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /smack
%{_sbindir}/smackcipso
%{_sbindir}/smackload
%{_sysconfdir}/init.d/smack

%files %{libsuffix}
%defattr(-,root,root)
%{_libdir}/libsmack.a
