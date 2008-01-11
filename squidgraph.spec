%include	/usr/lib/rpm/macros.perl
Summary:	Squid logfile analyzer and traffic grapher
Summary(pl.UTF-8):	Program do analizy logów Squida i rysowania wykresów ruchu
Name:		squidgraph
Version:	3.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/squid-graph/squid-graph-%{version}.tar.gz
# Source0-md5:	7ed7d187f87bde1ec9dabe05f07053b5
URL:		http://squid-graph.sourceforge.net/
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
%setup -q -n squid-graph

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install squid-graph $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc apacheconv generate.cgi timeconv
%attr(755,root,root) %{_sbindir}/squid-graph
