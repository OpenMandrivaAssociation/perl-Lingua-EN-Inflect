%define upstream_name	 Lingua-EN-Inflect
%define upstream_version 1.895

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl module to find English word inflections
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/Lingua-EN-Inflect-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The exportable subroutines of Lingua::EN::Inflect provide plural inflections,
"a"/"an" selection for English words, and manipulation of numbers as words.
Plural forms of all nouns, most verbs, and some adjectives are provided. Where
appropriate, "classical" variants (for example: "brother" -> "brethren",
"dogma" -> "dogmata", etc.) are also provided.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 644 README Changes lib/Lingua/EN/Inflect.pm
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Lingua/*
%{_mandir}/*/*

%changelog
* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.893.0-1mdv2011.0
+ Revision: 597079
- new version

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.892.0-1mdv2011.0
+ Revision: 552384
- update to 1.892

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.891.0-1mdv2010.1
+ Revision: 461323
- update to 1.891

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.890.0-1mdv2010.0
+ Revision: 407789
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.89-4mdv2009.0
+ Revision: 241599
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.89-2mdv2008.0
+ Revision: 86519
- rebuild


* Mon Jul 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.89-1mdk
- 1.89, complete rewrite of specfile

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 1.88-1mdk
- Initial build.


