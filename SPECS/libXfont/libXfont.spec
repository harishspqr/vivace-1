Summary:	X11 Xfont runtime library.
Name:		libXfont
Version:	1.5.1
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	pkg-config util-macros proto xtrans libfontenc-devel freetype2-devel harfbuzz-devel glib-devel
Requires:	libfontenc freetype2 harfbuzz glib
%description
The X11 Xfont runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} --disable-devel-docs
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
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.5.1-1
-	initial version