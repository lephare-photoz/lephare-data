import sys
import pooch
from pathlib import Path

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

    with open(registry_name, "a", encoding="utf-8") as outfile:
        for fname, fhash in zip(files, hashes):
            # Pooch requires us to use Unix separators for the registry
            outfile.write("{} {}\n".format(
                fname.replace("\\", "/"),
                fhash
            ))


if __name__ == "__main__":
    #filename = sys.argv[1]
    #registry_file = sys.argv[2]
    #print(f"Adding {filename} to registry {registry_file}...")
    data_dir = sys.argv[1]
    registry_name = sys.argv[2]
    print(f"Making registry at {registry_name} for data dir {data_dir}...")
    make_registry_for_data_dir(".", data_dir, registry_name)

