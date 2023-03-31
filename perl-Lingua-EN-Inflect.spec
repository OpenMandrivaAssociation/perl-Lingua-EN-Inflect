%define module Lingua-EN-Inflect

Name: perl-%{module}
Version: 1.905
Release: 2
Summary: Convert singular to plural. Select "a" or "an".
URL: https://metacpan.org/pod/%{module}
Source: https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/%{module}-%{version}.tar.gz
License: Perl (Artistic or GPL)
Group: Development/Languages
BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: make

%description
Convert singular to plural. Select "a" or "an".

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
