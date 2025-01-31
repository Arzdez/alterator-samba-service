%define _unpackaged_files_terminate_build 1
%define service samba-ad-service
Name: %service 
Version: 0.1
Release: alt1

Summary: Service for managment samba ad
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/samba-service-managment

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: python3-devel

Requires: alterator-module-executor >= 0.1.14
Requires: alterator-interface-service
Requires: alterator-entry
Requires: python3

%package -n alterator-interface-service
Summary: Interface for managment some services
Group: System/Configuration/Other
Version: 0.1
Release: alt1

%description
Service for managment samba ad.

%description -n alterator-interface-service
Alterator interface for managment some services.

%prep
%setup

%install
mkdir -p %buildroot%_alterator_datadir/service/%name
mkdir -p %buildroot%_alteratordir/backends
mkdir -p %buildroot%_datadir/alterator-samba-service

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m755 samba-ad-service-exec %buildroot%_bindir/samba-ad-service-exec
install -p -D -m644 alterator/%name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 alterator/%service.service %buildroot%_alterator_datadir/service/%service.service
install -p -D -m644 interface/org.altlinux.alterator.service1.xml %buildroot%_datadir/dbus-1/interfaces/org.altlinux.alterator.service1.xml
install -p -D -m644 alterator/service.schema.json %buildroot%_alterator_datadir/schemas/service.schema.json
install -p -D -m644 interface/org.altlinux.alterator.service1.policy %buildroot%_datadir/polkit-1/actions/org.altlinux.alterator.service1.policy
install -p -D -m644 schema/join-parameters-validation.schema.json %buildroot%_datadir/alterator-samba-service/join-parameters-validation.schema.json
install -p -D -m644 schema/deploy-parameters-validation.schema.json %buildroot%_datadir/alterator-samba-service/deploy-parameters-validation.schema.json

%files
%_bindir/%name
%_bindir/samba-ad-service-exec
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/service/%service.service
%_alterator_datadir/schemas/service.schema.json
%_datadir/alterator-samba-service/join-parameters-validation.schema.json
%_datadir/alterator-samba-service/deploy-parameters-validation.schema.json

%files -n alterator-interface-service
%_datadir/dbus-1/interfaces/org.altlinux.alterator.service1.xml
%_datadir/polkit-1/actions/org.altlinux.alterator.service1.policy

%changelog
* Tue Jan 28 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial commit
