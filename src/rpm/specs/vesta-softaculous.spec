Name:           vesta-softaculous
Version:        0.9.8
Release:        18
Summary:        Vesta Control Panel
Group:          System Environment/Base
License:        Softaculous License
URL:            https://www.softaculous.com
Vendor:         vestacp.com
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       redhat-release >= 5
Provides:       vesta-softaculous

%define         _vestadir  /usr/local/vesta/softaculous

%description
This package contains Softaculous apps for Vesta Control Panel web interface.

%prep
%setup -q -n %{name}-%{version}

%build

%install
install -d  %{buildroot}%{_vestadir}
%{__cp} -ad ./* %{buildroot}%{_vestadir}

%clean
rm -rf %{buildroot}

%post
if [ $1 -ge 1 ]; then
    if [ -e /usr/local/vesta/softaculous/vesta_install.inc ]; then
        cd /usr/local/vesta/php/bin/php  vesta_install.inc
        rm vesta_install.inc
    fi
fi


%files
%defattr(-,root,root)
%attr(755,root,root) %{_vestadir}
%config(noreplace) %{_vestadir}/conf

%changelog
* Mon Jul 21 2017 Serghey Rodin <builder@vestacp.com> - 0.9.8-18
- Initial build for Softaculous 4.9.2