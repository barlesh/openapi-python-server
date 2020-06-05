docker run --rm -v "${PWD}/sdk/rest:/local" -v "${PWD}/openAPI:/tmp/openAPI" \
 openapitools/openapi-generator-cli generate \
    -i tmp/openAPI/api.yaml \
    -g python \
    -o /local/out/python