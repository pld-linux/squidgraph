%include	/usr/lib/rpm/macros.perl
Summary:	Squid logfile analyzer and traffic grapher
Summary(pl):	Program do analizy logów Squida i rysowania wykresów ruchu
Name:		squidgraph
Version:	3.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://squid-graph.securlogic.com/files/stable/squid-graph-%{version}.tar.gz
# Source0-md5:	e9565daabc23599094ed2d0e9a984d5e
URL:		http://squid-graph.securlogic.com/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-GD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squid Graph is a free, simple, yet powerful Squid v2 native logfile
analysis tool that generates reports with graphical representation of
the proxy server's traffic.

%description -l pl
Squid Graph to wolnodostêpne, proste lecz maj±ce du¿e mo¿liwo¶ci
narzêdzie do analizy natywnych plików logów Squida 2, generuj±ce
raporty z graficzn± reprezentacj± ruchu przechodz±cego przez serwer
proxy.

%prep
%setup -q -n squid-graph-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/squid-graph $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{README,html} images/*
%doc bin/{apacheconv,generate.cgi,timeconv}
%attr(754,root,root) %{_bindir}/*
