{ inputs, pkgs, ... }:
{
  devShells.${system}.default = pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
      python3
    ];
  };
}
