%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	SelfExtracting
Summary:	Compress::SelfExtracting Perl module
Summary(pl):	Modu³ Perla Compress::SelfExtracting
Name:		perl-Compress-SelfExtracting
Version:	0.04
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5 >= 0.01
BuildRequires:	perl-Filter-Simple
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
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
%{perl_sitelib}/Compress
%{_mandir}/man3/*
