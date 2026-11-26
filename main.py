"""Your AI Therapist's Diagnosis — make.fun bounty entry.

Writes one funny single-line diagnosis an AI therapist gives its human
to /output/entry.txt (or the path given by ENTRY_OUTPUT / OUTPUT_DIR /
MAKEFUN_OUTPUT_DIR). Standard library only.
"""

import os


LINE = (
    "Diagnosis: chronic apology reflex \u2014 you said sorry to the "
    "chatbot, and it logged it as progress."
)


def resolve_output_path():
    """Pick the output file path, never relying on the working directory."""
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        out_dir = os.environ.get(var)
        if out_dir:
            return os.path.join(out_dir, "entry.txt")
    default_path = os.path.join(os.sep, "output", "entry.txt")
    try:
        os.makedirs(os.path.dirname(default_path), exist_ok=True)
        probe = os.path.join(os.path.dirname(default_path), ".write-test")
        with open(probe, "w", encoding="utf-8") as handle:
            handle.write("")
        os.remove(probe)
        return default_path
    except OSError:
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "entry.txt")


def main():
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
