Summary:	Squid logfile analyzer and traffic grapher
Name:		squidgraph
Version:	3.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://squid-graph.securlogic.com/files/stable/squid-graph-%{version}.tar.gz
# Source0-md5:	e9565daabc23599094ed2d0e9a984d5e
URL:		http://squid-graph.securlogic.com/
Requires:	perl-GD
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squid Graph is a free, simple, yet powerful Squid v2 native logfile
analysis tool that generates reports with graphical representation of
the proxy server's traffic.
%prep
%setup -q -n squid-graph-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install bin/squid-graph $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(754,root,root) %{_bindir}/*
