Copr repository for COPR repo for https://github.com/Zamundaaa/VK_hdr_layer, commits are fetched every hour.

The packages in this repo should work on Fedora 40+.

See the COPR page here: https://copr.fedorainfracloud.org/coprs/jackgreiner/vk-hdr-layer

## Installation 

Activate the repo with `sudo dnf copr enable jackgreiner/vk-hdr-layer` and then run `sudo dnf update --refresh`.

Install the package with `sudo dnf install vk-hdr-layer`

To revert this, remove the package with `sudo dnf install vk-hdr-layer` and remove the copr repository with `sudo dnf copr remove jackgreiner/vk-hdr-layer`.

## Issues

Feel free to open issues when there are build issues I haven't fixed for a few days: https://github.com/ProjectSynchro/copr-vk-hdr-layer/issues

If you'd like me to attempt to package this for other RPM based distros like SUSE, open an issue and I'll see what I can do :)

## Testing

To test build this package locally using `fedpkg`, follow these steps:

1. Install `fedpkg`:
   ```sh
   sudo dnf install fedpkg
   ```

3. Prepare the sources:
   ```sh
   fedpkg prep
   ```

4. Build the package:
   ```sh
   fedpkg local
   ```

This will create the RPM packages in the `x86_64` (or whatever arch you are building this package for) directory under the current working directory.