# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sseq
# catalog-date 2009-04-10 15:43:04 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-sseq
Version:	2.0
Release:	1
Summary:	Spectral sequence diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sseq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sseq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sseq.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sseq.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides commands to draw spectral sequence
diagrams, providing facilities for clipping and arranging
multiple symbols so that they do not overlap. The package is
built using pgf, and shares that systems large demands for TeX
system memory. Its geometric commands are based on a turtle
graphics model, and control structures such as loops and
conditionals are available.

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
%{_texmfdistdir}/tex/latex/sseq/sseq.sty
%doc %{_texmfdistdir}/doc/latex/sseq/sseq.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sseq/sseq.dtx
%doc %{_texmfdistdir}/source/latex/sseq/sseq.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
