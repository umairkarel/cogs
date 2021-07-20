# Verification

This Cog is used to add a verification system.


## add


With the `add` subcommand you can add a verification role.
If you set `reverse` to `true`, the role will be removed from the user instead of added.

```css
.verification [add|a|+] <role> [reverse=False]
```

Argument | Required            | Description
---------|---------------------|------------
role     | :heavy_check_mark:  | The verification role
reverse  |                     | The Role assignment will be reversed => Role will get removed

Required Permissions:

- `settings.change_prefix`


## delay


Set the Time you have to be on the Server until you can Verify.

```css
.verification [delay|d] <seconds>
```

Argument | Required            | Description
---------|---------------------|------------
delay    | :heavy_check_mark:  | The Time in Seconds


## password


Sets the *Secret* Password you'll need to Verify.

```css
.verification [password|p] <password>
```

Argument | Required            | Description
---------|---------------------|------------
password | :heavy_check_mark:  | The Password as string

!!! note
    Password has a Max-Length of 256 Chars


## remove


Removes an existing Verification.

```css
.verification [remove|r|-] <role>
```

Argument | Required            | Description
---------|---------------------|------------
role     | :heavy_check_mark:  | The Verification Role
