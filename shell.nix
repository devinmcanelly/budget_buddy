{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/360a7d31c30abefdc490d203f80e3221b7a24af2.tar.gz") {} ## nixos-23.05 9/16/2023
}:

pkgs.mkShell {
  packages = [
    (pkgs.python311.withPackages (ps: [
      ps.flask
      ps.openpyxl
      ps.pandas
      ps.ipython
      ps.numpy
    ]))

    pkgs.curl
    pkgs.jq
    pkgs.tree
  ];
}
