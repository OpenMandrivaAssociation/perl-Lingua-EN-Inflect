%define upstream_name	 Lingua-EN-Inflect
%define upstream_version 1.89

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module to find English word inflections
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Lingua/*
%{_mandir}/*/*
