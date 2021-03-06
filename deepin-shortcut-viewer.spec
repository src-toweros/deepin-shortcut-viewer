Name:           deepin-shortcut-viewer
Version:        5.0.1
Release:        4
Summary:        Deepin Shortcut Viewer
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-shortcut-viewer
Source0:        https://proposed-packages.deepin.com/dde-apricot/pool/main/d/%{name}/%{name}_%{version}.orig.tar.xz

BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
Provides:       bundled(CuteLogger)

%description
The program displays a shortcut key window when a JSON data is passed.

%prep
%setup -q

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Thu Sep 3 2020 weidong <weidong@uniontech.com> - 5.0.1-4
- fix source url in spec

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.0.1-3
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.1-2
- Package init
