#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Importer
Version  : 0.026
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Importer-0.026.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Importer-0.026.tar.gz
Summary  : 'Alternative but compatible interface to modules that export symbols.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Importer-license = %{version}-%{release}
Requires: perl-Importer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Importer - Alternative but compatible interface to modules that export
symbols.

%package dev
Summary: dev components for the perl-Importer package.
Group: Development
Provides: perl-Importer-devel = %{version}-%{release}
Requires: perl-Importer = %{version}-%{release}

%description dev
dev components for the perl-Importer package.


%package license
Summary: license components for the perl-Importer package.
Group: Default

%description license
license components for the perl-Importer package.


%package perl
Summary: perl components for the perl-Importer package.
Group: Default
Requires: perl-Importer = %{version}-%{release}

%description perl
perl components for the perl-Importer package.


%prep
%setup -q -n Importer-0.026
cd %{_builddir}/Importer-0.026

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Importer
cp %{_builddir}/Importer-0.026/LICENSE %{buildroot}/usr/share/package-licenses/perl-Importer/9338d181c35500f6234819031096e61d55a6bdd5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Importer.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Importer/9338d181c35500f6234819031096e61d55a6bdd5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Importer.pm
