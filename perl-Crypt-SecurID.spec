#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	SecurID
Summary:	Crypt::SecurID - generating and verifying SecurID time hash codes
Summary(pl):	Crypt::SecurID - generowanie i weryfikowanie kodów SecurID time hash
Name:		perl-Crypt-SecurID
Version:	0.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	f0ebb7c5e549557a197b2df746f21c91
BuildRequires:	libstdc++-devel
%{!?_without_tests:BuildRequires:	perl-Test-Simple >= 0.01}
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::SecurID is an emulator module for generating and verifying
SecurID time-hash codes. Such codes are often useful during identity
authentication, especially when the code is generated out-of-band
so that the 64-bit secret key is never on any client machine.

%description -l pl
Crypt::SecurID to modu³ emulatora do generowania i weryfikowania
kodów SecurID time-hash. Takie kody s± czêsto przydatne przy
uwierzytelnianiu, szczególnie kiedy kod jest generowany na zewn±trz,
tak ¿e 64-bitowy tajny klucz nigdy nie jest obecny na ¿adnej maszynie
klienckiej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	LD="%{__cxx}" \
	OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# note: COPYING is not GPL text, only copyright note
%doc COPYING Changes README
%{perl_vendorarch}/Crypt/SecurID.pm
%{perl_vendorarch}/Crypt/securid.pm
%dir %{perl_vendorarch}/auto/Crypt/securid
%{perl_vendorarch}/auto/Crypt/securid/securid.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/securid/securid.so
%{_mandir}/man3/*
