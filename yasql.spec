%include	/usr/lib/rpm/macros.perl
Summary:	Yet Another SQL*Plus replacement
Summary(pl):	Yet Another SQL*Plus replacement
Name:		yasql
Version:	1.81
Release:	1
Group:		Applications/Databases
License:	GPL
URL:		http://sourceforge.net/projects/yasql/
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/yasql/%{name}-%{version}.tar.gz
# Source0-md5:	30ea822727aebd53ad1f5a3fe569718a
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a much kinder alternative to SQL*Plus. This does not provide
every feature that SQL*Plus does, only the ones needed for general ad
hoc queries. The main intent of this program is for viewing data in
the database, or testing queries. It is not intended to create fancy
reports, such as those featured in SQL*Plus. It also does not have any
sort of scripting language such as PL/SQL. It has a few native
commands, such as describe, show, quit, and everything else is passed
through to the Oracle server.

%description -l pl
Co¶ w rodzaju SQL*Plusa. Nie zawiera wszystkich bajerów orygina³u,
jedynie te niezbêdne do zadawania szybkich zapytañ. G³ówn± intencj±
powstania programu jest przegl±danie danych w bazie lub testowanie
pytañ. Nie jest jednak intencj± fantazyjnych takich, jakie s± dostêpne
w SQL*Plus. Nie ma tu równie¿ niczego co by przypomina³o jêzyk
skryptowy podobny do PL/SQL. Ma kilka w³asnych komend, takich jak
describe, show, quit; reszta jest przesy³ana do serwera Oracla.

%prep
%setup -q

%build
./configure --sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install -m 755 yasql $RPM_BUILD_ROOT%{_bindir}/
install yasql.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install yasql.conf $RPM_BUILD_ROOT%{_sysconfdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README yasql.html
%attr(755,root,root) %{_bindir}/yasql
%{_mandir}/man1/yasql.1*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/yasql.conf
