# wakapi
A minimalist, self-hosted WakaTime-compatible backend for coding statistics.

- <https://github.com/muety/wakapi>

## Usage

```
cp env .env
```

and modify `.env`.

Generate `SALT`

```
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w ${1:-32} | head -n 1
```

Set `WAKAPI_DATA` to a local path.

## Read more

- <https://blog.einverne.info> search wakapi
