import os
import sys
import pooch
from pathlib import Path


def write_hashes_to_registry(files, hashes, registry_name):
    with open(registry_name, "a", encoding="utf-8") as outfile:
        for fname, fhash in zip(files, hashes):
            # Pooch requires us to use Unix separators for the registry
            outfile.write("{} {}\n".format(
                fname.replace("\\", "/"),
                fhash
            ))
    print(f"Added {len(files)} files to registry {registry_name}.")


def make_registry_for_data_file(filename, registry_file):
    """
    Make a registry of files and hashes for the given file.

    Parameters
    ----------
    filename : str
        Name of the file to put in the registry.
    registry_file : str
        Name of the output registry file.

    """
    hash = pooch.file_hash(filename)
    write_hashes_to_registry([filename], [hash], registry_file)


def make_registry_for_data_dir(directory, data_dir, registry_name, recursive=True):
    """
    Make a registry of files and hashes for the given subdir, but as if we
    had specified the top level dir (TODO wording here)

    This is helpful if you have many files in your test dataset as it keeps you
    from needing to manually update the registry.

    Parameters
    ----------
    directory : str
        Directory of the test data to put in the registry. All file names in
        the registry will be relative to this directory.
    output : str
        Name of the output registry file.
    recursive : bool
        If True, will recursively look for files in subdirectories of
        *directory*.

    """
    directory = Path(directory)
    data_dir = Path(data_dir)
    if recursive:
        pattern = "**/*"
    else:
        pattern = "*"

    files = sorted(
        str(path.relative_to(directory))
        for path in data_dir.glob(pattern)
        if path.is_file()
    )

    hashes = [pooch.file_hash(str(directory / fname)) for fname in files]
    write_hashes_to_registry(files, hashes, registry_name)


if __name__ == "__main__":
    data_to_hash = sys.argv[1]
    registry_name = sys.argv[2]
    registry_hash_name = f"{os.path.splitext(registry_name)[0]}-hash.txt"

    if os.path.isfile(data_to_hash):
        print(f"Making registry at {registry_name} for file {data_to_hash}...")
        make_registry_for_data_file(data_to_hash, registry_name)
    else:
        print(f"Making registry at {registry_name} for data dir {data_to_hash}...")
        make_registry_for_data_dir(".", data_to_hash, registry_name)
    
    print(f"Making hash file at {registry_hash_name} for registry {registry_name}...")
    registry_hash = pooch.file_hash(registry_name)
    with open(registry_hash_name, "w", encoding="utf-8") as outfile:
        outfile.write(registry_hash)
