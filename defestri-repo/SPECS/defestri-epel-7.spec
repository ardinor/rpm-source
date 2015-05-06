Name:		repo.defestri.org-release
Version:	7.0
Release:	1%{?dist}
Summary:	Installs the repo.defestri.org repo

Group:		
License:	GPLv2
URL:		http://repo.defestri.org/pub/epel
#Source0:	GPG key
Source1:	GPL
Source2:	defestri-epel.repo

BuildRequires:	
BuildArch:	noarch
Requires:	epel-release >= ${version}

%description
Installs the repo file and GPG key necessary to use the repo.defestri.org repository.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
$defattr(-,root,root,-)
%doc
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*



%changelog

