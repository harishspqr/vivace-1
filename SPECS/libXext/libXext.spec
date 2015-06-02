Summary:	library for common extensions to the X11 protocol.
Name:		libXext
Version:	1.3.3
Release:	1
License:	TODO
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/libXext-1.3.3.tar.bz2
BuildRequires:	pkg-config util-macros fontconfig-devel libxcb-devel xtrans libX11-devel libXau-devel
Requires:	fontconfig libxcb libX11 libXau
Provides:	pkgconfig(xext)
%description
Core X11 protocol client library.
%package	devel
Summary:	Header and development files for libXext
Requires:	%{name} = %{version}
%description	devel
libXext - library for common extensions to the X11 protocol.
%prep
%setup -q 
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.3-1
-	initial version