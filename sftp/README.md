# sftp

- <https://hub.docker.com/r/atmoz/sftp>

Edit the config file:

```
cp env .env
# Change the Environment variable
```

- `SFTP_PATH` the folder you want to share with sftp
- `SFTP_CONFIG` point to `users.conf` file

## users.conf
users.conf 是 SFTP 的配置文件，内容语法：

```
user:pass[:e][:uid[:gid[:dir1[,dir2]...]]] ...
```

举例说明：

```
foo:123:1001:100
```

表示的含义就是创建一个名为 `foo`，密码为 `123` 的用户，其 UID 是 1001，GID 是 100.

记住如果这里需要设置一个加密的密码，可以使用：

```
echo -n "your-password" | docker run -i --rm atmoz/makepasswd --crypt-md5 --clearfrom=-
```

然后配置：

```
foo:$1$0G2g0GSt$ewU0t6GXG15.0hWoOX8X9.:e:1001
```

注意在生成的密码后面加上 `:e`。


## Mount volumes

SFTP 的用户可以访问 `/home/foo` 目录，但是不能在 HOME 目录下创建文件夹，所以保证至少 mount 一个子文件夹以供用户读写。


## sftp cli

```
sftp -P 2222 -o PreferredAuthentications=password -o PubKeyAuthentication=no foo@ip.of.your.server:
```

And the enter the password you set.
