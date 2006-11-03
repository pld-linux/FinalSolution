Summary:	A distrubuted, multithreaded, multiprotocol password cracker
Summary(pl):	Rozproszony, wielow±tkowy, wieloprotoko³owy ³amacz hase³
Name:		FinalSolution
Version:	0.2
Release:	0.9
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/finalsolution/%{name}-%{version}.tar.gz
# Source0-md5:	229f1ef5852a75d5a48c07c67306416c
URL:		http://finalsolution.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FinalSolution is a network administrator's tool to check the strength
of network passwords. This is done by trying to crack the server you
want to test. FinalSolution is multithreaded - i.e., it makes many
simultaneous connections to the test server in order to optimize the
bandwidth usage. It is also distributed, which means you can make the
test from many computers to a single server. It could be useful in
some cases when the test server has more bandwidth than you. Using
distributed cracking helps optimize the bandwidth usage in the
server's side.

%description -l pl
FinalSolution to narzêdzie administratora sieci s³u¿±ce do sprawdzania
jako¶ci hase³. Robi to próbuj±c z³amaæ serwer, który chcemy
przetestowaæ. FinalSolution jest wielow±tkowy - czyli tworzy wiele
jednoczesnych po³±czeñ do testowanego serwera, aby zoptymalizowaæ
wykorzystanie pasma. Jest tak¿e rozproszony, co oznacza, ¿e mo¿na
testowaæ pojedynczy serwer z wielu komputerów. Mo¿e to byæ przydatne,
kiedy testowany serwer ma lepsze ³±cze od nas. U¿ycie ³amania
rozproszonego pomaga zoptymalizowaæ wykorzystanie pasma po stronie
serwera.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall -Wno-deprecated -c -Isrc/Include" \
	DEBUG=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install finalsolution $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
