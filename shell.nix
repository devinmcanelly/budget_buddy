{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: [
      ps.flask
      ps.openpyxl
      ps.pandas
      ps.sqlalchemy
      ps.ipython
      ps.numpy
    ]))

    pkgs.curl
    pkgs.jq
  ];
}
