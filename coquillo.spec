%define _disable_ld_no_undefined	1
Name:           coquillo
Version:        1.12
Release:        1
License:        GPLv2
Summary:        Audio Metadata Editor
Url:            http://univerge.no-ip.org/?q=coquillo
Group:          Sound
Source0:        http://cs.joensuu.fi/~sjuvonen/coquillo/%{version}/%{name}-%{version}-src.tar.gz
Patch0:		coquillo-1.9-mdv-plugins.patch
Patch1:		coquillo-1.9-mdv-libsuff.patch
BuildRequires:  taglib-devel >= 1.6
BuildRequires:  qt4-devel

%description
Coquillo is a metadata editor, or so-called tagger utility, with which you can
edit tags of many different audio files. Its support includes MP3, Ogg/Vorbis,
FLAC and many others.

%prep
%setup -q
#patch0 -p1
#patch1 -p1

%build
%{qmake_qt4}
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%doc CHANGES README
%{_bindir}/coquillo
%{_datadir}/applications/coquillo.desktop
%{_datadir}/pixmaps/coquillo.png
