Summary:        Embedded lua scripts for parsing media details
Name:           libquvi-scripts
Version:	0.9.20131104
Release:	3
Group:		Networking/Other
License:        LGPLv2+
Url:            http://quvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
The pkgconfig for %{name}.

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
%{_mandir}/man7/*

%files devel
%{_datadir}/pkgconfig/*.pc

