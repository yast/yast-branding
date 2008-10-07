#
# spec file for package yast2-branding-openSUSE (Version 2.17.0)
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           yast2-branding-openSUSE
Version:        2.17.0
Release:        6
License:        GPL v2 or later
Group:          System/YaST
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        COPYING
Prefix:         /usr
BuildRequires:  yast2-devtools
BuildArch:      noarch
Provides:       yast2-branding
Conflicts:      otherproviders(yast2-branding)
Requires:       yast2-theme-openSUSE-any
Summary:        openSuSE branding for YaST

%description
YaST branding for the openSUSE distribution



%prep

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/doc/packages/yast2-branding-openSUSE
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/YaST2/theme
cp $RPM_SOURCE_DIR/COPYING $RPM_BUILD_ROOT%{prefix}/share/doc/packages/yast2-branding-openSUSE
cd $RPM_BUILD_ROOT%{prefix}/share/YaST2/theme
ln -sf openSUSE-current current

%files
%defattr(644,root,root,755)
%dir %{prefix}/share/YaST2/theme
%{prefix}/share/doc/packages/yast2-branding-openSUSE/
%{prefix}/share/YaST2/theme/current

%changelog
* Thu Sep 11 2008 jsrain@suse.cz
- initial package (fate #301794)
