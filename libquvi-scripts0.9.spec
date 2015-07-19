%define oname libquvi-scripts
%define api 0.9

Summary:	Embedded lua scripts for parsing media details
Name:		%{oname}%{api}
Version:	0.9.20131130
Release:	4
Group:		Networking/Other
License:	LGPLv2+
Url:		http://quvi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/quvi/%{oname}-%{version}.tar.xz
BuildArch:	noarch
Obsoletes:	%{oname} = 0.9

%description
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{oname}-devel = 0.9

%description devel
The pkgconfig for %{name}.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure --libdir=%{_datadir}
%make

%install
%makeinstall_std

mv %{buildroot}%{_mandir}/man7/libquvi-scripts.7  %{buildroot}%{_mandir}/man7/libquvi-scripts0.9.7
%files
%doc ChangeLog COPYING README
%dir %{_datadir}/%{oname}
%{_datadir}/%{oname}/%{api}
%dir %{_datadir}/%{oname}/%{version}
%{_datadir}/%{oname}/%{version}/*
%{_mandir}/man7/*

%files devel
%{_datadir}/pkgconfig/%{oname}-%{api}.pc
