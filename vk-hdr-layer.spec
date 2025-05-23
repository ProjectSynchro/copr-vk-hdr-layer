%global tag 0
%global date 20250522
%global commit 1384036
%global longcommit 1384036ea24a9bc38a5c684dac5122d5e3431ae6

Name:           vk-hdr-layer
Version:        %{tag}
Release:        1.%{date}git%{commit}%{?dist}
Summary:        Implements HDR vulkan extensions in Wayland compositors that support it.

# SPDX
License:        GPL-3.0-only
URL:            https://github.com/Zamundaaa/VK_hdr_layer

BuildRequires:       gcc-c++
BuildRequires:       meson
BuildRequires:       git
BuildRequires:       pkgconfig(x11)
BuildRequires:       pkgconfig(vulkan)
BuildRequires:       pkgconfig(vkroots)
BuildRequires:       pkgconfig(wayland-client)
BuildRequires:       pkgconfig(wayland-scanner)

Recommends:          mesa-dri-drivers
Recommends:          mesa-vulkan-drivers

%description
The %{name} package contains the VK_hdr_layer Vulkan layer which implements HDR vulkan extensions in Wayland compositors that support it.

%prep
git clone --single-branch --branch main https://github.com/Zamundaaa/VK_hdr_layer
cd VK_hdr_layer
git checkout %{longcommit}
git submodule update --init --recursive

%build
cd VK_hdr_layer

MESON_OPTIONS=(
   --wrap-mode=nofallback
)

%meson "${MESON_OPTIONS[@]}"
%meson_build

%install
cd VK_hdr_layer
%meson_install

%files
%{_libdir}/libVkLayer_hdr_wsi.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_hdr_wsi.*.json

%changelog
%autochangelog
