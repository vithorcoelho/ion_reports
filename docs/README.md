# Documentação ION NUTRI

Bem-vindo à documentação do sistema ION NUTRI - Nutrição de Precisão.

---

## 📚 Estrutura da Documentação

### Geração de Relatórios e PDFs

- **[PDF_GENERATION.md](./PDF_GENERATION.md)** - Guia completo de geração de PDFs
  - Métodos disponíveis (Backend e Frontend)
  - Como usar cada método
  - Comparação de qualidade
  - Resolução de problemas

- **[WKHTMLTOPDF_INSTALLATION.md](./WKHTMLTOPDF_INSTALLATION.md)** - Instalação do wkhtmltopdf
  - Ubuntu/Debian
  - macOS
  - Docker
  - Resolução de problemas

### Sprints e Planejamento

- **[sprints/](./sprints/)** - Documentação de sprints
  - Planejamento de features
  - Retrospectivas
  - Análises técnicas

---

## 🚀 Quick Start

### Gerar um Relatório com PDF

1. **Instalar wkhtmltopdf** (recomendado):
   ```bash
   # Ubuntu/Debian
   sudo apt-get install wkhtmltopdf

   # macOS
   brew install wkhtmltopdf
   ```

   Ver [guia completo](./WKHTMLTOPDF_INSTALLATION.md) para mais detalhes.

2. **Iniciar sistema:**
   ```bash
   # Backend
   cd /home/warley/dev/ion-nutri
   uv run uvicorn app.main:app --reload

   # Frontend (outro terminal)
   cd frontend
   npm run dev
   ```

3. **Usar a aplicação:**
   - Acesse: http://localhost:3000
   - Preencha formulário de relatório
   - Clique "Generate Report"
   - Na visualização, clique "⬇️ Download PDF"

---

## 📖 Documentação por Tópico

### Para Desenvolvedores

- Arquitetura do sistema: `sprints/7/TECHNICAL-OVERVIEW.md`
- APIs disponíveis: http://localhost:8000/docs (Swagger)
- Sessões de desenvolvimento: `.sessions/cursor/`

### Para Usuários

- Como gerar PDFs: [PDF_GENERATION.md](./PDF_GENERATION.md)
- Resolução de problemas: [WKHTMLTOPDF_INSTALLATION.md](./WKHTMLTOPDF_INSTALLATION.md#resolução-de-problemas)

---

## 🔧 Ferramentas e Tecnologias

### Backend
- **Python 3.12+** com `uv` para gerenciamento de pacotes
- **FastAPI** para API REST
- **MLflow** para tracking de experimentos
- **wkhtmltopdf** para geração de PDFs

### Frontend
- **React** com TypeScript
- **Vite** para build
- **TailwindCSS** para estilos
- **ReactMarkdown** para visualização de relatórios

---

## 📝 Changelog Recente

### 2025-12-16 - PDF Generation v2.0
- ✅ Implementado endpoint de PDF no backend
- ✅ Adicionado download automático de PDFs no frontend
- ✅ Criada documentação completa
- ✅ Estilos de impressão otimizados

Ver [PDF_GENERATION.md](./PDF_GENERATION.md#changelog) para detalhes completos.

---

## 🤝 Contribuindo

Para adicionar ou atualizar documentação:

1. Coloque documentação técnica em `docs/`
2. Coloque sessões de desenvolvimento em `.sessions/cursor/`
3. Use Markdown com formatação clara
4. Adicione exemplos práticos
5. Mantenha este README atualizado

---

## 📞 Suporte

- Issues técnicos: Verificar `.sessions/cursor/` para análises anteriores
- Problemas de PDF: Ver [resolução de problemas](./PDF_GENERATION.md#resolução-de-problemas)
- wkhtmltopdf: Ver [guia de instalação](./WKHTMLTOPDF_INSTALLATION.md)
