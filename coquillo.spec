Summary:	Audio Metadata Editor
Name:		coquillo
Version:	1.12
Release:	2
License:	GPLv2+
Group:		Sound
Url:		https://github.com/sjuvonen/coquillo
Source0:	http://cs.joensuu.fi/~sjuvonen/coquillo/%{version}/%{name}-%{version}-src.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(taglib)

%description
Coquillo is a metadata editor, or so-called tagger utility, with which you can
edit tags of many different audio files. Its support includes MP3, Ogg/Vorbis,
FLAC and many others.

%files
%doc CHANGES README
%{_bindir}/coquillo
%{_datadir}/applications/coquillo.desktop
%{_datadir}/pixmaps/coquillo.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

