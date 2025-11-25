Name:           hyprland-guiutils
Version:        0.1.0
Release:        %autorelease -b4
Summary:        Hyprland utility apps
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-guiutils
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++

#BuildRequires:  cmake(Qt6Quick)
#BuildRequires:  cmake(Qt6QuickControls2)
#BuildRequires:  cmake(Qt6WaylandClient)
#BuildRequires:  cmake(Qt6Widgets)
#BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  pkgconfig(hyprutils) >= 0.6.0
BuildRequires:  pkgconfig(hyprlang) >= 0.2.4
BuildRequires:  pkgconfig(hyprtoolkit) >= 0.2.2
BuildRequires:  libdrm-devel
BuildRequires:  pixman-devel
#BuildRequires:  wayland-devel

#Requires:       hyprland-qt-support%{?_isa}

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprland-dialog
%{_bindir}/hyprland-donate-screen
%{_bindir}/hyprland-update-screen

%changelog
%autochangelog
