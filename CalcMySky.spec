#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
Name     : CalcMySky
Version  : 0.3.3
Release  : 11
URL      : https://github.com/10110111/CalcMySky/archive/v0.3.3/CalcMySky-0.3.3.tar.gz
Source0  : https://github.com/10110111/CalcMySky/archive/v0.3.3/CalcMySky-0.3.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: CalcMySky-bin = %{version}-%{release}
Requires: CalcMySky-data = %{version}-%{release}
Requires: CalcMySky-lib = %{version}-%{release}
Requires: CalcMySky-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : eigen-dev
BuildRequires : git
BuildRequires : glm-dev
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build status](https://ci.appveyor.com/api/projects/status/vtrtpjxk08xp6ba6/branch/master?svg=true)](https://ci.appveyor.com/project/10110111/CalcMySky)

%package bin
Summary: bin components for the CalcMySky package.
Group: Binaries
Requires: CalcMySky-data = %{version}-%{release}
Requires: CalcMySky-license = %{version}-%{release}

%description bin
bin components for the CalcMySky package.


%package data
Summary: data components for the CalcMySky package.
Group: Data

%description data
data components for the CalcMySky package.


%package dev
Summary: dev components for the CalcMySky package.
Group: Development
Requires: CalcMySky-lib = %{version}-%{release}
Requires: CalcMySky-bin = %{version}-%{release}
Requires: CalcMySky-data = %{version}-%{release}
Provides: CalcMySky-devel = %{version}-%{release}
Requires: CalcMySky = %{version}-%{release}

%description dev
dev components for the CalcMySky package.


%package lib
Summary: lib components for the CalcMySky package.
Group: Libraries
Requires: CalcMySky-data = %{version}-%{release}
Requires: CalcMySky-license = %{version}-%{release}

%description lib
lib components for the CalcMySky package.


%package license
Summary: license components for the CalcMySky package.
Group: Default

%description license
license components for the CalcMySky package.


%prep
%setup -q -n CalcMySky-0.3.3
cd %{_builddir}/CalcMySky-0.3.3
pushd ..
cp -a CalcMySky-0.3.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735661170
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../../buildavx2/clr-build-avx2;
make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735661170
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/CalcMySky
cp %{_builddir}/CalcMySky-%{version}/COPYING %{buildroot}/usr/share/package-licenses/CalcMySky/31a3d460bb3c7d98845187c716a30db81c44b615 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/calcmysky
/V3/usr/bin/showmysky
/usr/bin/calcmysky
/usr/bin/showmysky

%files data
%defattr(-,root,root,-)
/usr/share/CalcMySky/shaders/accumulate-single-scattering-texture.frag
/usr/share/CalcMySky/shaders/calc-view-dir.h.glsl
/usr/share/CalcMySky/shaders/common-functions.frag
/usr/share/CalcMySky/shaders/common-functions.h.glsl
/usr/share/CalcMySky/shaders/compute-direct-irradiance.frag
/usr/share/CalcMySky/shaders/compute-eclipsed-double-scattering.frag
/usr/share/CalcMySky/shaders/compute-eclipsed-single-scattering.frag
/usr/share/CalcMySky/shaders/compute-indirect-irradiance.frag
/usr/share/CalcMySky/shaders/compute-light-pollution-multiple-scattering.frag
/usr/share/CalcMySky/shaders/compute-light-pollution-single-scattering.frag
/usr/share/CalcMySky/shaders/compute-multiple-scattering.frag
/usr/share/CalcMySky/shaders/compute-scattering-density.frag
/usr/share/CalcMySky/shaders/compute-single-scattering.frag
/usr/share/CalcMySky/shaders/compute-transmittance-functions.h.glsl
/usr/share/CalcMySky/shaders/compute-transmittance.frag
/usr/share/CalcMySky/shaders/copy-scattering-texture-2d.frag
/usr/share/CalcMySky/shaders/copy-scattering-texture-3d.frag
/usr/share/CalcMySky/shaders/direct-irradiance.frag
/usr/share/CalcMySky/shaders/direct-irradiance.h.glsl
/usr/share/CalcMySky/shaders/eclipsed-direct-irradiance.frag
/usr/share/CalcMySky/shaders/eclipsed-direct-irradiance.h.glsl
/usr/share/CalcMySky/shaders/multiple-scattering-light-pollution.frag
/usr/share/CalcMySky/shaders/multiple-scattering-light-pollution.h.glsl
/usr/share/CalcMySky/shaders/multiple-scattering.frag
/usr/share/CalcMySky/shaders/multiple-scattering.h.glsl
/usr/share/CalcMySky/shaders/render.frag
/usr/share/CalcMySky/shaders/shader.geom
/usr/share/CalcMySky/shaders/shader.vert
/usr/share/CalcMySky/shaders/single-scattering-eclipsed.frag
/usr/share/CalcMySky/shaders/single-scattering-eclipsed.h.glsl
/usr/share/CalcMySky/shaders/single-scattering-light-pollution.frag
/usr/share/CalcMySky/shaders/single-scattering-light-pollution.h.glsl
/usr/share/CalcMySky/shaders/single-scattering.frag
/usr/share/CalcMySky/shaders/single-scattering.h.glsl
/usr/share/CalcMySky/shaders/texture-coordinates.frag
/usr/share/CalcMySky/shaders/texture-coordinates.h.glsl
/usr/share/CalcMySky/shaders/texture-sampling-functions.frag
/usr/share/CalcMySky/shaders/texture-sampling-functions.h.glsl
/usr/share/CalcMySky/shaders/version.h.glsl

%files dev
%defattr(-,root,root,-)
/usr/include/ShowMySky/AtmosphereRenderer.hpp
/usr/include/ShowMySky/Exception.hpp
/usr/include/ShowMySky/Settings.hpp
/usr/lib64/cmake/ShowMySky-Qt6/ShowMySky-Qt6Config-relwithdebinfo.cmake
/usr/lib64/cmake/ShowMySky-Qt6/ShowMySky-Qt6Config.cmake
/usr/lib64/libShowMySky-Qt6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libShowMySky-Qt6.so.15.0.0
/usr/lib64/libShowMySky-Qt6.so.15
/usr/lib64/libShowMySky-Qt6.so.15.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/CalcMySky/31a3d460bb3c7d98845187c716a30db81c44b615
