Summary: nethserver-rh-python35 is made to ease the installation of rh-python35
%define name nethserver-rh-python35
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: development
Source: %{name}-%{version}.tar.gz
Requires: rh-python35
BuildRequires: nethserver-devtools
BuildArch: noarch

%description

nethserver-rh-python35 is made to ease the installation of rh-python35

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} \
    --file /usr/bin/python35 'attr(0750,root,root)' \
$RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Mon Sep 03 2018 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial