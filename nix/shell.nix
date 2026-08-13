{pkgs ? import <nixpkgs>}:
pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    python3
    python313Packages.dataclasses-json
  ];
}
