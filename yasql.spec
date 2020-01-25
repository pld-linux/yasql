Summary:	Yet Another SQL*Plus replacement
Summary(pl.UTF-8):	Yet Another SQL*Plus replacement - jeszcze jeden zamiennik SQL*Plus
Name:		yasql
Version:	1.83
Release:	2
Group:		Applications/Databases
License:	GPL v2
Source0:	http://dl.sourceforge.net/yasql/%{name}-%{version}.tar.gz
# Source0-md5:	c580402d20df6a1a0efe72d65a40ff0d
URL:		http://sourceforge.net/projects/yasql/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
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

%description -l pl.UTF-8
Coś w rodzaju SQL*Plusa. Nie zawiera wszystkich bajerów oryginału,
jedynie te niezbędne do zadawania szybkich zapytań. Główną intencją
powstania programu jest przeglądanie danych w bazie lub testowanie
pytań. Nie jest jednak intencją fantazyjnych takich, jakie są dostępne
w SQL*Plus. Nie ma tu również niczego co by przypominało język
skryptowy podobny do PL/SQL. Ma kilka własnych komend, takich jak
describe, show, quit; reszta jest przesyłana do serwera Oracle'a.

%prep
%setup -q

%build
./configure \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install yasql $RPM_BUILD_ROOT%{_bindir}
install yasql.1 $RPM_BUILD_ROOT%{_mandir}/man1
install yasql.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README yasql.html
%attr(755,root,root) %{_bindir}/yasql
%{_mandir}/man1/yasql.1*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yasql.conf
