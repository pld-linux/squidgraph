%include	/usr/lib/rpm/macros.perl
Summary:	Squid logfile analyzer and traffic grapher
Summary(pl.UTF-8):	Program do analizy logów Squida i rysowania wykresów ruchu
Name:		squidgraph
Version:	3.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://squid-graph.securlogic.com/files/stable/squid-graph-%{version}.tar.gz
# Source0-md5:	e9565daabc23599094ed2d0e9a984d5e
URL:		http://squid-graph.securlogic.com/
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squid Graph is a free, simple, yet powerful Squid v2 native logfile
analysis tool that generates reports with graphical representation of
the proxy server's traffic.

%description -l pl.UTF-8
Squid Graph to wolnodostępne, proste lecz mające duże możliwości
narzędzie do analizy natywnych plików logów Squida 2, generujące
raporty z graficzną reprezentacją ruchu przechodzącego przez serwer
proxy.

%prep
%setup -q -n squid-graph-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install bin/squid-graph $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{README,html} images/*
%doc bin/{apacheconv,generate.cgi,timeconv}
%attr(755,root,root) %{_sbindir}/*
