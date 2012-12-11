%define name 		pftp
%define version 	1.1.6
%define release 	%mkrel 15

Summary: 	Port-File-Transfer-Program not to muddle up with standard FTP
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		Networking/File transfer
License: 	GPL
URL: 		http://www.pftp.de/
Source0: 	%{name}-%{version}.tar.bz2
Source1:	faq.html.bz2
Source2:	pftp-xinetd
Patch0:		%{name}-mdk.patch.bz2
Buildrequires:	openssl-devel glibc-static-devel 
BuildRoot: 	%{_tmppath}/%{name}-buildroot


%description
pftp allows you to send and receive files and directories recursively, 
send and receive standard input and ouput, filter your connection, set 
the net buffer size, set the bandwidth, send UDP datagrams unicasted, 
broadcasted, and multicasted (which is meant for AUDIO and VIDEO streaming), 
send data to another user and manage that data, perform a network test 
based on either UDP or TCP, and use optimized buffers for your Gigabit 
Ethernet links. pftp can start from command line, as a daemon, or by
inetd. All features are supported for IPv4 and IPv6.

%prep

%setup -q
%patch0 -p1 

%build
%__make

%install
[ -d $RPM_BUILD_ROOT ] && rm -r $RPM_BUILD_ROOT;

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/xinetd.d}

install -m644 pftp.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m644 %SOURCE2 $RPM_BUILD_ROOT%{_sysconfdir}/xinetd.d/pftp
bzcat %SOURCE1 > faq.html

%makeinstall  BINDIR=$RPM_BUILD_ROOT%{_sbindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
[ -d $RPM_BUILD_ROOT ] && rm -r $RPM_BUILD_ROOT;

%post
cp /etc/services /etc/services.pftp.save
cat /etc/services.pftp.save | \
grep -v "^"pftp | grep -v "^#pftp"  > /etc/services
echo "pftp      662/tcp		# pftp service" >> /etc/services 
rm -f /etc/services.pftp.save 

%files 
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/xinetd.d/pftp
%config(noreplace) %{_sysconfdir}/pftp.conf
%{_sbindir}/*
%defattr(644,root,root,755)
%doc INSTALL README TODO COPYING CREDITS Changes faq.html pftp.conf
%{_mandir}/man*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1.6-15mdv2010.0
+ Revision: 430681
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1.6-14mdv2009.0
+ Revision: 258929
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1.6-13mdv2009.0
+ Revision: 246849
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.1.6-11mdv2008.1
+ Revision: 124153
- kill re-definition of %%buildroot on Pixel's request
- import pftp


* Tue Dec 27 2005 Lenny Cartier <lenny@mandriva.com> 1.1.6-11mdk
- rebuild

* Tue Oct 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-10mdk
- rebuild

* Sat Sep 13 2003 Michael Scherer <scherer.michael@free.fr> 1.1.6-9mdk 
- BuildRequires glibc-devel-static

* Fri Sep 05 2003 Michael Scherer <scherer.michael@free.fr> 1.1.6-8mdk 
- Buildrequires openssl-devel
- fix /etc/services modification

* Tue May 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-7mdk
- buildrequires

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-6mdk
- rebuild

* Wed Aug 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-5mdk
- rebuild

* Fri Aug 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-4mdk
- rebuild

* Wed Jan 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-3mdk
- rebuild

* Tue Sep 12 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-2mdk
- BM

* Sun Jul 16 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 1.1.6-1mdk
- Mandrakized version
- Added xinetd support

