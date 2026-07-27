{
  description = "devshell for learning python";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };
  outputs = { nixpkgs, ... }:
      let
        inherit (nixpkgs.lib) genAttrs;
        systems = [
          "x86_64-linux"
          "aarch64-linux"
          "x86_64-darwin"
          "aarch64-darwin"
        ];
        forEachSystem =
          perSystem:
          genAttrs systems (
            system:
            let
              pkgs = nixpkgs.legacyPackages.${system};
            in
              perSystem { inherit pkgs system; }
          );
      in {
        packages =  forEachSystem (
          { pkgs, ...}:
            {
              default = pkgs.callPackage ./nix/devshell.nix {};
            }
          );
        };
}
