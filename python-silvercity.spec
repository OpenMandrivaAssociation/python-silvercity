%define shortname SilverCity
Name:           python-silvercity
Version:        0.9.7
Release:        11
Summary:        Lexing package, based on Scintilla
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

# Fix dummy source file permissions
find . -type f -exec chmod a+r {} \;
find . \( -name "*.cxx" -o -name "*.h" \) -exec chmod a-x {} \;

sed -i "s,/usr/home/sweetapp/bin/python,/usr/bin/env python," PySilverCity/Scripts/cgi-styler-form.py

# fix .css permissions
chmod 644 CSS/default.css

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}

%files
%{_bindir}/cgi-styler-form.py
%{_bindir}/cgi-styler.py
%{_bindir}/source2html.py
%{py_platsitedir}/*

