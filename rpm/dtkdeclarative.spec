Name:           dtkdeclarative
Version:        6.0.0
Release:        1%{?dist}
Summary:        DTK Declarative Module (QML bindings)
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkdeclarative
Source0:        dtkdeclarative-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.10
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(dtk6core)
BuildRequires:  pkgconfig(dtk6gui)
BuildRequires:  pkgconfig(dtk6widget)

%description
DTK Declarative module provides QML bindings for DTK widgets,
enabling use of DTK components in QML-based applications.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DDTK5=OFF
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE*
%{_libdir}/qt6/qml/org/deepin/dtk/*
%{_libdir}/libdtkdeclarative*.so*

%package devel
Summary: Development files for DTK Declarative
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and development libraries for DTK Declarative.

%files devel
%{_includedir}/dtkdeclarative*/
%{_libdir}/libdtkdeclarative*.so
%{_libdir}/cmake/DtkDeclarative/

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
