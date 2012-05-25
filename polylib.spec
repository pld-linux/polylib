#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Polyhedral Library
Summary(pl.UTF-8):	Biblioteka operacji na wielościanach
Name:		polylib
Version:	5.22.5
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://icps.u-strasbg.fr/PolyLib/polylib_src/%{name}-%{version}.tar.gz
# Source0-md5:	c0088786e0a5ae64b7cc47ad19ae4f83
URL:		http://icps.u-strasbg.fr/PolyLib/
BuildRequires:	gmp-devel >= 2.0.2
Requires:	gmp >= 2.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Polyhedral Library (PolyLib for short) operates on objects made up
of unions of polyhedra of any dimension. It was first developed by
Doran Wilde at IRISA, in Rennes, France, in connection with the ALPHA
project.

%description -l pl.UTF-8
PolyLib (Polyhedral Library) to biblioteka operująca na obiektach
powstałych z sum wielościanów o dowolnej liczbie wymiarów. Początkowo
została stworzona przez Dorana Wilde'a w IRISA, w Rennes, we Francji,
we współpracy z projektem ALPHA.

%package devel
Summary:	Header files for PolyLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PolyLib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 2.0.2

%description devel
Header files for PolyLib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PolyLib.

%package static
Summary:	Static PolyLib library
Summary(pl.UTF-8):	Statyczna biblioteka PolyLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PolyLib library.

%description static -l pl.UTF-8
Statyczna biblioteka PolyLib.

%package apidocs
Summary:	PolyLib API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki PolyLib
Group:		Documentation

%description apidocs
API and internal documentation for PolyLib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki PolyLib.

%prep
%setup -q

%build
%configure \
	--enable-int-lib \
	--enable-longlongint-lib \
	--with-libgmp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/Changes 
%attr(755,root,root) %{_bindir}/c2p
%attr(755,root,root) %{_bindir}/disjoint_union_adj
%attr(755,root,root) %{_bindir}/disjoint_union_sep
%attr(755,root,root) %{_bindir}/ehrhart_lower_bound
%attr(755,root,root) %{_bindir}/ehrhart_quick_apx
%attr(755,root,root) %{_bindir}/ehrhart_ranking*
%attr(755,root,root) %{_bindir}/ehrhart_union*
%attr(755,root,root) %{_bindir}/ehrhart_upper_bound
%attr(755,root,root) %{_bindir}/findv
%attr(755,root,root) %{_bindir}/pp*
%attr(755,root,root) %{_bindir}/r2p
%attr(755,root,root) %{_bindir}/testehrhart*
%attr(755,root,root) %{_libdir}/libpolylib32.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolylib32.so.8
%attr(755,root,root) %{_libdir}/libpolylib64.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolylib64.so.8
%if 0
# not built
%attr(755,root,root) %{_libdir}/libpolylib128.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolylib128.so.8
%endif
%attr(755,root,root) %{_libdir}/libpolylibgmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolylibgmp.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolylib32.so
%{_libdir}/libpolylib32.la
%attr(755,root,root) %{_libdir}/libpolylib64.so
%{_libdir}/libpolylib64.la
%attr(755,root,root) %{_libdir}/libpolylibgmp.so
%{_libdir}/libpolylibgmp.la
%{_includedir}/polylib
%if 0
# not generated
%{_pkgconfigdir}/polylib32.pc
%{_pkgconfigdir}/polylib64.pc
%endif
%{_pkgconfigdir}/polylibgmp.pc
%if 0
# not built
%attr(755,root,root) %{_libdir}/libpolylib128.so
%{_libdir}/libpolylib128.la
%{_pkgconfigdir}/polylib128.pc
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/libpolylib32.a
%{_libdir}/libpolylib64.a
%if 0
# not built
%{_libdir}/libpolylib128.a
%endif
%{_libdir}/libpolylibgmp.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/{PI-1330.ps.gz,PI-785.ps.gz,parampoly-doc.ps.gz,doc.pdf}
%endif
