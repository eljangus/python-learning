{
  description = "devshell for learning python";
  inputs = {
    nixpkgs.url = "https://channels.nixos.org/nixos-unstable/nixexprs.tar.zst";
  };
  outputs = {nixpkgs, ...}: {
    devShells = nixpkgs.lib.genAttrs nixpkgs.lib.systems.flakeExposed (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        default = pkgs.callPackage ./nix/shell.nix {};
      }
    );
  };
}
