%global commit0 11cbc6c577b84ffb1edf4df3fc5b6128c3ae6947
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 5

%global __provides_exclude_from ^(%{_libdir}/hyprland/.*\\.so)$

%global plugins %{shrink:
    borders-plus-plus
                csgo-vulkan-fix
                hyprbars
                hyprfocus
}

%if !%{defined build_for}
%global build_for release
%endif

%define pluginsmeta %{lua:
if rpm.expand("%build_for") == "git" then
    rpm.define("pluginssuffix -git")
    rpm.define(rpm.expand("pluginsmetaname hyprland-plugins%pluginssuffix"))
    rpm.define(rpm.expand("hyprlandpkg hyprland%pluginssuffix"))
else
    rpm.define("pluginsmetaname hyprland-plugins")
    rpm.define("hyprlandpkg hyprland")
end
}

%pluginsmeta

Name:           %{pluginsmetaname}
Version:        0.57.0
Release:        %autorelease
Summary:        Official plugins for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-plugins
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  %{hyprlandpkg}-devel

Requires:       %{hyprlandpkg} = %_hyprland_version

# print Recommends: for each plugin
%{lua:for w in rpm.expand('%plugins'):gmatch("%S+") do print("Recommends: hyprland-plugin-"..w..(rpm.expand("%build_for") == "git" and "-git" or "")..'\n') end}

%description
%{summary}.

%define _package() \%package -n hyprland-plugin-%1%{?pluginssuffix:%{pluginssuffix}}\
Summary:       %1 plugin for %{hyprlandpkg}\
Requires:      %{hyprlandpkg} = %_hyprland_version\
\%description  -n hyprland-plugin-%1%{?pluginssuffix:%{pluginssuffix}}\
\%1 plugin for %{hyprlandpkg}.\
\%files -n     hyprland-plugin-%1%{?pluginssuffix:%{pluginssuffix}}\
\%%license LICENSE\
\%dir %{_libdir}/hyprland\
\%{_libdir}/hyprland/lib%1.so\

# expand %%_package for each plugin
%{lua:for w in rpm.expand('%plugins'):gmatch("%S+") do print(rpm.expand("%_package "..w)..'\n\n') end}


%prep
%autosetup -n hyprland-plugins-%{version} -p1

%global _vpath_builddir ../redhat-linux-build-$plugin

%build
for plugin in %{plugins}
do
pushd $plugin
%meson --libdir=%{_libdir}/hyprland
%meson_build
popd
done


%install
for plugin in %{plugins}
do
pushd $plugin
%meson_install
popd
done


%files


%changelog
%autochangelog
