{ pkgs, ... }:
pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
      python3
    ];
}
