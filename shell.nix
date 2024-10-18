{ pkgs ? import <nixpkgs> {} }: pkgs.mkShell {
  packages = [
    pkgs.python3
    pkgs.python3Packages.fastapi
    pkgs.python3Packages.aiosmtplib
    pkgs.python3Packages.websockets
    pkgs.python3Packages.uvicorn
    pkgs.python3Packages.rich
    pkgs.python3Packages.pyjwt
    pkgs.python3Packages.passlib
    pkgs.python3Packages.bcrypt
  ];
}
