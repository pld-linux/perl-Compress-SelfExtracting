%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	SelfExtracting
Summary:	Compress::SelfExtracting Perl module
Summary(pl):	Modu³ Perla Compress::SelfExtracting
Name:		perl-Compress-SelfExtracting
Version:	0.04
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	e1151e0602e01f88e6c8ae1f4ea70b59
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Digest-MD5 >= 0.01
BuildRequires:	perl-Filter-Simple
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress::SelfExtracting allows you to create pure-Perl
self-extracting scripts using a variety of compression algorithms.
These scripts will then run on any system with a recent version of
Perl.

%description -l pl
Modu³ Compress::SelfExtracting pozwala na tworzenie czysto perlowych
samorozpakowuj±cych siê skryptów przy u¿yciu ró¿nych algorytmów
kompresji. Te skrypty bêd± dzia³a³y na ka¿dym systemie ze wspó³czesn±
wersj± Perla.

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
%{perl_vendorlib}/Compress
%{_mandir}/man3/*
