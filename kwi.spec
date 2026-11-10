%define commit 8937f4131dc6a218b45f3aa236ce7457905a0a2b

Name:		kwi
Version:	0.1.0
Release:	0.20261109.1
Summary:	A modern terminal emulator for KDE
Url:		https://invent.kde.org/utilities/kwi
# Application: GPL-2.0-only OR GPL-3.0-only.
# Libraries: LGPL-2.1-only OR LGPL-3.0-only.
License:	(GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
Group:		Graphical desktop/KDE
Source0:	https://invent.kde.org/utilities/kwi/-/archive/%{commit}/kwi-%{commit}.tar.gz
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DBUILD_KPART:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core) >= 6.11
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6Pty)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WidgetsAddons)
# KF5 provides the same unversioned qml(org.kde.kitemmodels) name.
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6KirigamiAddons) >= 1.11
BuildRequires:	cmake(KF6KirigamiAppComponents) >= 1.1
BuildRequires:	pkgconfig(libghostty-vt) >= 1.0
# KDECMakeSettings turns BUILD_TESTING on. The tests are not installed.
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6QuickTest)
BuildRequires:	python
BuildRequires:	%{_bindir}/dbus-run-session
BuildRequires:	qml(QtQuick.Dialogs)
BuildRequires:	qml(org.kde.kirigami.forms)
BuildRequires:	qml(org.kde.kirigami.dialogs)
BuildRequires:	qml(org.kde.kirigami.delegates)
BuildRequires:	qml(org.kde.kirigami.actioncollection)
BuildRequires:	qml(org.kde.kirigamiaddons.settings)
BuildRequires:	qml(org.kde.desktop)
BuildRequires:	qml(org.kde.notification)
# QML imports are loaded at runtime, not through DT_NEEDED.
# Qt5 and KF5 provide the same unversioned qml() names as Qt6 and KF6.
Requires:	kirigami-addons >= 1.11
Requires:	%{mklibname KF6ItemModels} >= 6.29
Requires:	qml(org.kde.desktop)
Requires:	%{mklibname Qt6QuickControls2} >= 6.11
Requires:	%{mklibname Qt6QuickDialogs2} >= 6.11

%description
Kwi is a terminal emulator for KDE Plasma and other desktops. It is
built on the Ghostty terminal library and KDE Frameworks, and it can
be embedded through a QML module or a KPart.

%install -a
# No public headers are installed, so the linker symlink is unused.
rm -f %{buildroot}%{_libdir}/libkwi-terminal.so

%files
%{_bindir}/kwi
# The terminal library is only used by Kwi and its KPart.
%{_libdir}/libkwi-terminal.so.0.1.0
%{_qtdir}/qml/org/kde/kwi
%{_qtdir}/plugins/kf6/parts/kwipart.so
%{_datadir}/applications/org.kde.kwi.desktop
%{_datadir}/metainfo/org.kde.kwi.metainfo.xml
%{_datadir}/knotifications6/kwi.notifyrc
%{_datadir}/config.kcfg/TerminalPreferences.kcfg
%{_datadir}/kwi
%{_datadir}/licenses/kwi
%{_datadir}/icons/hicolor/*/apps/org.kde.kwi.*
