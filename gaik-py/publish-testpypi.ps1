$envVars = Get-Content .env | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]+)=(.*)$') {
        [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
    }
}

twine upload `
  --repository-url https://test.pypi.org/legacy/ `
  -u __token__ `
  -p $env:TEST_PYPI_API_TOKEN `
  dist/*
