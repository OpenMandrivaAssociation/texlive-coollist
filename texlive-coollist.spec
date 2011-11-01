Name:		texlive-coollist
Version:	1.4
Release:	1
Summary:	Manipulate COntent Oriented LaTeX Lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coollist
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coollist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coollist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coollist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Lists are defined as a sequence of tokens separated by a comma.
The coollist package allows the user to access certain elements
of the list while neglecting others--essentially turning lists
into a sort of array. Lists elements are accessed by specifying
the position of the object within the list (the index of the
item).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
