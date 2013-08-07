# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       qmlcalendar

# >> macros
# << macros

Summary:    Calendar application made with QML
Version:    0.3
Release:    1
Group:      Applications/System
License:    BSD
URL:        https://github.com/nemomobile/qmlcalendar/
Source0:    %{name}-%{version}.tar.bz2
Source100:  qmlcalendar.yaml
Requires:   qt5-qtdeclarative-pim-organizer
Requires:   mkcal-qt5
Requires:   qt-components-qt5
Requires:   mapplauncherd-booster-qtcomponents-qt5
Requires:   systemd
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Organizer)
BuildRequires:  pkgconfig(qdeclarative5-boostable)
BuildRequires:  desktop-file-utils

%description
Calendar application written using QML.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%preun
if [ "$1" -eq 0 ]; then
systemctl stop calenderr.service
fi
# >> preun
systemctl stop calenderr.service
systemctl disable calenderr.service
# << preun

%post
systemctl daemon-reload
systemctl reload-or-try-restart calenderr.service
# >> post
systemctl --system daemon-reload
systemctl start calenderr.service
systemctl enable calenderr.service
# << post

%postun
systemctl daemon-reload
# >> postun
systemctl --system daemon-reload
# << postun

%files
%defattr(-,root,root,-)
/lib/systemd/system/calenderr.service
/opt/%{name}
%{_datadir}/icons/hicolor/80x80/apps/*.png
%{_datadir}/applications/*.desktop
# >> files
# << files
