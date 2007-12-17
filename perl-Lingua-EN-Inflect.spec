%define module	Lingua-EN-Inflect
%define name	perl-%{module}
%define version 1.89
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module to find English word inflections
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch

%description
The exportable subroutines of Lingua::EN::Inflect provide plural inflections,
"a"/"an" selection for English words, and manipulation of numbers as words.
Plural forms of all nouns, most verbs, and some adjectives are provided. Where
appropriate, "classical" variants (for example: "brother" -> "brethren",
"dogma" -> "dogmata", etc.) are also provided.

%prep
%setup -q -n %{module}-%{version}

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

