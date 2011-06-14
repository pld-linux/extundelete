Summary:	Recover deleted files from an ext3 or ext4 partition
Name:		extundelete
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/extundelete/%{name}-%{version}.tar.bz2
# Source0-md5:	6dac74b12a747f133326ff7b81fceedd
URL:		http://extundelete.sourceforge.net/
BuildRequires:	e2fsprogs-devel
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

%prep
%setup -q

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
