Name:           hyprshutdown
Version:        0.1.0
Release:        %autorelease
Summary:        Graceful session logout for hyprland
# LICENSE: BSD-3-Clause
# protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant
License:        BSD-3-Clause AND HPND-sell-variant
URL:            https://github.com/hyprwm/hyprshutdown
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires: glaze-static
BuildRequires: pkgconfig(hyprtoolkit)
BuildRequires: pkgconfig(hyprutils) >= 0.11.0
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
# BuildRequires:  pkgconfig(cairo)
# BuildRequires:  pkgconfig(glesv2)
# BuildRequires:  pkgconfig(hyprgraphics)
# BuildRequires:  pkgconfig(hyprlang)
# BuildRequires:  pkgconfig(hyprutils)
# BuildRequires:  pkgconfig(hyprwayland-scanner)
# BuildRequires:  pkgconfig(pango)
# BuildRequires:  pkgconfig(pangocairo)

%description
Hypershutdown closes out a hyprland session cleanly.



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
%{_bindir}/%{name}

%changelog
%autochangelog
