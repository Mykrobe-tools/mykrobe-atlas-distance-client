java -jar ./openapi-generator-cli-4.2.2.jar generate \
  -i https://raw.githubusercontent.com/Mykrobe-tools/mykrobe-atlas-distance-api/release/dev/swagger.yaml \
  -g python \
  -c codegen_configuration.yaml \
  -o .
