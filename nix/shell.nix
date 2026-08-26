{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  # One coherent interpreter: `python3` and its site-packages agree on the
  # version, so pyrefly can learn everything from a single query (no
  # PYTHONPATH injection, no version/site-package mismatch warning).
  packages = [
    (pkgs.python314.withPackages (ps: [
      ps.dataclasses-json
    ]))
  ];
}
