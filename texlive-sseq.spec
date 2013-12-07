# revision 31585
# category Package
# catalog-ctan /macros/latex/contrib/sseq
# catalog-date 2013-09-06 14:59:23 +0200
# catalog-license lppl
# catalog-version 2.01
Name:		texlive-sseq
Version:	2.01
Release:	4
Summary:	Typesetting spectral sequence charts
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

%description
The package provides commands to draw spectral sequence
diagrams, providing facilities for clipping and arranging
multiple symbols so that they do not overlap. The package is
built using pgf, and shares that systems large demands for TeX
system memory. Its geometric commands are based on a turtle
graphics model, and control structures such as loops and
conditionals are available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sseq/sseq.sty
%doc %{_texmfdistdir}/doc/latex/sseq/sseq.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sseq/sseq.dtx
%doc %{_texmfdistdir}/source/latex/sseq/sseq.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
