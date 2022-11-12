Name:		texlive-coollist
Version:	63523
Release:	1
Summary:	Manipulate COntent Oriented LaTeX Lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coollist
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coollist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coollist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coollist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Lists are defined as a sequence of tokens separated by a comma.
The coollist package allows the user to access certain elements
of the list while neglecting others--essentially turning lists
into a sort of array. Lists elements are accessed by specifying
the position of the object within the list (the index of the
item).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/coollist/coollist.sty
%doc %{_texmfdistdir}/doc/latex/coollist/README
%doc %{_texmfdistdir}/doc/latex/coollist/coollist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/coollist/coollist.dtx
%doc %{_texmfdistdir}/source/latex/coollist/coollist.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
