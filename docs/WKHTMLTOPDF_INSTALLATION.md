# Instalação do wkhtmltopdf

O **wkhtmltopdf** é necessário para gerar PDFs profissionais dos relatórios TNM. Este guia mostra como instalá-lo em diferentes sistemas operacionais.

> ⚡ **Usando Docker?** Se você usa Docker para desenvolvimento ou produção, **o wkhtmltopdf já está incluído** no `Dockerfile`! Não precisa instalar manualmente. Pule para a [seção Docker](#docker).

---

## 📋 Índice

- [Docker (Recomendado)](#docker)
- [Ubuntu / Debian](#ubuntu--debian)
- [macOS](#macos)
- [Verificação da Instalação](#verificação-da-instalação)
- [Resolução de Problemas](#resolução-de-problemas)

---

## 🐳 Docker (Recomendado)

**Se você usa Docker, wkhtmltopdf já está incluído!** ✅

O `Dockerfile` do projeto já inclui wkhtmltopdf e todas as suas dependências:

```dockerfile
# Incluído automaticamente no Dockerfile
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    fontconfig \
    libfreetype6 \
    fonts-roboto \
    # ... outras dependências
    && rm -rf /var/lib/apt/lists/*
```

### Como Usar com Docker

**1. Build da imagem:**

```bash
cd /home/warley/dev/ion-nutri

# Com docker-compose
docker-compose build

# Ou com docker build
docker build -t ion-nutri-api .
```

**2. Iniciar containers:**

```bash
# Iniciar todos os serviços
docker-compose up -d

# Ver logs
docker-compose logs -f api
```

**3. Verificar instalação:**

```bash
# Verificar se wkhtmltopdf está disponível no container
docker exec ion-nutri-api wkhtmltopdf --version

# Deve mostrar algo como:
# wkhtmltopdf 0.12.6
```

**4. Testar geração de PDF:**

- Acesse: http://localhost:8000/docs
- Use o endpoint `POST /api/v1/reports/pdf`
- Se funcionar, está tudo pronto! 🎉

### Reconstruir após mudanças

Se você fez alterações no código ou dependências:

```bash
# Parar containers
docker-compose down

# Rebuild e reiniciar
docker-compose up -d --build
```

### Docker em Produção

O mesmo `Dockerfile` funciona para produção. wkhtmltopdf será automaticamente instalado no container.

---

## 🐧 Ubuntu / Debian

### Instalação via APT

```bash
# Atualizar repositórios
sudo apt-get update

# Instalar wkhtmltopdf
sudo apt-get install -y wkhtmltopdf

# Verificar instalação
wkhtmltopdf --version
```

### Instalação Manual (Versão Mais Recente)

Se precisar da versão mais recente com suporte a Qt patches:

```bash
# Baixar o pacote (Ubuntu 22.04 / Jammy)
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb

# Instalar dependências
sudo apt-get install -y fontconfig libfreetype6 libjpeg-turbo8 libpng16-16 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base

# Instalar o pacote
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb

# Verificar instalação
wkhtmltopdf --version
```

**Para outras versões do Ubuntu:**
- Ubuntu 20.04 (Focal): Use `focal` no lugar de `jammy`
- Ubuntu 18.04 (Bionic): Use `bionic` no lugar de `jammy`

Verifique versões disponíveis em: https://github.com/wkhtmltopdf/packaging/releases

---

## 🍎 macOS

### Instalação via Homebrew

```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar wkhtmltopdf
brew install wkhtmltopdf

# Verificar instalação
wkhtmltopdf --version
```

### Instalação Manual

```bash
# Baixar o instalador
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox-0.12.6-1.macos-cocoa.pkg

# Instalar
sudo installer -pkg wkhtmltox-0.12.6-1.macos-cocoa.pkg -target /

# Verificar instalação
wkhtmltopdf --version
```

---

## ✅ Verificação da Instalação

### Via Terminal

```bash
# Verificar se está instalado
which wkhtmltopdf

# Ver versão
wkhtmltopdf --version

# Testar geração de PDF simples
echo "<h1>Hello World</h1>" | wkhtmltopdf - test.pdf
```

### Via API do Backend

1. Inicie o backend:
   ```bash
   cd /home/warley/dev/ion-nutri
   uv run uvicorn app.main:app --reload
   ```

2. Acesse a documentação: http://localhost:8000/docs

3. Teste o endpoint `/api/v1/reports/pdf` com um payload de exemplo

### Via Frontend

1. Gere um relatório através do frontend
2. Na página de visualização, clique em "⬇️ Download PDF"
3. Se wkhtmltopdf estiver instalado, o PDF será baixado
4. Se não estiver instalado, você verá uma mensagem de erro

---

## 🐛 Resolução de Problemas

### Erro: "wkhtmltopdf: command not found"

**Causa:** wkhtmltopdf não está instalado ou não está no PATH.

**Solução:**
1. Instale usando os comandos acima
2. Reinicie o terminal/IDE
3. Verifique com `which wkhtmltopdf`

### Erro: "wkhtmltopdf is not installed"

**No Backend:**
O serviço de PDF detecta automaticamente se wkhtmltopdf está disponível.

**Solução:**
1. Instale wkhtmltopdf usando os comandos acima
2. Reinicie o servidor do backend: `Ctrl+C` e depois `uv run uvicorn app.main:app --reload`

**No Frontend:**
Você verá uma mensagem de erro ao tentar baixar o PDF.

**Solução alternativa:**
Use o botão "🖨️ Print to PDF" que funciona sem wkhtmltopdf.

### Erro: "Permission denied" ao instalar

**Solução:**
Use `sudo` antes dos comandos de instalação:
```bash
sudo apt-get install wkhtmltopdf
```

### Erro: Dependências faltando no Ubuntu/Debian

**Sintoma:**
```
dpkg: dependency problems prevent configuration of wkhtmltox
```

**Solução:**
```bash
# Instalar dependências faltantes
sudo apt-get install -f

# Ou instalar manualmente
sudo apt-get install -y fontconfig libfreetype6 libjpeg-turbo8 libpng16-16 \
    libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base
```

### PDFs com fontes ruins

**Causa:** Fontes do sistema não estão instaladas.

**Solução (Ubuntu/Debian):**
```bash
# Instalar fontes básicas
sudo apt-get install -y fonts-liberation fonts-dejavu-core fonts-freefont-ttf

# Instalar fonte Roboto (usada nos relatórios)
sudo apt-get install -y fonts-roboto

# Atualizar cache de fontes
fc-cache -fv
```

**Solução (macOS):**
Instale as fontes Roboto através do Font Book ou baixe de https://fonts.google.com/specimen/Roboto

### Servidor não reinicia após instalar wkhtmltopdf

**Causa:** O backend não detecta mudanças no sistema.

**Solução:**
```bash
# Parar o servidor
Ctrl+C

# Reiniciar
uv run uvicorn app.main:app --reload
```

---

## 📚 Informações Adicionais

### Versões Recomendadas

- **wkhtmltopdf:** 0.12.6 ou superior
- **Com Qt patches:** Versão com patches do Qt para melhor renderização

### Links Úteis

- [Repositório Oficial](https://github.com/wkhtmltopdf/wkhtmltopdf)
- [Releases e Downloads](https://github.com/wkhtmltopdf/packaging/releases)
- [Documentação](https://wkhtmltopdf.org/docs.html)

### Alternativas se não puder instalar wkhtmltopdf

Se não puder instalar wkhtmltopdf no servidor:

1. **Usar "Print to PDF" do navegador:**
   - Funciona sem dependências do servidor
   - Usa os estilos `@media print` otimizados
   - Qualidade boa, mas não profissional

2. **Implementar geração de PDF no frontend:**
   - Usar bibliotecas JavaScript (react-pdf, jsPDF)
   - Funciona totalmente no cliente
   - Mais difícil de implementar e manter

---

## 🔄 Changelog

### 2025-12-16
- ✅ Documentação inicial criada
- ✅ Instruções para Ubuntu/Debian, macOS e Docker
- ✅ Seção de resolução de problemas

---

## 📝 Contribuindo

Se você encontrar problemas não documentados aqui, por favor:
1. Documente a solução
2. Adicione à seção de Resolução de Problemas
3. Commit e push para o repositório
