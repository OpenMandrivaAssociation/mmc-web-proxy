%define _requires_exceptions pear(graph\\|pear(includes\\|pear(modules
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	SquidGuard module for the MMC web interface
Name:		mmc-web-proxy
Version:	2.3.2
Release:	%mkrel 3
License:	GPL
Group:		System/Servers
URL:		https://mds.mandriva.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		mmc-web-proxy-Makefile_fix.diff
Requires:	squid squidGuard
Requires:	mmc-web-base >= 2.3.2
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mandriva Management Console web interface designed by Linbox.

This is the Squid/SquidGuard module.

%prep

%setup -q -n %{name}-%{version}
for i in `find . -type d -name .svn`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch0 -p0

%build

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING Changelog
%{_datadir}/mmc/modules/proxy
