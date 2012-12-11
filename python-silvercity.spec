%define shortname SilverCity
Name:           python-silvercity
Version:        0.9.7
Release:        10
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
sed -i "s,/usr/home/sweetapp/bin/python,/usr/bin/env python," PySilverCity/Scripts/cgi-styler-form.py

# fix .css permissions
chmod 644 CSS/default.css

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir

%files
%defattr(-,root,root,-)
%{_bindir}/cgi-styler-form.py
%{_bindir}/cgi-styler.py
%{_bindir}/source2html.py
%{py_platsitedir}/*


%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.9.7-9mdv2011.0
+ Revision: 590089
- rebuild for python 2.7

* Fri Jan 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.7-8mdv2010.1
+ Revision: 495120
- fix file permissions

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.7-7mdv2010.0
+ Revision: 442484
- rebuild

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 0.9.7-6mdv2009.1
+ Revision: 318412
- rebuild for new python

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-5mdv2009.0
+ Revision: 259779
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-4mdv2009.0
+ Revision: 247634
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-2mdv2008.1
+ Revision: 171067
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 21 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.7-1mdv2008.1
+ Revision: 100735
- import python-silvercity


