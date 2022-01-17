# searX
Privacy-respecting, hackable [metasearch engine](https://en.wikipedia.org/wiki/Metasearch_engine).

- <https://github.com/searx/searx>


# Morty
Morty is a web content sanitizer proxy.

- <https://github.com/dalf/morty>

Morty can be configured using the following environment variables:

- `MORTY_ADDRESS`: Listen address (default to `127.0.0.1:3000`)
- `MORTY_KEY`: HMAC url validation key (base64 encoded) to prevent direct URL opening. Leave blank to disable validation. Use `openssl rand -base64 33` to generate.
- `DEBUG`: Enable/disable proxy and redirection logs (default to `true`). Set to `false` to disable.

