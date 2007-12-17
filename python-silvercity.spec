%define shortname SilverCity
Name:           python-silvercity
Version:        0.9.7
Release:        %mkrel 1
Summary:        SilverCity is a lexing package, based on Scintilla
Group:          Development/Python
License:        BSD-like
URL:            http://silvercity.sourceforge.net/
Source0:        http://garr.dl.sourceforge.net/sourceforge/silvercity/%{shortname}-%{version}.tar.gz

BuildRequires:  python-devel

%description
SilverCity is a lexing package, based on Scintilla, that can provide lexical
analysis for over 20 programming and markup langauges.

Scripting language bindings currently exist for Python. 

%prep
%setup -q -n %{shortname}-%{version}
sed -i "s,/usr/home/sweetapp/bin/python,/usr/bin/env python," PySilverCity/Scripts/cgi-styler-form.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/cgi-styler-form.py
%{_bindir}/cgi-styler.py
%{_bindir}/source2html.py
%{py_platsitedir}/*
