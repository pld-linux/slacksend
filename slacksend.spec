Summary:	Sends messages to Slack's incoming webhooks via CLI
Name:		slacksend
Version:	0.1
Release:	9
License:	MIT
Group:		Applications/Networking
Source0:	https://pypi.python.org/packages/source/s/slacksend/%{name}-%{version}.tar.gz
# Source0-md5:	c6ec90dba9d1c0b3aae091a54b476585
URL:		https://github.com/mtorromeo/slacksend
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sends messages to Slack's incoming webhooks via CLI

CLI tool to send messages to the Incoming webhook of Slack
<https://slack.com>.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%attr(755,root,root) %{_bindir}/slacksend
%{py3_sitescriptdir}/slacksend.py
%{py3_sitescriptdir}/__pycache__/slacksend.*.pyc
%{py3_sitescriptdir}/slacksend-%{version}-py*.egg-info
