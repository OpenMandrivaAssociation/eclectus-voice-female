Summary:	Han character dictionary
Name:		eclectus-voice-female
Version:	0.2
Release:	%mkrel 1
Group:		Development/Python
License:	GPLv3+
URL:		http://code.google.com/p/eclectus/
Source0:	http://eclectus.googlecode.com/files/cmn-caen-tan-%{version}beta.tar.gz
BuildArch:	noarch
Requires:	eclectus
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
Eclectus is a small Han character dictionary especially designed for
learners of Chinese character based languages like Mandarin Chinese
or Japanese.

%prep
%setup -qn cmn-caen-tan-%{version}beta

%install
rm -rf %{buildroot}
make install installpath=%{buildroot}%{_datadir}/eclectus/cmn-caen-tan

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/eclectus/cmn-caen-tan
