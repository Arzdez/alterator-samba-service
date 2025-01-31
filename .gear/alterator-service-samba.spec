%define _unpackaged_files_terminate_build 1
%define service service-samba-dc
Name: alterator-service-samba
Version: 0.1
Release: alt1

Summary: Service for managment samba dc
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-service-samba

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: python3-devel

Requires: alterator-module-executor
Requires: alterator-interface-service
Requires: alterator-entry
Requires: python3

%description
Service for managment samba ad.

%prep
%setup

%install
mkdir -p %buildroot%_alterator_datadir/service
mkdir -p %buildroot%_datadir/%name/samba-dc

install -p -D -m755 %service %buildroot%_bindir/%service
install -p -D -m755 service-samba-dc-exec %buildroot%_bindir/service-samba-dc-exec
install -p -D -m644 %service.backend %buildroot%_alterator_datadir/backends/%service.backend
install -p -D -m644 %service.service %buildroot%_alterator_datadir/service/%service.service
install -p -D -m644 parameters/provision-parameters.schema.json %buildroot%_datadir/%name/samba-dc/provision-parameters.schema.json

%files
%_bindir/%service
%_bindir/%service-exec
%_alterator_datadir/backends/%service.backend
%_alterator_datadir/service/%service.service
%_datadir/alterator-service-samba/samba-dc/provision-parameters.schema.json

%changelog
* Tue Jan 28 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial commit
