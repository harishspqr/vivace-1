Summary:	Abstract network code for X.
Name:		xtrans
Version:	1.3.5
Release:	1
License:	TODO
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/xtrans-1.3.5.tar.bz2
BuildRequires:	pkg-config util-macros fontconfig-devel libxcb-devel
Requires:	fontconfig libxcb
%description
Abstract network code for X.
%prep
%setup -q 
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
/*
%changelog
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.5-1
-	initial version