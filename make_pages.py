import os
import markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader

# Diretório dos arquivos Markdown
markdown_dir = "posts"

# Diretório dos templates HTML
template_dir = "templates"

# Diretório dos recursos estáticos (CSS, imagens, etc.)
static_dir = "static"

# Criar o diretório de saída se não existir
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Carregar o template
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("post_template.html")

# Processar cada arquivo Markdown
for markdown_file in os.listdir(markdown_dir):
    if markdown_file.endswith(".md"):
        # Ler o conteúdo do arquivo Markdown usando frontmatter
        with open(os.path.join(markdown_dir, markdown_file), "r", encoding="utf-8") as f:
            post = frontmatter.load(f)

        # Converter Markdown para HTML
        html_content = markdown.markdown(post.content)

        # Criar um dicionário de contexto para o template
        context = {"post": {"titulo": post.get("titulo", ""),
                            "autor": post.get("autor", ""),
                            "data": post.get("data", ""),
                            "conteudo": html_content}}

        # Renderizar o template com o contexto
        html_output = template.render(context)

        # Salvar o HTML gerado
        html_file = os.path.splitext(markdown_file)[0] + ".html"
        with open(os.path.join(output_dir, html_file), "w", encoding="utf-8") as f:
            f.write(html_output)