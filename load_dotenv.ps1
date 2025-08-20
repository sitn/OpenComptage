Get-Content ".env" | ForEach-Object {
    if ($_ -notmatch '^\s*(#|$)') {
        $k,$v = $_ -split '=', 2
        Set-Item "Env:$($k.Trim())" ($v.Trim())
    }
}
