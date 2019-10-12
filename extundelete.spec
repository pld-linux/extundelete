Summary:	Recover deleted files from an ext3 or ext4 partition
Summary(pl.UTF-8):	Odtwarzanie usuniętych plików z partycji ext3 lub ext4
Name:		extundelete
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://download.sourceforge.net/extundelete/%{name}-%{version}.tar.bz2
# Source0-md5:	77e626ad31433680c0a222069295d2ca
Patch0:		%{name}-attrs.patch
Patch1:		%{name}-dirs.patch
Patch2:		e2fsprogs.patch
URL:		http://extundelete.sourceforge.net/
BuildRequires:	e2fsprogs-devel
BuildRequires:	libcom_err-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
extundelete is a utility that can recover deleted files from an ext3
or ext4 partition. The ext3 file system is the most common file system
when using Linux, and ext4 is its successor. extundelete uses the
information stored in the partition's journal to attempt to recover a
file that has been deleted from the partition. There is no guarantee
that any particular file will be able to be undeleted, so always try
to have a good backup system in place, or at least put one in place
after recovering your files!

%description
extundelete to narzędzie które potrafi odzyskać usunięte pliki z
partycji ext3 lub ext4. System plików ext3 jest najczęściej używanym
systemem plików pod Linuksem, a ext4 to jego następca. extundelete
wykorzystuje informacje zapisane w kronice partycji, aby spróbować
odtworzyć plik, który został wcześniej z partycji usunięty. Nie ma
gwarancji, że jakikolwiek plik da się odzyskać, więc nie należy
zapominać o kopiach zapasowych!

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
