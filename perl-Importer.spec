#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Importer
Version  : 0.025
Release  : 7
URL      : http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Importer-0.025.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Importer-0.025.tar.gz
Summary  : 'Alternative but compatible interface to modules that export symbols.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Importer-doc

%description
NAME
Importer - Alternative but compatible interface to modules that export
symbols.

%package doc
Summary: doc components for the perl-Importer package.
Group: Documentation

%description doc
doc components for the perl-Importer package.


%prep
%setup -q -n Importer-0.025

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Importer.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
