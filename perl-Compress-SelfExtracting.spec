%define		pdir	Compress
%define		pnam	SelfExtracting
Summary:	Compress::SelfExtracting - create compressed scripts
Summary(pl.UTF-8):	Compress::SelfExtracting - tworzenie samorozpakowujących się skryptów
Name:		perl-Compress-SelfExtracting
Version:	0.04
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	e1151e0602e01f88e6c8ae1f4ea70b59
URL:		http://search.cpan.org/dist/Compress-SelfExtracting/
BuildRequires:	perl-Digest-MD5 >= 0.01
BuildRequires:	perl-Filter-Simple >= 0.01
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress::SelfExtracting allows you to create pure-Perl
self-extracting scripts using a variety of compression algorithms.
These scripts will then run on any system with a recent version of
Perl.

%description -l pl.UTF-8
Moduł Compress::SelfExtracting pozwala na tworzenie czysto perlowych
samorozpakowujących się skryptów przy użyciu różnych algorytmów
kompresji. Te skrypty będą działały na każdym systemie ze współczesną
wersją Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Compress/SelfExtracting.pm
%{perl_vendorlib}/Compress/SelfExtracting
%{_mandir}/man3/*
