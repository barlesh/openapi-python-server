import connexion
import os

spec_dir = os.environ.get("SPEC_DIR", 'openAPI/')
spec_file = os.environ.get("SPEC_FILE", 'api.yaml')
port = os.environ.get("PORT", 8080)

app = connexion.App(__name__, specification_dir=spec_dir)
app.add_api(spec_file)
app.run(port=port)