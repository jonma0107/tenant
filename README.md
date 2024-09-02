# Tenants will share the same database but they will be separated by the sub-domains.

## Previously you have to configure the local machine from `nano etc/hosts` in the `hosts` file to test locally you configure `example.com` to point to `127.0.0.1`:

```bash
127.0.0.1       example.com
127.0.0.1       tenantone.example.com
127.0.0.1       tenanttwo.example.com
```
## Then we test in the browser with the subdomain and the view url:

![image](https://github.com/user-attachments/assets/5aa0448c-7619-4963-8f88-42d2291c756b)
