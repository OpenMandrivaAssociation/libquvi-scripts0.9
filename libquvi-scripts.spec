%define major 6
%define libname %mklibname quvi-scripts %major
%define develname %mklibname -d quvi-scripts

Name:           libquvi-scripts
Version:        0.4.7
Release:        1
Summary:        Embedded lua scripts for parsing media details
Group:          Networking/Other
License:        LGPLv2+
URL:            http://quvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%prep
%setup -q

%build
%configure2_5x --libdir=%{_datadir}
%make

%install
%makeinstall_std

%files
%doc ChangeLog COPYING README
%{_datadir}/%{name}
%{_datadir}/pkgconfig/*.pc
%{_mandir}/man7/*


