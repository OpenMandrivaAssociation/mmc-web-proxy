%define _requires_exceptions pear(graph\\|pear(includes\\|pear(modules
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	SquidGuard module for the LMC web interface
Name:		lmc-web-proxy
Version:	2.0.0
Release:	%mkrel 2
License:	GPL
Group:		System/Servers
URL:		http://lds.linbox.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		lmc-web-proxy-Makefile_fix.diff
Requires:	squid squidGuard
Requires:	lmc-web-base
BuildArch:      noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
Linbox Management Console web interface designed by Linbox.

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
%{_datadir}/lmc/modules/proxy
