# MLflow Trace Report

**Trace ID:** `d9de4018c1154fe8af66ec56a3bb902c`
**State:** `TraceState.OK`
**Start:** `2025-09-05T16:04:22.524000`
**End:** `2025-09-05T16:04:22.524000`
**Token Usage:** input=33148, output=4318, total=37466

---
## Spans

### 1. Report AI
- **Type:** `UNKNOWN`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanOutputs": {
    "report_id": "vida_PP032_20250905_190423",
    "patient_id": "PP032",
    "anamnesis_id": "anam_PP032_20250905",
    "exam_id": "exam_PP032_20250814",
    "version": "1.0",
    "timestamp": "2025-09-05 19:04:23.061565",
    "report": "# RELATÓRIO FINAL - Vida Nova\n\nObserva-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\n\n---\n\n## Sugestão Alimentar\n- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\n- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\n- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\n- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\n- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\n- Frutas vermelhas (morango, framboesa): Fonte de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\n- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\n\n---\n\n## Suplementação Sugerida\n- **Acetil-L-Carnitina**\n  - Dosagem: 1g a 2g\n  - Frequência: Diário, antes do treino\n  - Propósito: Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\n  - Observação: Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\n  \n- **L-Carnitina**\n  - Dosagem: 500mg a 1g\n  - Frequência: Diário, se necessário\n  - Propósito: Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\n  - Observação: Avaliar a necessidade com base no nível de atividade física e fadiga.\n\n- **Cofatores: Vitamina C**\n  - Dosagem: 500mg\n  - Frequência: Diário\n  - Propósito: Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\n  - Observação: Monitorar a ingestão de antioxidantes na dieta.\n\n- **Cofatores: Vitamina B6 (P-5-P)**\n  - Dosagem: 10mg - 25mg\n  - Frequência: Diário\n  - Propósito: Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\n  - Observação: Importante para a adequada metabolização da isoleucina.\n\n- **Cofatores: Vitamina B3 (niacinamida ou NAD precursor)**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Suporte à produção de energia e otimização do metabolismo.\n  - Observação: Pode auxiliar na regulação do metabolismo energético.\n\n- **CoQ10 (ubiquinol)**\n  - Dosagem: 100mg a 300mg\n  - Frequência: Diário\n  - Propósito: Promover a saúde mitocondrial e aumentar a produção de ATP.\n  - Observação: Avaliar a resposta do paciente ao suporte mitocondrial.\n\n- **Ácido Alfa-Lipóico**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\n  - Observação: Considerar a relação com o excesso de leucina.\n\n- **Complexo de Vitaminas do grupo B (incluindo B6, B12)**\n  - Dosagem: Recomendações diárias específicas.\n  - Frequência: Diário\n  - Propósito: Apoio geral ao metabolismo energético e recuperação muscular.\n  - Observação: Incluir como um suporte contínuo através de uma dieta equilibrada.\n\n- **Glutamina**\n  - Dosagem: 5g\n  - Frequência: Diário, especialmente após exercícios\n  - Propósito: Apoio à recuperação muscular e manutenção da integridade intestinal.\n  - Observação: Considerar a saúde intestinal do paciente.\n\n- **Whey Protein (rico em BCAAs)**\n  - Dosagem: 20g a 30g\n  - Frequência: Após o treino\n  - Propósito: Promover a síntese proteica e a recuperação muscular.\n  - Observação: Importante para a melhoria dos níveis críticos de isoleucina.\n\n---\n\n## Dica de Treino\n- Recomendações:\n  - Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\n  - Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\n  - Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\n  - Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\n  - Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\n\n- Evitar:\n  - Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\n  - Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\n  - Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\n\n- Foco: Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
  },
  "mlflow.spanFunctionName": "generate_report",
  "mlflow.spanType": "UNKNOWN",
  "mlflow.spanInputs": {
    "exam_data": {
      "patient_id": "PP032",
      "exam_date": "2025-08-14 00:00:00+00:00",
      "metabolites": [
        {
          "name": "ACETIL-L-CARNITINA",
          "value": 0.314
        },
        {
          "name": "ADENOSINA",
          "value": 0.618
        },
        {
          "name": "L-CARNITINA",
          "value": 0.986
        },
        {
          "name": "GLUTAMINA",
          "value": 35.8
        },
        {
          "name": "ISOLEUCINA",
          "value": 1.0
        },
        {
          "name": "LACTATO",
          "value": 149.0
        },
        {
          "name": "LEUCINA",
          "value": 45.9
        },
        {
          "name": "PIRUVATO",
          "value": 0.001
        },
        {
          "name": "TMAO [Trimetilamina N-Óxido]",
          "value": 0.051
        },
        {
          "name": "VALINA",
          "value": 31.4
        },
        {
          "name": "PROPIONIL-L-CARNITINA",
          "value": 0.026
        }
      ]
    },
    "anamnesis": {
      "patient_id": "PP032",
      "objective": "Melhora da composição corporal e ganho de massa muscular",
      "personal_data": {
        "age": 32,
        "gender": "masculino",
        "weight": 83.0,
        "height": 1.76,
        "bmi": 26.82
      },
      "context_factors": {
        "medical_history": [
          "não informado"
        ],
        "intolerances": [],
        "physical_activity": {
          "frequency": "não informado",
          "type": "não informado",
          "intensity": "não informado"
        },
        "sleep": {
          "quality": "não informado",
          "hours": 7.0,
          "issues": [
            "não informado"
          ]
        },
        "alcohol_consumption": {
          "frequency": "não informado",
          "amount": "não informado"
        },
        "medications": [
          {
            "name": "Reposição hormonal de testosterona",
            "frequency": "semanal",
            "dosage": "0,4mg durateston"
          }
        ],
        "stress_level": "não informado"
      },
      "anamnesis_type": "vidanova",
      "diet_type": "Como de tudo, sem restrições específicas (onívora)",
      "energy_level": "Depende da semana, difícil dizer",
      "muscle_gain_goal": "Ganho de massa muscular",
      "nutritionist_plan": "Não, mas já segui antes",
      "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
    },
    "exam_type": null,
    "coordinator": "<app.services.report_coordinator.ReportCoordinator object at 0x7f6750c7a510>"
  }
}
```

---

### 2. Report Generator
- **Type:** `workflow`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `af0a2f87391a6dc5`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "generate_report",
  "mlflow.spanType": "workflow"
}
```
- **Inputs:**
```json
{
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "exam_type": "vidanova"
}
```
- **Outputs:**
```json
[
  "# RELATÓRIO FINAL - Vida Nova\n\nObserva-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\n\n---\n\n## Sugestão Alimentar\n- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\n- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\n- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\n- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\n- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\n- Frutas vermelhas (morango, framboesa): Fonte de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\n- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\n\n---\n\n## Suplementação Sugerida\n- **Acetil-L-Carnitina**\n  - Dosagem: 1g a 2g\n  - Frequência: Diário, antes do treino\n  - Propósito: Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\n  - Observação: Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\n  \n- **L-Carnitina**\n  - Dosagem: 500mg a 1g\n  - Frequência: Diário, se necessário\n  - Propósito: Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\n  - Observação: Avaliar a necessidade com base no nível de atividade física e fadiga.\n\n- **Cofatores: Vitamina C**\n  - Dosagem: 500mg\n  - Frequência: Diário\n  - Propósito: Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\n  - Observação: Monitorar a ingestão de antioxidantes na dieta.\n\n- **Cofatores: Vitamina B6 (P-5-P)**\n  - Dosagem: 10mg - 25mg\n  - Frequência: Diário\n  - Propósito: Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\n  - Observação: Importante para a adequada metabolização da isoleucina.\n\n- **Cofatores: Vitamina B3 (niacinamida ou NAD precursor)**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Suporte à produção de energia e otimização do metabolismo.\n  - Observação: Pode auxiliar na regulação do metabolismo energético.\n\n- **CoQ10 (ubiquinol)**\n  - Dosagem: 100mg a 300mg\n  - Frequência: Diário\n  - Propósito: Promover a saúde mitocondrial e aumentar a produção de ATP.\n  - Observação: Avaliar a resposta do paciente ao suporte mitocondrial.\n\n- **Ácido Alfa-Lipóico**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\n  - Observação: Considerar a relação com o excesso de leucina.\n\n- **Complexo de Vitaminas do grupo B (incluindo B6, B12)**\n  - Dosagem: Recomendações diárias específicas.\n  - Frequência: Diário\n  - Propósito: Apoio geral ao metabolismo energético e recuperação muscular.\n  - Observação: Incluir como um suporte contínuo através de uma dieta equilibrada.\n\n- **Glutamina**\n  - Dosagem: 5g\n  - Frequência: Diário, especialmente após exercícios\n  - Propósito: Apoio à recuperação muscular e manutenção da integridade intestinal.\n  - Observação: Considerar a saúde intestinal do paciente.\n\n- **Whey Protein (rico em BCAAs)**\n  - Dosagem: 20g a 30g\n  - Frequência: Após o treino\n  - Propósito: Promover a síntese proteica e a recuperação muscular.\n  - Observação: Importante para a melhoria dos níveis críticos de isoleucina.\n\n---\n\n## Dica de Treino\n- Recomendações:\n  - Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\n  - Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\n  - Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\n  - Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\n  - Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\n\n- Evitar:\n  - Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\n  - Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\n  - Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\n\n- Foco: Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.",
  {
    "report_id": "vida_PP032_20250905_190423",
    "patient_id": "PP032",
    "anamnesis_id": "anam_PP032_20250905",
    "exam_id": "exam_PP032_20250814",
    "version": "1.0",
    "timestamp": "2025-09-05 19:04:23.061565",
    "summary": {
      "content": "Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas."
    },
    "findings": {
      "items": [
        {
          "status": "alterado",
          "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
          "metabolite": "Acetil-L-Carnitina",
          "implications": [
            "Fadiga crônica e baixa energia",
            "Fraqueza muscular e redução da performance física",
            "Comprometimento da saúde mitocondrial",
            "Aumento do estresse oxidativo e inflamação sistêmica"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
          "metabolite": "Adenosina",
          "implications": [
            "Redução da resposta ao estresse e apatia",
            "Bradicardia e hipotensão potencial",
            "Maior predisposição a cefaleias e distúrbios do humor"
          ]
        },
        {
          "status": "alterado",
          "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
          "metabolite": "Isoleucina",
          "implications": [
            "Fraqueza muscular e perda de massa magra",
            "Dificuldade na regeneração tecidual",
            "Alterações na regulação da glicose"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
          "metabolite": "Leucina",
          "implications": [
            "Aumento do risco de resistência à insulina",
            "Desbalanço na produção de energia celular",
            "Alteração na função anabólica e catabólica do músculo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
          "metabolite": "Piruvato",
          "implications": [
            "Fadiga crônica e redução da resistência física",
            "Disfunção neurológica e dificuldade cognitiva",
            "Menor resistência ao estresse oxidativo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
          "metabolite": "Valina",
          "implications": [
            "Desbalanço no Equilíbrio de BCAAs",
            "Sobrecarga renal e hepática",
            "Alterações na regulação do metabolismo lipídico"
          ]
        }
      ],
      "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
    },
    "diet_suggestions": {
      "carnivoro_onivoro": [
        "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
        "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
        "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
        "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
        "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
        "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
        "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
      ],
      "vegetariano": [],
      "vegano": []
    },
    "supplements": [
      {
        "name": "Acetil-L-Carnitina",
        "dosage": "1g a 2g",
        "frequency": "Diário, antes do treino",
        "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
        "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
      },
      {
        "name": "L-Carnitina",
        "dosage": "500mg a 1g",
        "frequency": "Diário, se necessário",
        "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
        "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
      },
      {
        "name": "Cofatores: Vitamina C",
        "dosage": "500mg",
        "frequency": "Diário",
        "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
        "observation": "Monitorar a ingestão de antioxidantes na dieta."
      },
      {
        "name": "Cofatores: Vitamina B6 (P-5-P)",
        "dosage": "10mg - 25mg",
        "frequency": "Diário",
        "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
        "observation": "Importante para a adequada metabolização da isoleucina."
      },
      {
        "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
        "dosage": "300mg",
        "frequency": "Diário",
        "purpose": "Suporte à produção de energia e otimização do metabolismo.",
        "observation": "Pode auxiliar na regulação do metabolismo energético."
      },
      {
        "name": "CoQ10 (ubiquinol)",
        "dosage": "100mg a 300mg",
        "frequency": "Diário",
        "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
        "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
      },
      {
        "name": "Ácido Alfa-Lipóico",
        "dosage": "300mg",
        "frequency": "Diário",
        "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
        "observation": "Considerar a relação com o excesso de leucina."
      },
      {
        "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
        "dosage": "Recomendações diárias específicas.",
        "frequency": "Diário",
        "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
        "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
      },
      {
        "name": "Glutamina",
        "dosage": "5g",
        "frequency": "Diário, especialmente após exercícios",
        "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
        "observation": "Considerar a saúde intestinal do paciente."
      },
      {
        "name": "Whey Protein (rico em BCAAs)",
        "dosage": "20g a 30g",
        "frequency": "Após o treino",
        "purpose": "Promover a síntese proteica e a recuperação muscular.",
        "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
      }
    ],
    "training": {
      "recommendations": [
        "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
        "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
        "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
        "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
        "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
      ],
      "avoid": [
        "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
        "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
        "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
      ],
      "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
    }
  }
]
```

---

### 3. KG Query
- **Type:** `UNKNOWN`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `03b9785753e1b628`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "execute_unified_query",
  "mlflow.spanType": "UNKNOWN"
}
```
- **Inputs:**
```json
{
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  }
}
```
- **Outputs:**
```json
{
  "metabolite_info": [
    {
      "name": "ACETIL-L-CARNITINA",
      "value": 0.314,
      "status": "moderate_deficit",
      "description": "",
      "reference_range": {
        "min": 0.5,
        "max": 1.5
      },
      "category": ""
    },
    {
      "name": "ADENOSINA",
      "value": 0.618,
      "status": "moderate_excess",
      "description": "",
      "reference_range": {
        "min": 0.38,
        "max": 0.6
      },
      "category": ""
    },
    {
      "name": "ISOLEUCINA",
      "value": 1.0,
      "status": "moderate_deficit",
      "description": "",
      "reference_range": {
        "min": 2.0,
        "max": 10.0
      },
      "category": ""
    },
    {
      "name": "LEUCINA",
      "value": 45.9,
      "status": "severe_excess",
      "description": "",
      "reference_range": {
        "min": 4.0,
        "max": 15.0
      },
      "category": ""
    },
    {
      "name": "PIRUVATO",
      "value": 0.001,
      "status": "severe_deficit",
      "description": "",
      "reference_range": {
        "min": 10.0,
        "max": 120.0
      },
      "category": ""
    },
    {
      "name": "VALINA",
      "value": 31.4,
      "status": "severe_excess",
      "description": "",
      "reference_range": {
        "min": 6.0,
        "max": 15.0
      },
      "category": ""
    }
  ],
  "manifestations": [
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "status": "moderate_deficit",
      "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
      "type": "",
      "severity": "",
      "affected_system": "",
      "physiological_mechanism": ""
    },
    {
      "metabolite": "ADENOSINA",
      "status": "moderate_excess",
      "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
      "type": "",
      "severity": "",
      "affected_system": "",
      "physiological_mechanism": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "status": "moderate_deficit",
      "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
      "type": "",
      "severity": "",
      "affected_system": "",
      "physiological_mechanism": ""
    },
    {
      "metabolite": "LEUCINA",
      "status": "severe_excess",
      "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
      "type": "",
      "severity": "",
      "affected_system": "",
      "physiological_mechanism": ""
    },
    {
      "metabolite": "PIRUVATO",
      "status": "severe_deficit",
      "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
      "type": "",
      "severity": "",
      "affected_system": "",
      "physiological_mechanism": ""
    },
    {
      "metabolite": "VALINA",
      "status": "severe_excess",
      "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
      "type": "",
      "severity": "",
      "affected_system": "",
      "physiological_mechanism": ""
    }
  ],
  "recommended_interventions": [
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "type": "LowLevel",
      "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
      "priority": "medium",
      "recommended_duration": "",
      "expected_results": "",
      "is_contraindicated": false,
      "contraindication_reason": "",
      "medication_interaction": ""
    },
    {
      "metabolite": "ADENOSINA",
      "type": "HighLevel",
      "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
      "priority": "medium",
      "recommended_duration": "",
      "expected_results": "",
      "is_contraindicated": false,
      "contraindication_reason": "",
      "medication_interaction": ""
    }
  ],
  "foods": [
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
      "food_group": "",
      "main_nutrients": [],
      "recommended_portion": "",
      "consumption_frequency": ""
    },
    {
      "metabolite": "ADENOSINA",
      "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
      "food_group": "",
      "main_nutrients": [],
      "recommended_portion": "",
      "consumption_frequency": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
      "food_group": "",
      "main_nutrients": [],
      "recommended_portion": "",
      "consumption_frequency": ""
    },
    {
      "metabolite": "LEUCINA",
      "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
      "food_group": "",
      "main_nutrients": [],
      "recommended_portion": "",
      "consumption_frequency": ""
    },
    {
      "metabolite": "PIRUVATO",
      "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
      "food_group": "",
      "main_nutrients": [],
      "recommended_portion": "",
      "consumption_frequency": ""
    },
    {
      "metabolite": "VALINA",
      "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
      "food_group": "",
      "main_nutrients": [],
      "recommended_portion": "",
      "consumption_frequency": ""
    }
  ],
  "supplements": [
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
      "active_composition": "",
      "dosage": null,
      "administration_form": ""
    },
    {
      "metabolite": "ADENOSINA",
      "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
      "active_composition": "",
      "dosage": null,
      "administration_form": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
      "active_composition": "",
      "dosage": null,
      "administration_form": ""
    },
    {
      "metabolite": "LEUCINA",
      "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
      "active_composition": "",
      "dosage": null,
      "administration_form": ""
    },
    {
      "metabolite": "PIRUVATO",
      "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
      "active_composition": "",
      "dosage": null,
      "administration_form": ""
    },
    {
      "metabolite": "VALINA",
      "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
      "active_composition": "",
      "dosage": null,
      "administration_form": ""
    }
  ],
  "pathway_impacts": [
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
      "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
      "biological_function": "",
      "clinical_importance": ""
    },
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "name": "Saúde Intestinal",
      "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
      "biological_function": "",
      "clinical_importance": ""
    },
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "name": "Ciclo da Metionina - Acetilação (via carbono I)",
      "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
      "biological_function": "",
      "clinical_importance": ""
    },
    {
      "metabolite": "ADENOSINA",
      "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
      "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
      "biological_function": "",
      "clinical_importance": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "name": "Sinalização da Insulina",
      "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
      "biological_function": "",
      "clinical_importance": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "name": "Aminoácidos Essenciais",
      "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
      "biological_function": "",
      "clinical_importance": ""
    },
    {
      "metabolite": "PIRUVATO",
      "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
      "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
      "biological_function": "",
      "clinical_importance": ""
    },
    {
      "metabolite": "PIRUVATO",
      "name": "Glicólise",
      "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
      "biological_function": "",
      "clinical_importance": ""
    }
  ],
  "scientific_evidence": [
    {
      "metabolite": "ACETIL-L-CARNITINA",
      "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ADENOSINA",
      "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "ISOLEUCINA",
      "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "LEUCINA",
      "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "LEUCINA",
      "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "PIRUVATO",
      "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "PIRUVATO",
      "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "PIRUVATO",
      "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "PIRUVATO",
      "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "PIRUVATO",
      "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "PIRUVATO",
      "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "VALINA",
      "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "VALINA",
      "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "VALINA",
      "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    },
    {
      "metabolite": "VALINA",
      "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
      "authors": "",
      "year": "",
      "doi": "",
      "study_type": "",
      "evidence_level": ""
    }
  ],
  "contraindications": [],
  "error": null
}
```

---

### 4. get_vidanova_markdown_report
- **Type:** `func`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `03b9785753e1b628`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "get_markdown_report",
  "mlflow.spanType": "func"
}
```
- **Inputs:**
```json
{
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  }
}
```
- **Outputs:**
```json
[
  "# RELATÓRIO FINAL - Vida Nova\n\nObserva-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\n\n---\n\n## Sugestão Alimentar\n- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\n- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\n- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\n- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\n- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\n- Frutas vermelhas (morango, framboesa): Fonte de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\n- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\n\n---\n\n## Suplementação Sugerida\n- **Acetil-L-Carnitina**\n  - Dosagem: 1g a 2g\n  - Frequência: Diário, antes do treino\n  - Propósito: Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\n  - Observação: Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\n  \n- **L-Carnitina**\n  - Dosagem: 500mg a 1g\n  - Frequência: Diário, se necessário\n  - Propósito: Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\n  - Observação: Avaliar a necessidade com base no nível de atividade física e fadiga.\n\n- **Cofatores: Vitamina C**\n  - Dosagem: 500mg\n  - Frequência: Diário\n  - Propósito: Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\n  - Observação: Monitorar a ingestão de antioxidantes na dieta.\n\n- **Cofatores: Vitamina B6 (P-5-P)**\n  - Dosagem: 10mg - 25mg\n  - Frequência: Diário\n  - Propósito: Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\n  - Observação: Importante para a adequada metabolização da isoleucina.\n\n- **Cofatores: Vitamina B3 (niacinamida ou NAD precursor)**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Suporte à produção de energia e otimização do metabolismo.\n  - Observação: Pode auxiliar na regulação do metabolismo energético.\n\n- **CoQ10 (ubiquinol)**\n  - Dosagem: 100mg a 300mg\n  - Frequência: Diário\n  - Propósito: Promover a saúde mitocondrial e aumentar a produção de ATP.\n  - Observação: Avaliar a resposta do paciente ao suporte mitocondrial.\n\n- **Ácido Alfa-Lipóico**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\n  - Observação: Considerar a relação com o excesso de leucina.\n\n- **Complexo de Vitaminas do grupo B (incluindo B6, B12)**\n  - Dosagem: Recomendações diárias específicas.\n  - Frequência: Diário\n  - Propósito: Apoio geral ao metabolismo energético e recuperação muscular.\n  - Observação: Incluir como um suporte contínuo através de uma dieta equilibrada.\n\n- **Glutamina**\n  - Dosagem: 5g\n  - Frequência: Diário, especialmente após exercícios\n  - Propósito: Apoio à recuperação muscular e manutenção da integridade intestinal.\n  - Observação: Considerar a saúde intestinal do paciente.\n\n- **Whey Protein (rico em BCAAs)**\n  - Dosagem: 20g a 30g\n  - Frequência: Após o treino\n  - Propósito: Promover a síntese proteica e a recuperação muscular.\n  - Observação: Importante para a melhoria dos níveis críticos de isoleucina.\n\n---\n\n## Dica de Treino\n- Recomendações:\n  - Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\n  - Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\n  - Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\n  - Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\n  - Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\n\n- Evitar:\n  - Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\n  - Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\n  - Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\n\n- Foco: Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.",
  {
    "report_id": "vida_PP032_20250905_190423",
    "patient_id": "PP032",
    "anamnesis_id": "anam_PP032_20250905",
    "exam_id": "exam_PP032_20250814",
    "version": "1.0",
    "timestamp": "2025-09-05 19:04:23.061565",
    "summary": {
      "content": "Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas."
    },
    "findings": {
      "items": [
        {
          "status": "alterado",
          "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
          "metabolite": "Acetil-L-Carnitina",
          "implications": [
            "Fadiga crônica e baixa energia",
            "Fraqueza muscular e redução da performance física",
            "Comprometimento da saúde mitocondrial",
            "Aumento do estresse oxidativo e inflamação sistêmica"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
          "metabolite": "Adenosina",
          "implications": [
            "Redução da resposta ao estresse e apatia",
            "Bradicardia e hipotensão potencial",
            "Maior predisposição a cefaleias e distúrbios do humor"
          ]
        },
        {
          "status": "alterado",
          "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
          "metabolite": "Isoleucina",
          "implications": [
            "Fraqueza muscular e perda de massa magra",
            "Dificuldade na regeneração tecidual",
            "Alterações na regulação da glicose"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
          "metabolite": "Leucina",
          "implications": [
            "Aumento do risco de resistência à insulina",
            "Desbalanço na produção de energia celular",
            "Alteração na função anabólica e catabólica do músculo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
          "metabolite": "Piruvato",
          "implications": [
            "Fadiga crônica e redução da resistência física",
            "Disfunção neurológica e dificuldade cognitiva",
            "Menor resistência ao estresse oxidativo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
          "metabolite": "Valina",
          "implications": [
            "Desbalanço no Equilíbrio de BCAAs",
            "Sobrecarga renal e hepática",
            "Alterações na regulação do metabolismo lipídico"
          ]
        }
      ],
      "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
    },
    "diet_suggestions": {
      "carnivoro_onivoro": [
        "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
        "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
        "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
        "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
        "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
        "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
        "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
      ],
      "vegetariano": [],
      "vegano": []
    },
    "supplements": [
      {
        "name": "Acetil-L-Carnitina",
        "dosage": "1g a 2g",
        "frequency": "Diário, antes do treino",
        "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
        "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
      },
      {
        "name": "L-Carnitina",
        "dosage": "500mg a 1g",
        "frequency": "Diário, se necessário",
        "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
        "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
      },
      {
        "name": "Cofatores: Vitamina C",
        "dosage": "500mg",
        "frequency": "Diário",
        "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
        "observation": "Monitorar a ingestão de antioxidantes na dieta."
      },
      {
        "name": "Cofatores: Vitamina B6 (P-5-P)",
        "dosage": "10mg - 25mg",
        "frequency": "Diário",
        "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
        "observation": "Importante para a adequada metabolização da isoleucina."
      },
      {
        "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
        "dosage": "300mg",
        "frequency": "Diário",
        "purpose": "Suporte à produção de energia e otimização do metabolismo.",
        "observation": "Pode auxiliar na regulação do metabolismo energético."
      },
      {
        "name": "CoQ10 (ubiquinol)",
        "dosage": "100mg a 300mg",
        "frequency": "Diário",
        "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
        "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
      },
      {
        "name": "Ácido Alfa-Lipóico",
        "dosage": "300mg",
        "frequency": "Diário",
        "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
        "observation": "Considerar a relação com o excesso de leucina."
      },
      {
        "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
        "dosage": "Recomendações diárias específicas.",
        "frequency": "Diário",
        "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
        "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
      },
      {
        "name": "Glutamina",
        "dosage": "5g",
        "frequency": "Diário, especialmente após exercícios",
        "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
        "observation": "Considerar a saúde intestinal do paciente."
      },
      {
        "name": "Whey Protein (rico em BCAAs)",
        "dosage": "20g a 30g",
        "frequency": "Após o treino",
        "purpose": "Promover a síntese proteica e a recuperação muscular.",
        "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
      }
    ],
    "training": {
      "recommendations": [
        "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
        "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
        "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
        "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
        "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
      ],
      "avoid": [
        "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
        "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
        "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
      ],
      "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
    }
  }
]
```

---

### 5. build_vidanova_report
- **Type:** `func`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `d280763c8298c2da`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "build_report",
  "mlflow.spanType": "func"
}
```
- **Inputs:**
```json
{
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  }
}
```
- **Outputs:**
```json
{
  "report_id": "vida_PP032_20250905_190423",
  "patient_id": "PP032",
  "anamnesis_id": "anam_PP032_20250905",
  "exam_id": "exam_PP032_20250814",
  "version": "1.0",
  "timestamp": "2025-09-05 19:04:23.061565",
  "summary": {
    "content": "Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas."
  },
  "findings": {
    "items": [
      {
        "status": "alterado",
        "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
        "metabolite": "Acetil-L-Carnitina",
        "implications": [
          "Fadiga crônica e baixa energia",
          "Fraqueza muscular e redução da performance física",
          "Comprometimento da saúde mitocondrial",
          "Aumento do estresse oxidativo e inflamação sistêmica"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
        "metabolite": "Adenosina",
        "implications": [
          "Redução da resposta ao estresse e apatia",
          "Bradicardia e hipotensão potencial",
          "Maior predisposição a cefaleias e distúrbios do humor"
        ]
      },
      {
        "status": "alterado",
        "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
        "metabolite": "Isoleucina",
        "implications": [
          "Fraqueza muscular e perda de massa magra",
          "Dificuldade na regeneração tecidual",
          "Alterações na regulação da glicose"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
        "metabolite": "Leucina",
        "implications": [
          "Aumento do risco de resistência à insulina",
          "Desbalanço na produção de energia celular",
          "Alteração na função anabólica e catabólica do músculo"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
        "metabolite": "Piruvato",
        "implications": [
          "Fadiga crônica e redução da resistência física",
          "Disfunção neurológica e dificuldade cognitiva",
          "Menor resistência ao estresse oxidativo"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
        "metabolite": "Valina",
        "implications": [
          "Desbalanço no Equilíbrio de BCAAs",
          "Sobrecarga renal e hepática",
          "Alterações na regulação do metabolismo lipídico"
        ]
      }
    ],
    "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
  },
  "diet_suggestions": {
    "carnivoro_onivoro": [
      "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
      "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
      "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
      "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
      "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
      "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
      "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
    ],
    "vegetariano": [],
    "vegano": []
  },
  "supplements": [
    {
      "name": "Acetil-L-Carnitina",
      "dosage": "1g a 2g",
      "frequency": "Diário, antes do treino",
      "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
      "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
    },
    {
      "name": "L-Carnitina",
      "dosage": "500mg a 1g",
      "frequency": "Diário, se necessário",
      "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
      "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
    },
    {
      "name": "Cofatores: Vitamina C",
      "dosage": "500mg",
      "frequency": "Diário",
      "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
      "observation": "Monitorar a ingestão de antioxidantes na dieta."
    },
    {
      "name": "Cofatores: Vitamina B6 (P-5-P)",
      "dosage": "10mg - 25mg",
      "frequency": "Diário",
      "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
      "observation": "Importante para a adequada metabolização da isoleucina."
    },
    {
      "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
      "dosage": "300mg",
      "frequency": "Diário",
      "purpose": "Suporte à produção de energia e otimização do metabolismo.",
      "observation": "Pode auxiliar na regulação do metabolismo energético."
    },
    {
      "name": "CoQ10 (ubiquinol)",
      "dosage": "100mg a 300mg",
      "frequency": "Diário",
      "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
      "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
    },
    {
      "name": "Ácido Alfa-Lipóico",
      "dosage": "300mg",
      "frequency": "Diário",
      "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
      "observation": "Considerar a relação com o excesso de leucina."
    },
    {
      "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
      "dosage": "Recomendações diárias específicas.",
      "frequency": "Diário",
      "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
      "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
    },
    {
      "name": "Glutamina",
      "dosage": "5g",
      "frequency": "Diário, especialmente após exercícios",
      "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
      "observation": "Considerar a saúde intestinal do paciente."
    },
    {
      "name": "Whey Protein (rico em BCAAs)",
      "dosage": "20g a 30g",
      "frequency": "Após o treino",
      "purpose": "Promover a síntese proteica e a recuperação muscular.",
      "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
    }
  ],
  "training": {
    "recommendations": [
      "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
      "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
      "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
      "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
      "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
    ],
    "avoid": [
      "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
      "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
      "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
    ],
    "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
  }
}
```

---

### 6. generate_section_contents
- **Type:** `func`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `fdcb43014f21d775`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "_generate_section_contents",
  "mlflow.spanType": "func"
}
```
- **Inputs:**
```json
{
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  }
}
```
- **Outputs:**
```json
{
  "findings": {
    "items": [
      {
        "status": "alterado",
        "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
        "metabolite": "Acetil-L-Carnitina",
        "implications": [
          "Fadiga crônica e baixa energia",
          "Fraqueza muscular e redução da performance física",
          "Comprometimento da saúde mitocondrial",
          "Aumento do estresse oxidativo e inflamação sistêmica"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
        "metabolite": "Adenosina",
        "implications": [
          "Redução da resposta ao estresse e apatia",
          "Bradicardia e hipotensão potencial",
          "Maior predisposição a cefaleias e distúrbios do humor"
        ]
      },
      {
        "status": "alterado",
        "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
        "metabolite": "Isoleucina",
        "implications": [
          "Fraqueza muscular e perda de massa magra",
          "Dificuldade na regeneração tecidual",
          "Alterações na regulação da glicose"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
        "metabolite": "Leucina",
        "implications": [
          "Aumento do risco de resistência à insulina",
          "Desbalanço na produção de energia celular",
          "Alteração na função anabólica e catabólica do músculo"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
        "metabolite": "Piruvato",
        "implications": [
          "Fadiga crônica e redução da resistência física",
          "Disfunção neurológica e dificuldade cognitiva",
          "Menor resistência ao estresse oxidativo"
        ]
      },
      {
        "status": "alterado",
        "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
        "metabolite": "Valina",
        "implications": [
          "Desbalanço no Equilíbrio de BCAAs",
          "Sobrecarga renal e hepática",
          "Alterações na regulação do metabolismo lipídico"
        ]
      }
    ],
    "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
  },
  "diet_suggestions": {
    "carnivoro_onivoro": [
      "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
      "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
      "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
      "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
      "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
      "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
      "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
    ],
    "vegetariano": [],
    "vegano": []
  },
  "supplements": {
    "items": [
      {
        "name": "Acetil-L-Carnitina",
        "dosage": "1g a 2g",
        "frequency": "Diário, antes do treino",
        "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
        "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
      },
      {
        "name": "L-Carnitina",
        "dosage": "500mg a 1g",
        "frequency": "Diário, se necessário",
        "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
        "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
      },
      {
        "name": "Cofatores: Vitamina C",
        "dosage": "500mg",
        "frequency": "Diário",
        "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
        "observation": "Monitorar a ingestão de antioxidantes na dieta."
      },
      {
        "name": "Cofatores: Vitamina B6 (P-5-P)",
        "dosage": "10mg - 25mg",
        "frequency": "Diário",
        "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
        "observation": "Importante para a adequada metabolização da isoleucina."
      },
      {
        "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
        "dosage": "300mg",
        "frequency": "Diário",
        "purpose": "Suporte à produção de energia e otimização do metabolismo.",
        "observation": "Pode auxiliar na regulação do metabolismo energético."
      },
      {
        "name": "CoQ10 (ubiquinol)",
        "dosage": "100mg a 300mg",
        "frequency": "Diário",
        "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
        "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
      },
      {
        "name": "Ácido Alfa-Lipóico",
        "dosage": "300mg",
        "frequency": "Diário",
        "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
        "observation": "Considerar a relação com o excesso de leucina."
      },
      {
        "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
        "dosage": "Recomendações diárias específicas.",
        "frequency": "Diário",
        "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
        "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
      },
      {
        "name": "Glutamina",
        "dosage": "5g",
        "frequency": "Diário, especialmente após exercícios",
        "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
        "observation": "Considerar a saúde intestinal do paciente."
      },
      {
        "name": "Whey Protein (rico em BCAAs)",
        "dosage": "20g a 30g",
        "frequency": "Após o treino",
        "purpose": "Promover a síntese proteica e a recuperação muscular.",
        "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
      }
    ]
  },
  "training": {
    "recommendations": [
      "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
      "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
      "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
      "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
      "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
    ],
    "avoid": [
      "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
      "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
      "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
    ],
    "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
  },
  "summary": {
    "content": "Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas."
  }
}
```

---

### 7. generate_vidanova_section_1
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `23e3926405b6f906`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "_generate_section",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "section_name": "findings",
  "config": {
    "prompt_func": "<bound method VidaNovaPrompts.get_findings_prompt of <app.plugins.prompts.vidanova_prompts.VidaNovaPrompts object at 0x7f6750c7a900>>",
    "schema": "<class 'app.domain.report.FindingsSection'>",
    "requires_context": false
  },
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  },
  "section_contents": {}
}
```

---

### 8. call_llm_api_1
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `aab9a57b5c4dce6b`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "call_llm_api",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "user_prompt": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\nAnalise os dados metabólicos e descreva os principais achados clínicos relevantes para performance e fitness.",
  "schema": "<class 'app.domain.report.FindingsSection'>",
  "system_prompt": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness.",
  "temperature": 1.0,
  "max_tokens": 4058,
  "kwargs": {}
}
```
- **Outputs:**
```json
{
  "items": [
    {
      "status": "alterado",
      "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
      "metabolite": "Acetil-L-Carnitina",
      "implications": [
        "Fadiga crônica e baixa energia",
        "Fraqueza muscular e redução da performance física",
        "Comprometimento da saúde mitocondrial",
        "Aumento do estresse oxidativo e inflamação sistêmica"
      ]
    },
    {
      "status": "alterado",
      "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
      "metabolite": "Adenosina",
      "implications": [
        "Redução da resposta ao estresse e apatia",
        "Bradicardia e hipotensão potencial",
        "Maior predisposição a cefaleias e distúrbios do humor"
      ]
    },
    {
      "status": "alterado",
      "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
      "metabolite": "Isoleucina",
      "implications": [
        "Fraqueza muscular e perda de massa magra",
        "Dificuldade na regeneração tecidual",
        "Alterações na regulação da glicose"
      ]
    },
    {
      "status": "alterado",
      "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
      "metabolite": "Leucina",
      "implications": [
        "Aumento do risco de resistência à insulina",
        "Desbalanço na produção de energia celular",
        "Alteração na função anabólica e catabólica do músculo"
      ]
    },
    {
      "status": "alterado",
      "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
      "metabolite": "Piruvato",
      "implications": [
        "Fadiga crônica e redução da resistência física",
        "Disfunção neurológica e dificuldade cognitiva",
        "Menor resistência ao estresse oxidativo"
      ]
    },
    {
      "status": "alterado",
      "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
      "metabolite": "Valina",
      "implications": [
        "Desbalanço no Equilíbrio de BCAAs",
        "Sobrecarga renal e hepática",
        "Alterações na regulação do metabolismo lipídico"
      ]
    }
  ],
  "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
}
```

---

### 9. AsyncCompletions_1
- **Type:** `CHAT_MODEL`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `152249b9c9226205`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "model": "openai/gpt-4o-mini",
  "temperature": 1.0,
  "response_format": "<class 'app.domain.report.FindingsSection'>",
  "mlflow.chat.messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\nAnalise os dados metabólicos e descreva os principais achados clínicos relevantes para performance e fitness."
    },
    {
      "content": "{\"items\":[{\"status\":\"alterado\",\"description\":\"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\"metabolite\":\"Acetil-L-Carnitina\",\"implications\":[\"Fadiga crônica e baixa energia\",\"Fraqueza muscular e redução da performance física\",\"Comprometimento da saúde mitocondrial\",\"Aumento do estresse oxidativo e inflamação sistêmica\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\"metabolite\":\"Adenosina\",\"implications\":[\"Redução da resposta ao estresse e apatia\",\"Bradicardia e hipotensão potencial\",\"Maior predisposição a cefaleias e distúrbios do humor\"]},{\"status\":\"alterado\",\"description\":\"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\"metabolite\":\"Isoleucina\",\"implications\":[\"Fraqueza muscular e perda de massa magra\",\"Dificuldade na regeneração tecidual\",\"Alterações na regulação da glicose\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\"metabolite\":\"Leucina\",\"implications\":[\"Aumento do risco de resistência à insulina\",\"Desbalanço na produção de energia celular\",\"Alteração na função anabólica e catabólica do músculo\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\"metabolite\":\"Piruvato\",\"implications\":[\"Fadiga crônica e redução da resistência física\",\"Disfunção neurológica e dificuldade cognitiva\",\"Menor resistência ao estresse oxidativo\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\"metabolite\":\"Valina\",\"implications\":[\"Desbalanço no Equilíbrio de BCAAs\",\"Sobrecarga renal e hepática\",\"Alterações na regulação do metabolismo lipídico\"]}],\"conclusion\":\"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"}",
      "refusal": null,
      "role": "assistant",
      "tool_calls": null,
      "parsed": {
        "items": [
          {
            "status": "alterado",
            "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
            "metabolite": "Acetil-L-Carnitina",
            "implications": [
              "Fadiga crônica e baixa energia",
              "Fraqueza muscular e redução da performance física",
              "Comprometimento da saúde mitocondrial",
              "Aumento do estresse oxidativo e inflamação sistêmica"
            ]
          },
          {
            "status": "alterado",
            "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
            "metabolite": "Adenosina",
            "implications": [
              "Redução da resposta ao estresse e apatia",
              "Bradicardia e hipotensão potencial",
              "Maior predisposição a cefaleias e distúrbios do humor"
            ]
          },
          {
            "status": "alterado",
            "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
            "metabolite": "Isoleucina",
            "implications": [
              "Fraqueza muscular e perda de massa magra",
              "Dificuldade na regeneração tecidual",
              "Alterações na regulação da glicose"
            ]
          },
          {
            "status": "alterado",
            "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
            "metabolite": "Leucina",
            "implications": [
              "Aumento do risco de resistência à insulina",
              "Desbalanço na produção de energia celular",
              "Alteração na função anabólica e catabólica do músculo"
            ]
          },
          {
            "status": "alterado",
            "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
            "metabolite": "Piruvato",
            "implications": [
              "Fadiga crônica e redução da resistência física",
              "Disfunção neurológica e dificuldade cognitiva",
              "Menor resistência ao estresse oxidativo"
            ]
          },
          {
            "status": "alterado",
            "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
            "metabolite": "Valina",
            "implications": [
              "Desbalanço no Equilíbrio de BCAAs",
              "Sobrecarga renal e hepática",
              "Alterações na regulação do metabolismo lipídico"
            ]
          }
        ],
        "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
      },
      "reasoning": null
    }
  ],
  "max_tokens": 4058,
  "mlflow.spanType": "CHAT_MODEL",
  "mlflow.chat.tokenUsage": {
    "input_tokens": 4754,
    "output_tokens": 578,
    "total_tokens": 5332
  }
}
```
- **Inputs:**
```json
{
  "model": "openai/gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\nAnalise os dados metabólicos e descreva os principais achados clínicos relevantes para performance e fitness."
    }
  ],
  "temperature": 1.0,
  "max_tokens": 4058,
  "response_format": "<class 'app.domain.report.FindingsSection'>"
}
```
- **Outputs:**
```json
{
  "id": "gen-1757099062-HBiplFBJkFwhQaY37LM5",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "{\"items\":[{\"status\":\"alterado\",\"description\":\"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\"metabolite\":\"Acetil-L-Carnitina\",\"implications\":[\"Fadiga crônica e baixa energia\",\"Fraqueza muscular e redução da performance física\",\"Comprometimento da saúde mitocondrial\",\"Aumento do estresse oxidativo e inflamação sistêmica\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\"metabolite\":\"Adenosina\",\"implications\":[\"Redução da resposta ao estresse e apatia\",\"Bradicardia e hipotensão potencial\",\"Maior predisposição a cefaleias e distúrbios do humor\"]},{\"status\":\"alterado\",\"description\":\"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\"metabolite\":\"Isoleucina\",\"implications\":[\"Fraqueza muscular e perda de massa magra\",\"Dificuldade na regeneração tecidual\",\"Alterações na regulação da glicose\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\"metabolite\":\"Leucina\",\"implications\":[\"Aumento do risco de resistência à insulina\",\"Desbalanço na produção de energia celular\",\"Alteração na função anabólica e catabólica do músculo\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\"metabolite\":\"Piruvato\",\"implications\":[\"Fadiga crônica e redução da resistência física\",\"Disfunção neurológica e dificuldade cognitiva\",\"Menor resistência ao estresse oxidativo\"]},{\"status\":\"alterado\",\"description\":\"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\"metabolite\":\"Valina\",\"implications\":[\"Desbalanço no Equilíbrio de BCAAs\",\"Sobrecarga renal e hepática\",\"Alterações na regulação do metabolismo lipídico\"]}],\"conclusion\":\"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"}",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "parsed": {
          "items": [
            {
              "status": "alterado",
              "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
              "metabolite": "Acetil-L-Carnitina",
              "implications": [
                "Fadiga crônica e baixa energia",
                "Fraqueza muscular e redução da performance física",
                "Comprometimento da saúde mitocondrial",
                "Aumento do estresse oxidativo e inflamação sistêmica"
              ]
            },
            {
              "status": "alterado",
              "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
              "metabolite": "Adenosina",
              "implications": [
                "Redução da resposta ao estresse e apatia",
                "Bradicardia e hipotensão potencial",
                "Maior predisposição a cefaleias e distúrbios do humor"
              ]
            },
            {
              "status": "alterado",
              "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
              "metabolite": "Isoleucina",
              "implications": [
                "Fraqueza muscular e perda de massa magra",
                "Dificuldade na regeneração tecidual",
                "Alterações na regulação da glicose"
              ]
            },
            {
              "status": "alterado",
              "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
              "metabolite": "Leucina",
              "implications": [
                "Aumento do risco de resistência à insulina",
                "Desbalanço na produção de energia celular",
                "Alteração na função anabólica e catabólica do músculo"
              ]
            },
            {
              "status": "alterado",
              "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
              "metabolite": "Piruvato",
              "implications": [
                "Fadiga crônica e redução da resistência física",
                "Disfunção neurológica e dificuldade cognitiva",
                "Menor resistência ao estresse oxidativo"
              ]
            },
            {
              "status": "alterado",
              "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
              "metabolite": "Valina",
              "implications": [
                "Desbalanço no Equilíbrio de BCAAs",
                "Sobrecarga renal e hepática",
                "Alterações na regulação do metabolismo lipídico"
              ]
            }
          ],
          "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
        },
        "reasoning": null
      },
      "native_finish_reason": "stop"
    }
  ],
  "created": 1757099062,
  "model": "openai/gpt-4o-mini",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_8bda4d3a2c",
  "usage": {
    "completion_tokens": 578,
    "prompt_tokens": 4754,
    "total_tokens": 5332,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "provider": "OpenAI"
}
```

---

### 10. generate_vidanova_section_2
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `23e3926405b6f906`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "_generate_section",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "section_name": "diet_suggestions",
  "config": {
    "prompt_func": "<bound method VidaNovaPrompts.get_diet_suggestions_prompt of <app.plugins.prompts.vidanova_prompts.VidaNovaPrompts object at 0x7f6750c7a900>>",
    "schema": "<class 'app.domain.report.VidaNovaDietSuggestions'>",
    "requires_context": true
  },
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  },
  "section_contents": {
    "findings": {
      "items": [
        {
          "status": "alterado",
          "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
          "metabolite": "Acetil-L-Carnitina",
          "implications": [
            "Fadiga crônica e baixa energia",
            "Fraqueza muscular e redução da performance física",
            "Comprometimento da saúde mitocondrial",
            "Aumento do estresse oxidativo e inflamação sistêmica"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
          "metabolite": "Adenosina",
          "implications": [
            "Redução da resposta ao estresse e apatia",
            "Bradicardia e hipotensão potencial",
            "Maior predisposição a cefaleias e distúrbios do humor"
          ]
        },
        {
          "status": "alterado",
          "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
          "metabolite": "Isoleucina",
          "implications": [
            "Fraqueza muscular e perda de massa magra",
            "Dificuldade na regeneração tecidual",
            "Alterações na regulação da glicose"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
          "metabolite": "Leucina",
          "implications": [
            "Aumento do risco de resistência à insulina",
            "Desbalanço na produção de energia celular",
            "Alteração na função anabólica e catabólica do músculo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
          "metabolite": "Piruvato",
          "implications": [
            "Fadiga crônica e redução da resistência física",
            "Disfunção neurológica e dificuldade cognitiva",
            "Menor resistência ao estresse oxidativo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
          "metabolite": "Valina",
          "implications": [
            "Desbalanço no Equilíbrio de BCAAs",
            "Sobrecarga renal e hepática",
            "Alterações na regulação do metabolismo lipídico"
          ]
        }
      ],
      "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
    }
  }
}
```

---

### 11. call_llm_api_2
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `0af46dd8348f3135`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "call_llm_api",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "user_prompt": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  }\n}\n\nCrie sugestões alimentares baseadas EXCLUSIVAMENTE no tipo de dieta informado na anamnese do paciente.\n\n        PRIORIZE os alimentos recomendados pelo knowledge graph\n\n        Se o paciente indicou 'Como de tudo, sem restrições específicas (onívora)', foque apenas em sugestões para dieta onívora/carnívora. Se indicou outro tipo específico, foque apenas nesse tipo. Ignore completamente os outros tipos de dieta não mencionados na anamnese.\n\n        Para cada sugestão alimentar, forneça também uma justificativa clara, relacionando-a aos achados metabólicos ou deficiências (ex.: “Alimento X devido à alteração Y”), mas sem rigidez — múltiplas relações podem existir.\n\n        Formate cada recomendação como um item de lista com '-' para melhor organização.",
  "schema": "<class 'app.domain.report.VidaNovaDietSuggestions'>",
  "system_prompt": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness.",
  "temperature": 1.0,
  "max_tokens": 4058,
  "kwargs": {}
}
```
- **Outputs:**
```json
{
  "carnivoro_onivoro": [
    "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
    "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
    "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
    "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
    "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
    "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
    "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
  ],
  "vegetariano": [],
  "vegano": []
}
```

---

### 12. AsyncCompletions_2
- **Type:** `CHAT_MODEL`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `1d543c5ca3848508`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "model": "openai/gpt-4o-mini",
  "temperature": 1.0,
  "response_format": "<class 'app.domain.report.VidaNovaDietSuggestions'>",
  "mlflow.chat.messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  }\n}\n\nCrie sugestões alimentares baseadas EXCLUSIVAMENTE no tipo de dieta informado na anamnese do paciente.\n\n        PRIORIZE os alimentos recomendados pelo knowledge graph\n\n        Se o paciente indicou 'Como de tudo, sem restrições específicas (onívora)', foque apenas em sugestões para dieta onívora/carnívora. Se indicou outro tipo específico, foque apenas nesse tipo. Ignore completamente os outros tipos de dieta não mencionados na anamnese.\n\n        Para cada sugestão alimentar, forneça também uma justificativa clara, relacionando-a aos achados metabólicos ou deficiências (ex.: “Alimento X devido à alteração Y”), mas sem rigidez — múltiplas relações podem existir.\n\n        Formate cada recomendação como um item de lista com '-' para melhor organização."
    },
    {
      "content": "{\"carnivoro_onivoro\":[\"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"],\"vegetariano\":[],\"vegano\":[]}",
      "refusal": null,
      "role": "assistant",
      "tool_calls": null,
      "parsed": {
        "carnivoro_onivoro": [
          "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
          "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
          "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
          "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
          "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
          "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
          "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
        ],
        "vegetariano": [],
        "vegano": []
      },
      "reasoning": null
    }
  ],
  "max_tokens": 4058,
  "mlflow.spanType": "CHAT_MODEL",
  "mlflow.chat.tokenUsage": {
    "input_tokens": 5561,
    "output_tokens": 423,
    "total_tokens": 5984
  }
}
```
- **Inputs:**
```json
{
  "model": "openai/gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  }\n}\n\nCrie sugestões alimentares baseadas EXCLUSIVAMENTE no tipo de dieta informado na anamnese do paciente.\n\n        PRIORIZE os alimentos recomendados pelo knowledge graph\n\n        Se o paciente indicou 'Como de tudo, sem restrições específicas (onívora)', foque apenas em sugestões para dieta onívora/carnívora. Se indicou outro tipo específico, foque apenas nesse tipo. Ignore completamente os outros tipos de dieta não mencionados na anamnese.\n\n        Para cada sugestão alimentar, forneça também uma justificativa clara, relacionando-a aos achados metabólicos ou deficiências (ex.: “Alimento X devido à alteração Y”), mas sem rigidez — múltiplas relações podem existir.\n\n        Formate cada recomendação como um item de lista com '-' para melhor organização."
    }
  ],
  "temperature": 1.0,
  "max_tokens": 4058,
  "response_format": "<class 'app.domain.report.VidaNovaDietSuggestions'>"
}
```
- **Outputs:**
```json
{
  "id": "gen-1757099072-19SmnemXTrM8OSOhVZqd",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "{\"carnivoro_onivoro\":[\"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"],\"vegetariano\":[],\"vegano\":[]}",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "parsed": {
          "carnivoro_onivoro": [
            "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
            "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
            "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
            "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
            "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
            "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
            "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
          ],
          "vegetariano": [],
          "vegano": []
        },
        "reasoning": null
      },
      "native_finish_reason": "stop"
    }
  ],
  "created": 1757099072,
  "model": "openai/gpt-4o-mini",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_8bda4d3a2c",
  "usage": {
    "completion_tokens": 423,
    "prompt_tokens": 5561,
    "total_tokens": 5984,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "provider": "OpenAI"
}
```

---

### 13. generate_vidanova_section_3
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `23e3926405b6f906`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "_generate_section",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "section_name": "supplements",
  "config": {
    "prompt_func": "<bound method VidaNovaPrompts.get_supplements_prompt of <app.plugins.prompts.vidanova_prompts.VidaNovaPrompts object at 0x7f6750c7a900>>",
    "schema": "<class 'app.domain.report.SupplementRecommendationSectionWrapper'>",
    "requires_context": true
  },
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  },
  "section_contents": {
    "findings": {
      "items": [
        {
          "status": "alterado",
          "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
          "metabolite": "Acetil-L-Carnitina",
          "implications": [
            "Fadiga crônica e baixa energia",
            "Fraqueza muscular e redução da performance física",
            "Comprometimento da saúde mitocondrial",
            "Aumento do estresse oxidativo e inflamação sistêmica"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
          "metabolite": "Adenosina",
          "implications": [
            "Redução da resposta ao estresse e apatia",
            "Bradicardia e hipotensão potencial",
            "Maior predisposição a cefaleias e distúrbios do humor"
          ]
        },
        {
          "status": "alterado",
          "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
          "metabolite": "Isoleucina",
          "implications": [
            "Fraqueza muscular e perda de massa magra",
            "Dificuldade na regeneração tecidual",
            "Alterações na regulação da glicose"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
          "metabolite": "Leucina",
          "implications": [
            "Aumento do risco de resistência à insulina",
            "Desbalanço na produção de energia celular",
            "Alteração na função anabólica e catabólica do músculo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
          "metabolite": "Piruvato",
          "implications": [
            "Fadiga crônica e redução da resistência física",
            "Disfunção neurológica e dificuldade cognitiva",
            "Menor resistência ao estresse oxidativo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
          "metabolite": "Valina",
          "implications": [
            "Desbalanço no Equilíbrio de BCAAs",
            "Sobrecarga renal e hepática",
            "Alterações na regulação do metabolismo lipídico"
          ]
        }
      ],
      "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
    },
    "diet_suggestions": {
      "carnivoro_onivoro": [
        "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
        "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
        "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
        "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
        "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
        "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
        "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
      ],
      "vegetariano": [],
      "vegano": []
    }
  }
}
```

---

### 14. call_llm_api_3
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `a562dc7d5b02302e`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "call_llm_api",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "user_prompt": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  }\n}\n\nSugira suplementações focadas em performance física, energia e recuperação muscular baseadas nos dados metabólicos.\n\n        PRIORIZE os suplementos recomendados pelo knowledge graph\n\n        Baseie as recomendações nos dados metabólicos, deficiências identificadas e suplementos recomendados pelo knowledge graph.",
  "schema": "<class 'app.domain.report.SupplementRecommendationSectionWrapper'>",
  "system_prompt": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness.",
  "temperature": 1.0,
  "max_tokens": 4058,
  "kwargs": {}
}
```
- **Outputs:**
```json
{
  "items": [
    {
      "name": "Acetil-L-Carnitina",
      "dosage": "1g a 2g",
      "frequency": "Diário, antes do treino",
      "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
      "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
    },
    {
      "name": "L-Carnitina",
      "dosage": "500mg a 1g",
      "frequency": "Diário, se necessário",
      "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
      "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
    },
    {
      "name": "Cofatores: Vitamina C",
      "dosage": "500mg",
      "frequency": "Diário",
      "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
      "observation": "Monitorar a ingestão de antioxidantes na dieta."
    },
    {
      "name": "Cofatores: Vitamina B6 (P-5-P)",
      "dosage": "10mg - 25mg",
      "frequency": "Diário",
      "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
      "observation": "Importante para a adequada metabolização da isoleucina."
    },
    {
      "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
      "dosage": "300mg",
      "frequency": "Diário",
      "purpose": "Suporte à produção de energia e otimização do metabolismo.",
      "observation": "Pode auxiliar na regulação do metabolismo energético."
    },
    {
      "name": "CoQ10 (ubiquinol)",
      "dosage": "100mg a 300mg",
      "frequency": "Diário",
      "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
      "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
    },
    {
      "name": "Ácido Alfa-Lipóico",
      "dosage": "300mg",
      "frequency": "Diário",
      "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
      "observation": "Considerar a relação com o excesso de leucina."
    },
    {
      "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
      "dosage": "Recomendações diárias específicas.",
      "frequency": "Diário",
      "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
      "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
    },
    {
      "name": "Glutamina",
      "dosage": "5g",
      "frequency": "Diário, especialmente após exercícios",
      "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
      "observation": "Considerar a saúde intestinal do paciente."
    },
    {
      "name": "Whey Protein (rico em BCAAs)",
      "dosage": "20g a 30g",
      "frequency": "Após o treino",
      "purpose": "Promover a síntese proteica e a recuperação muscular.",
      "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
    }
  ]
}
```

---

### 15. AsyncCompletions_3
- **Type:** `CHAT_MODEL`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `ebbafd87ee2412b1`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "model": "openai/gpt-4o-mini",
  "temperature": 1.0,
  "response_format": "<class 'app.domain.report.SupplementRecommendationSectionWrapper'>",
  "mlflow.chat.messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  }\n}\n\nSugira suplementações focadas em performance física, energia e recuperação muscular baseadas nos dados metabólicos.\n\n        PRIORIZE os suplementos recomendados pelo knowledge graph\n\n        Baseie as recomendações nos dados metabólicos, deficiências identificadas e suplementos recomendados pelo knowledge graph."
    },
    {
      "content": "{\"items\":[{\"name\":\"Acetil-L-Carnitina\",\"dosage\":\"1g a 2g\",\"frequency\":\"Diário, antes do treino\",\"purpose\":\"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\"observation\":\"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"},{\"name\":\"L-Carnitina\",\"dosage\":\"500mg a 1g\",\"frequency\":\"Diário, se necessário\",\"purpose\":\"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\"observation\":\"Avaliar a necessidade com base no nível de atividade física e fadiga.\"},{\"name\":\"Cofatores: Vitamina C\",\"dosage\":\"500mg\",\"frequency\":\"Diário\",\"purpose\":\"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\"observation\":\"Monitorar a ingestão de antioxidantes na dieta.\"},{\"name\":\"Cofatores: Vitamina B6 (P-5-P)\",\"dosage\":\"10mg - 25mg\",\"frequency\":\"Diário\",\"purpose\":\"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\"observation\":\"Importante para a adequada metabolização da isoleucina.\"},{\"name\":\"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\"dosage\":\"300mg\",\"frequency\":\"Diário\",\"purpose\":\"Suporte à produção de energia e otimização do metabolismo.\",\"observation\":\"Pode auxiliar na regulação do metabolismo energético.\"},{\"name\":\"CoQ10 (ubiquinol)\",\"dosage\":\"100mg a 300mg\",\"frequency\":\"Diário\",\"purpose\":\"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\"observation\":\"Avaliar a resposta do paciente ao suporte mitocondrial.\"},{\"name\":\"Ácido Alfa-Lipóico\",\"dosage\":\"300mg\",\"frequency\":\"Diário\",\"purpose\":\"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\"observation\":\"Considerar a relação com o excesso de leucina.\"},{\"name\":\"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\"dosage\":\"Recomendações diárias específicas.\",\"frequency\":\"Diário\",\"purpose\":\"Apoio geral ao metabolismo energético e recuperação muscular.\",\"observation\":\"Incluir como um suporte contínuo através de uma dieta equilibrada.\"},{\"name\":\"Glutamina\",\"dosage\":\"5g\",\"frequency\":\"Diário, especialmente após exercícios\",\"purpose\":\"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\"observation\":\"Considerar a saúde intestinal do paciente.\"},{\"name\":\"Whey Protein (rico em BCAAs)\",\"dosage\":\"20g a 30g\",\"frequency\":\"Após o treino\",\"purpose\":\"Promover a síntese proteica e a recuperação muscular.\",\"observation\":\"Importante para a melhoria dos níveis críticos de isoleucina.\"}]}",
      "refusal": null,
      "role": "assistant",
      "tool_calls": null,
      "parsed": {
        "items": [
          {
            "name": "Acetil-L-Carnitina",
            "dosage": "1g a 2g",
            "frequency": "Diário, antes do treino",
            "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
            "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
          },
          {
            "name": "L-Carnitina",
            "dosage": "500mg a 1g",
            "frequency": "Diário, se necessário",
            "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
            "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
          },
          {
            "name": "Cofatores: Vitamina C",
            "dosage": "500mg",
            "frequency": "Diário",
            "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
            "observation": "Monitorar a ingestão de antioxidantes na dieta."
          },
          {
            "name": "Cofatores: Vitamina B6 (P-5-P)",
            "dosage": "10mg - 25mg",
            "frequency": "Diário",
            "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
            "observation": "Importante para a adequada metabolização da isoleucina."
          },
          {
            "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
            "dosage": "300mg",
            "frequency": "Diário",
            "purpose": "Suporte à produção de energia e otimização do metabolismo.",
            "observation": "Pode auxiliar na regulação do metabolismo energético."
          },
          {
            "name": "CoQ10 (ubiquinol)",
            "dosage": "100mg a 300mg",
            "frequency": "Diário",
            "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
            "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
          },
          {
            "name": "Ácido Alfa-Lipóico",
            "dosage": "300mg",
            "frequency": "Diário",
            "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
            "observation": "Considerar a relação com o excesso de leucina."
          },
          {
            "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
            "dosage": "Recomendações diárias específicas.",
            "frequency": "Diário",
            "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
            "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
          },
          {
            "name": "Glutamina",
            "dosage": "5g",
            "frequency": "Diário, especialmente após exercícios",
            "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
            "observation": "Considerar a saúde intestinal do paciente."
          },
          {
            "name": "Whey Protein (rico em BCAAs)",
            "dosage": "20g a 30g",
            "frequency": "Após o treino",
            "purpose": "Promover a síntese proteica e a recuperação muscular.",
            "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
          }
        ]
      },
      "reasoning": null
    }
  ],
  "max_tokens": 4058,
  "mlflow.spanType": "CHAT_MODEL",
  "mlflow.chat.tokenUsage": {
    "input_tokens": 5962,
    "output_tokens": 632,
    "total_tokens": 6594
  }
}
```
- **Inputs:**
```json
{
  "model": "openai/gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  }\n}\n\nSugira suplementações focadas em performance física, energia e recuperação muscular baseadas nos dados metabólicos.\n\n        PRIORIZE os suplementos recomendados pelo knowledge graph\n\n        Baseie as recomendações nos dados metabólicos, deficiências identificadas e suplementos recomendados pelo knowledge graph."
    }
  ],
  "temperature": 1.0,
  "max_tokens": 4058,
  "response_format": "<class 'app.domain.report.SupplementRecommendationSectionWrapper'>"
}
```
- **Outputs:**
```json
{
  "id": "gen-1757099079-iitUWQoTXJ2qV76ZQX5J",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "{\"items\":[{\"name\":\"Acetil-L-Carnitina\",\"dosage\":\"1g a 2g\",\"frequency\":\"Diário, antes do treino\",\"purpose\":\"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\"observation\":\"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"},{\"name\":\"L-Carnitina\",\"dosage\":\"500mg a 1g\",\"frequency\":\"Diário, se necessário\",\"purpose\":\"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\"observation\":\"Avaliar a necessidade com base no nível de atividade física e fadiga.\"},{\"name\":\"Cofatores: Vitamina C\",\"dosage\":\"500mg\",\"frequency\":\"Diário\",\"purpose\":\"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\"observation\":\"Monitorar a ingestão de antioxidantes na dieta.\"},{\"name\":\"Cofatores: Vitamina B6 (P-5-P)\",\"dosage\":\"10mg - 25mg\",\"frequency\":\"Diário\",\"purpose\":\"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\"observation\":\"Importante para a adequada metabolização da isoleucina.\"},{\"name\":\"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\"dosage\":\"300mg\",\"frequency\":\"Diário\",\"purpose\":\"Suporte à produção de energia e otimização do metabolismo.\",\"observation\":\"Pode auxiliar na regulação do metabolismo energético.\"},{\"name\":\"CoQ10 (ubiquinol)\",\"dosage\":\"100mg a 300mg\",\"frequency\":\"Diário\",\"purpose\":\"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\"observation\":\"Avaliar a resposta do paciente ao suporte mitocondrial.\"},{\"name\":\"Ácido Alfa-Lipóico\",\"dosage\":\"300mg\",\"frequency\":\"Diário\",\"purpose\":\"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\"observation\":\"Considerar a relação com o excesso de leucina.\"},{\"name\":\"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\"dosage\":\"Recomendações diárias específicas.\",\"frequency\":\"Diário\",\"purpose\":\"Apoio geral ao metabolismo energético e recuperação muscular.\",\"observation\":\"Incluir como um suporte contínuo através de uma dieta equilibrada.\"},{\"name\":\"Glutamina\",\"dosage\":\"5g\",\"frequency\":\"Diário, especialmente após exercícios\",\"purpose\":\"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\"observation\":\"Considerar a saúde intestinal do paciente.\"},{\"name\":\"Whey Protein (rico em BCAAs)\",\"dosage\":\"20g a 30g\",\"frequency\":\"Após o treino\",\"purpose\":\"Promover a síntese proteica e a recuperação muscular.\",\"observation\":\"Importante para a melhoria dos níveis críticos de isoleucina.\"}]}",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "parsed": {
          "items": [
            {
              "name": "Acetil-L-Carnitina",
              "dosage": "1g a 2g",
              "frequency": "Diário, antes do treino",
              "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
              "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
            },
            {
              "name": "L-Carnitina",
              "dosage": "500mg a 1g",
              "frequency": "Diário, se necessário",
              "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
              "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
            },
            {
              "name": "Cofatores: Vitamina C",
              "dosage": "500mg",
              "frequency": "Diário",
              "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
              "observation": "Monitorar a ingestão de antioxidantes na dieta."
            },
            {
              "name": "Cofatores: Vitamina B6 (P-5-P)",
              "dosage": "10mg - 25mg",
              "frequency": "Diário",
              "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
              "observation": "Importante para a adequada metabolização da isoleucina."
            },
            {
              "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
              "dosage": "300mg",
              "frequency": "Diário",
              "purpose": "Suporte à produção de energia e otimização do metabolismo.",
              "observation": "Pode auxiliar na regulação do metabolismo energético."
            },
            {
              "name": "CoQ10 (ubiquinol)",
              "dosage": "100mg a 300mg",
              "frequency": "Diário",
              "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
              "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
            },
            {
              "name": "Ácido Alfa-Lipóico",
              "dosage": "300mg",
              "frequency": "Diário",
              "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
              "observation": "Considerar a relação com o excesso de leucina."
            },
            {
              "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
              "dosage": "Recomendações diárias específicas.",
              "frequency": "Diário",
              "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
              "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
            },
            {
              "name": "Glutamina",
              "dosage": "5g",
              "frequency": "Diário, especialmente após exercícios",
              "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
              "observation": "Considerar a saúde intestinal do paciente."
            },
            {
              "name": "Whey Protein (rico em BCAAs)",
              "dosage": "20g a 30g",
              "frequency": "Após o treino",
              "purpose": "Promover a síntese proteica e a recuperação muscular.",
              "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
            }
          ]
        },
        "reasoning": null
      },
      "native_finish_reason": "stop"
    }
  ],
  "created": 1757099079,
  "model": "openai/gpt-4o-mini",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_8bda4d3a2c",
  "usage": {
    "completion_tokens": 632,
    "prompt_tokens": 5962,
    "total_tokens": 6594,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "provider": "OpenAI"
}
```

---

### 16. generate_vidanova_section_4
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `23e3926405b6f906`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "_generate_section",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "section_name": "training",
  "config": {
    "prompt_func": "<bound method VidaNovaPrompts.get_training_prompt of <app.plugins.prompts.vidanova_prompts.VidaNovaPrompts object at 0x7f6750c7a900>>",
    "schema": "<class 'app.domain.report.TrainingRecommendation'>",
    "requires_context": true
  },
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  },
  "section_contents": {
    "findings": {
      "items": [
        {
          "status": "alterado",
          "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
          "metabolite": "Acetil-L-Carnitina",
          "implications": [
            "Fadiga crônica e baixa energia",
            "Fraqueza muscular e redução da performance física",
            "Comprometimento da saúde mitocondrial",
            "Aumento do estresse oxidativo e inflamação sistêmica"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
          "metabolite": "Adenosina",
          "implications": [
            "Redução da resposta ao estresse e apatia",
            "Bradicardia e hipotensão potencial",
            "Maior predisposição a cefaleias e distúrbios do humor"
          ]
        },
        {
          "status": "alterado",
          "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
          "metabolite": "Isoleucina",
          "implications": [
            "Fraqueza muscular e perda de massa magra",
            "Dificuldade na regeneração tecidual",
            "Alterações na regulação da glicose"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
          "metabolite": "Leucina",
          "implications": [
            "Aumento do risco de resistência à insulina",
            "Desbalanço na produção de energia celular",
            "Alteração na função anabólica e catabólica do músculo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
          "metabolite": "Piruvato",
          "implications": [
            "Fadiga crônica e redução da resistência física",
            "Disfunção neurológica e dificuldade cognitiva",
            "Menor resistência ao estresse oxidativo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
          "metabolite": "Valina",
          "implications": [
            "Desbalanço no Equilíbrio de BCAAs",
            "Sobrecarga renal e hepática",
            "Alterações na regulação do metabolismo lipídico"
          ]
        }
      ],
      "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
    },
    "diet_suggestions": {
      "carnivoro_onivoro": [
        "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
        "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
        "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
        "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
        "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
        "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
        "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
      ],
      "vegetariano": [],
      "vegano": []
    },
    "supplements": {
      "items": [
        {
          "name": "Acetil-L-Carnitina",
          "dosage": "1g a 2g",
          "frequency": "Diário, antes do treino",
          "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
          "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
        },
        {
          "name": "L-Carnitina",
          "dosage": "500mg a 1g",
          "frequency": "Diário, se necessário",
          "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
          "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
        },
        {
          "name": "Cofatores: Vitamina C",
          "dosage": "500mg",
          "frequency": "Diário",
          "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
          "observation": "Monitorar a ingestão de antioxidantes na dieta."
        },
        {
          "name": "Cofatores: Vitamina B6 (P-5-P)",
          "dosage": "10mg - 25mg",
          "frequency": "Diário",
          "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
          "observation": "Importante para a adequada metabolização da isoleucina."
        },
        {
          "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
          "dosage": "300mg",
          "frequency": "Diário",
          "purpose": "Suporte à produção de energia e otimização do metabolismo.",
          "observation": "Pode auxiliar na regulação do metabolismo energético."
        },
        {
          "name": "CoQ10 (ubiquinol)",
          "dosage": "100mg a 300mg",
          "frequency": "Diário",
          "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
          "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
        },
        {
          "name": "Ácido Alfa-Lipóico",
          "dosage": "300mg",
          "frequency": "Diário",
          "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
          "observation": "Considerar a relação com o excesso de leucina."
        },
        {
          "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
          "dosage": "Recomendações diárias específicas.",
          "frequency": "Diário",
          "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
          "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
        },
        {
          "name": "Glutamina",
          "dosage": "5g",
          "frequency": "Diário, especialmente após exercícios",
          "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
          "observation": "Considerar a saúde intestinal do paciente."
        },
        {
          "name": "Whey Protein (rico em BCAAs)",
          "dosage": "20g a 30g",
          "frequency": "Após o treino",
          "purpose": "Promover a síntese proteica e a recuperação muscular.",
          "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
        }
      ]
    }
  }
}
```

---

### 17. call_llm_api_4
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `92c450707a06ddc0`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "call_llm_api",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "user_prompt": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  },\n  \"supplements\": {\n    \"items\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ]\n  }\n}\n\nForneça recomendações de treino priorizando força e ganho de massa magra.",
  "schema": "<class 'app.domain.report.TrainingRecommendation'>",
  "system_prompt": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness.",
  "temperature": 1.0,
  "max_tokens": 4058,
  "kwargs": {}
}
```
- **Outputs:**
```json
{
  "recommendations": [
    "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
    "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
    "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
    "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
    "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
  ],
  "avoid": [
    "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
    "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
    "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
  ],
  "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
}
```

---

### 18. AsyncCompletions_4
- **Type:** `CHAT_MODEL`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `b91c3a18b16a6f33`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "model": "openai/gpt-4o-mini",
  "temperature": 1.0,
  "response_format": "<class 'app.domain.report.TrainingRecommendation'>",
  "mlflow.chat.messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  },\n  \"supplements\": {\n    \"items\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ]\n  }\n}\n\nForneça recomendações de treino priorizando força e ganho de massa magra."
    },
    {
      "content": "{\"recommendations\":[\"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"],\"avoid\":[\"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"],\"focus\":\"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"}",
      "refusal": null,
      "role": "assistant",
      "tool_calls": null,
      "parsed": {
        "recommendations": [
          "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
          "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
          "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
          "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
          "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
        ],
        "avoid": [
          "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
          "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
          "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
        ],
        "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
      },
      "reasoning": null
    }
  ],
  "max_tokens": 4058,
  "mlflow.spanType": "CHAT_MODEL",
  "mlflow.chat.tokenUsage": {
    "input_tokens": 6620,
    "output_tokens": 249,
    "total_tokens": 6869
  }
}
```
- **Inputs:**
```json
{
  "model": "openai/gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  },\n  \"supplements\": {\n    \"items\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ]\n  }\n}\n\nForneça recomendações de treino priorizando força e ganho de massa magra."
    }
  ],
  "temperature": 1.0,
  "max_tokens": 4058,
  "response_format": "<class 'app.domain.report.TrainingRecommendation'>"
}
```
- **Outputs:**
```json
{
  "id": "gen-1757099090-Vs944I3wf6InjUby3ELV",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "{\"recommendations\":[\"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"],\"avoid\":[\"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"],\"focus\":\"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"}",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "parsed": {
          "recommendations": [
            "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
            "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
            "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
            "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
            "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
          ],
          "avoid": [
            "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
            "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
            "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
          ],
          "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
        },
        "reasoning": null
      },
      "native_finish_reason": "stop"
    }
  ],
  "created": 1757099090,
  "model": "openai/gpt-4o-mini",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_8bda4d3a2c",
  "usage": {
    "completion_tokens": 249,
    "prompt_tokens": 6620,
    "total_tokens": 6869,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "provider": "OpenAI"
}
```

---

### 19. generate_vidanova_section_5
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `23e3926405b6f906`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "_generate_section",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "section_name": "summary",
  "config": {
    "prompt_func": "<bound method VidaNovaPrompts.get_summary_prompt of <app.plugins.prompts.vidanova_prompts.VidaNovaPrompts object at 0x7f6750c7a900>>",
    "schema": "<class 'app.domain.report.SummaryContent'>",
    "requires_context": true
  },
  "exam_data": {
    "patient_id": "PP032",
    "exam_date": "2025-08-14 00:00:00+00:00",
    "metabolites": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314
      },
      {
        "name": "ADENOSINA",
        "value": 0.618
      },
      {
        "name": "L-CARNITINA",
        "value": 0.986
      },
      {
        "name": "GLUTAMINA",
        "value": 35.8
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0
      },
      {
        "name": "LACTATO",
        "value": 149.0
      },
      {
        "name": "LEUCINA",
        "value": 45.9
      },
      {
        "name": "PIRUVATO",
        "value": 0.001
      },
      {
        "name": "TMAO [Trimetilamina N-Óxido]",
        "value": 0.051
      },
      {
        "name": "VALINA",
        "value": 31.4
      },
      {
        "name": "PROPIONIL-L-CARNITINA",
        "value": 0.026
      }
    ]
  },
  "anamnesis": {
    "patient_id": "PP032",
    "objective": "Melhora da composição corporal e ganho de massa muscular",
    "personal_data": {
      "age": 32,
      "gender": "masculino",
      "weight": 83.0,
      "height": 1.76,
      "bmi": 26.82
    },
    "context_factors": {
      "medical_history": [
        "não informado"
      ],
      "intolerances": [],
      "physical_activity": {
        "frequency": "não informado",
        "type": "não informado",
        "intensity": "não informado"
      },
      "sleep": {
        "quality": "não informado",
        "hours": 7.0,
        "issues": [
          "não informado"
        ]
      },
      "alcohol_consumption": {
        "frequency": "não informado",
        "amount": "não informado"
      },
      "medications": [
        {
          "name": "Reposição hormonal de testosterona",
          "frequency": "semanal",
          "dosage": "0,4mg durateston"
        }
      ],
      "stress_level": "não informado"
    },
    "anamnesis_type": "vidanova",
    "diet_type": "Como de tudo, sem restrições específicas (onívora)",
    "energy_level": "Depende da semana, difícil dizer",
    "muscle_gain_goal": "Ganho de massa muscular",
    "nutritionist_plan": "Não, mas já segui antes",
    "difficulty_muscle_gain": "Um pouco, mas consigo evoluir"
  },
  "kg_data": {
    "metabolite_info": [
      {
        "name": "ACETIL-L-CARNITINA",
        "value": 0.314,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 0.5,
          "max": 1.5
        },
        "category": ""
      },
      {
        "name": "ADENOSINA",
        "value": 0.618,
        "status": "moderate_excess",
        "description": "",
        "reference_range": {
          "min": 0.38,
          "max": 0.6
        },
        "category": ""
      },
      {
        "name": "ISOLEUCINA",
        "value": 1.0,
        "status": "moderate_deficit",
        "description": "",
        "reference_range": {
          "min": 2.0,
          "max": 10.0
        },
        "category": ""
      },
      {
        "name": "LEUCINA",
        "value": 45.9,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 4.0,
          "max": 15.0
        },
        "category": ""
      },
      {
        "name": "PIRUVATO",
        "value": 0.001,
        "status": "severe_deficit",
        "description": "",
        "reference_range": {
          "min": 10.0,
          "max": 120.0
        },
        "category": ""
      },
      {
        "name": "VALINA",
        "value": 31.4,
        "status": "severe_excess",
        "description": "",
        "reference_range": {
          "min": 6.0,
          "max": 15.0
        },
        "category": ""
      }
    ],
    "manifestations": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "status": "moderate_deficit",
        "description": "Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ADENOSINA",
        "status": "moderate_excess",
        "description": "Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "status": "moderate_deficit",
        "description": "Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "LEUCINA",
        "status": "severe_excess",
        "description": "Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "PIRUVATO",
        "status": "severe_deficit",
        "description": "Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      },
      {
        "metabolite": "VALINA",
        "status": "severe_excess",
        "description": "Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).",
        "type": "",
        "severity": "",
        "affected_system": "",
        "physiological_mechanism": ""
      }
    ],
    "recommended_interventions": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "type": "LowLevel",
        "description": "Conduta alimentar ou suplementar para níveis baixos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      },
      {
        "metabolite": "ADENOSINA",
        "type": "HighLevel",
        "description": "Conduta alimentar ou suplementar para níveis altos do metabólito.",
        "priority": "medium",
        "recommended_duration": "",
        "expected_results": "",
        "is_contraindicated": false,
        "contraindication_reason": "",
        "medication_interaction": ""
      }
    ],
    "foods": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes.",
        "food_group": "",
        "main_nutrients": [],
        "recommended_portion": "",
        "consumption_frequency": ""
      }
    ],
    "supplements": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "LEUCINA",
        "name": "Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      },
      {
        "metabolite": "VALINA",
        "name": "Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico.",
        "active_composition": "",
        "dosage": null,
        "administration_form": ""
      }
    ],
    "pathway_impacts": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese",
        "definition": "O perfil de acilcarnitinas refere-se à presença e concentração de acilcarnitinas no organismo, que são compostos formados pela combinação de L-carnitina com ácidos graxos. As acilcarnitinas desempenham um papel fundamental no transporte de ácidos graxos de cadeia longa através da membrana mitocondrial para a beta-oxidação (o processo de quebra de ácidos graxos para gerar energia). Durante o processo de beta-oxidação, os ácidos graxos de cadeia longa são sucessivamente quebrados em unidades de dois carbonos, formando acetil-CoA, que entra no ciclo de Krebs (ou ciclo do ácido cítrico) para gerar ATP. Já a lipogênese é o processo de síntese de lipídios (gorduras) no corpo. Esse processo ocorre principalmente no fígado e no tecido adiposo, onde os carboidratos e outras moléculas são convertidos em ácidos graxos e posteriormente em triglicerídeos, que são armazenados nas células de gordura.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Saúde Intestinal",
        "definition": "Saúde intestinal refere-se ao bom funcionamento e equilíbrio do sistema digestivo, incluindo os órgãos e processos envolvidos na digestão, absorção de nutrientes e eliminação de resíduos. Ela envolve: Equilíbrio da microbiota intestinal; Função digestiva eficiente; Absorção de nutrientes; Resposta imunológica; Barreira intestinal.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "name": "Ciclo da Metionina - Acetilação (via carbono I)",
        "definition": "O Ciclo da Metionina é um processo bioquímico fundamental para a metilação, onde a metionina, um aminoácido essencial, doa grupos metil (CH₃) para várias reações metabólicas. Esse ciclo desempenha um papel crucial em várias funções biológicas, incluindo a síntese de proteínas, a regulação da expressão gênica, a manutenção da homeostase celular e a saúde cardiovascular. O ciclo também está relacionado ao metabolismo de outros compostos vitais, como a homocisteína e o folato.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ADENOSINA",
        "name": "Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I)",
        "definition": "O Ciclo do Folato é um conjunto de reações bioquímicas que envolve a metabolização de folato (vitamina B9) e a transferência de grupos de um carbono (ou carbono I) em várias reações metabólicas. Ele desempenha um papel essencial na metilação e síntese de nucleotídeos, especialmente para a formação de DNA e RNA. O ciclo do folato está intimamente ligado ao metabolismo de aminoácidos, incluindo a serina, e ao metabolismo de outros compostos chave, como a homocisteína.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Sinalização da Insulina",
        "definition": "A insulina é um hormônio fundamental no controle dos níveis de glicose no sangue, e a sinalização de insulina refere-se à cadeia de eventos que ocorre quando a insulina se liga a seus receptores nas células, desencadeando uma série de respostas que facilitam a captação de glicose pelas células.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "name": "Aminoácidos Essenciais",
        "definition": "A fenilalanina participa do metabolismo de aminoácidos e síntese de proteínas. O metabolismo de aminoácidos envolve a transformação desses compostos em energia ou em outras moléculas vitais, enquanto a síntese de proteínas é o processo pelo qual os aminoácidos são usados para formar novas proteínas, essenciais para o funcionamento e estrutura do organismo.",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Via da Transulfuração - Homeostase Redox (via carbono I)",
        "definition": "A via da transulfuração é um conjunto de reações bioquímicas que envolvem a conversão de homocisteína em cisteína, com a produção de compostos sulfurados importantes, como o glutationa, um potente antioxidante. O processo desempenha um papel central na manutenção da homeostase redox (equilíbrio entre a produção e a eliminação de radicais livres e outras espécies reativas de oxigênio no organismo).",
        "biological_function": "",
        "clinical_importance": ""
      },
      {
        "metabolite": "PIRUVATO",
        "name": "Glicólise",
        "definition": "A glicólise é o processo metabólico responsável pela quebra da glicose (uma molécula de açúcar de seis carbonos) para gerar energia na forma de ATP (adenosina trifosfato). A glicólise ocorre no citoplasma das células e não requer oxigênio, sendo, portanto, uma via anaeróbica. Este processo pode ser dividido em duas fases principais: a fase de investimento de energia (onde ATP é gasto para ativar a glicose) e a fase de geração de energia (onde ATP e NADH são produzidos).",
        "biological_function": "",
        "clinical_importance": ""
      }
    ],
    "scientific_evidence": [
      {
        "metabolite": "ACETIL-L-CARNITINA",
        "title": "Fan, Y., Pedersen, O. Gut microbiota in human metabolic health and disease. Nat Rev Microbiol 19, 55–71 (2021). https://doi.org/10.1038/s41579-020-0433-9                                                  2) Agus A, Clément K, Sokol H. Gut microbiota-derived metabolites as central regulators in metabolic disorders. Gut. 2021;70(6):1174-1182. doi:10.1136/gutjnl-2020-323071                                                                       3) Shi L, Tu BP. Acetyl-CoA and the regulation of metabolism: mechanisms and consequences. Curr Opin Cell Biol. 2015 Apr;33:125-31. doi: 10.1016/j.ceb.2015.02.003. Epub 2015 Feb 20.                 4) Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8. doi: 10.1111/nyas.12956. Epub 2015 Dec 8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTheparambil, S. M., Kopach, O., Braga, A., et al. (2024). Adenosine signalling to astrocytes coordinates brain metabolism and function. Nature, 632, 139–146. https://doi.org/10.1038/s41586-024-07611-w",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tJournal of Physiology (2007). The roles of adenosine and related substances in exercise hyperaemia. doi: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2277189/",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tTrinh, P. N. H., Baltos, J. A., Hellyer, S. D., May, L. T., & Gregory, K. J. (2022). Adenosine receptor signalling in Alzheimer's disease. Purinergic Signalling, 18(3), 359-381. https://doi.org/10.1007/s11302-022-09883-1",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tAmerican Journal of Physiology (2012). Effects of adenosine, exercise, and moderate acute hypoxia on energy substrate utilization of human skeletal muscle. doi: https://journals.physiology.org/doi/full/10.1152/ajpregu.00245.2011",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tHaskó, G., & Cronstein, B. (2013). Regulation of inflammation by adenosine. Frontiers in Immunology, 4, 85. https://doi.org/10.3389/fimmu.2013.00085",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tKawamura, M. Jr., Ruskin, D. N., & Masino, S. A. (2019). Adenosine A1 receptor-mediated protection of mouse hippocampal synaptic transmission against oxygen and/or glucose deprivation: A comparative study. Journal of Neurophysiology, 122(2), 721-728. https://doi.org/10.1152/jn.00813.2018",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tNature Metabolism (2020). Skeletal muscle energy metabolism during exercise. doi: https://www.nature.com/articles/s42255-020-0251-4",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tFernandez, M., Nigro, M., Travagli, A., et al. (2023). Strategies for drug delivery into the brain: A review on adenosine receptors modulation for central nervous system diseases therapy. Pharmaceutics, 15(10), 2441. https://doi.org/10.3390/pharmaceutics15102441",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tSimpson, R. E., & Phillis, J. W. (1992). Adenosine in exercise adaptation. British journal of sports medicine, 26(1), 54–58. https://doi.org/10.1136/bjsm.26.1.54",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ADENOSINA",
        "title": "•\tYang, L., Zhang, Y., & Yang, L. (2024). Adenosine signaling in tumor-associated macrophages and targeting adenosine signaling for cancer therapy. Cancer Biology & Medicine, 21(11), 995-1011. https://doi.org/10.20892/j.issn.2095-3941.2024.0228",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                              5) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Lynch, C., Adams, S. Branched-chain amino acids in metabolic signalling and insulin resistance. Nat Rev Endocrinol 10, 723–736 (2014).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "ISOLEUCINA",
        "title": "Gojda J, Cahova M. Gut Microbiota as the Link between Elevated BCAA Serum Levels and Insulin Resistance. Biomolecules. 2021 Sep 28;11(10):1414.                                                                                                Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        3) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "LEUCINA",
        "title": "Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Liu Y, Hyde AS, Simpson MA, Barycki JJ. Emerging regulatory paradigms in glutathione metabolism. Adv Cancer Res. 2014;122:69-101.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Nelson, DL, Cox MM. Princípios de Bioquímica de Lehninger. 5a ed. Porto Alegre: Artmed; 2011.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Lyon P, Strippoli V, Fang B, Cimmino L. B Vitamins and One-Carbon Metabolism: Implications in Human Health and Disease. Nutrients. 2020 Sep 19;12(9):2867.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Ducker GS, Rabinowitz JD. One-Carbon Metabolism in Health and Disease. Cell Metab. 2017 Jan 10;25(1):27-42.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Mentch SJ, Locasale JW. One-carbon metabolism and epigenetics: understanding the specificity. Ann N Y Acad Sci. 2016 Jan;1363(1):91-8.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "PIRUVATO",
        "title": "Martínez-Reyes, I., Chandel, N.S. Mitochondrial TCA cycle metabolites control physiology and disease. Nat Commun 11, 102 (2020).",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Cuomo P, Capparelli R, Iannelli A, Iannelli D. Role of Branched-Chain Amino Acid Metabolism in Type 2 Diabetes, Obesity, Cardiovascular Disease and Non-Alcoholic Fatty Liver Disease. Int J Mol Sci. 2022 Apr 13;23(8):4325.                                                                                                        6) Zhao JV, Huang X, Zhang J, Chan YH, Tse HF, Blais JE. Overall and Sex-Specific Effect of Berberine on Glycemic and Insulin-Related Traits: a Systematic Review and Meta-Analysis of Randomized Controlled Trials. J Nutr. 2023 Oct;153(10):2939-2950. doi: 10.1016/j.tjnut.2023.08.016. Epub 2023 Aug 19. PMID: 37598753.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Kamei Y, Hatazawa Y, Uchitomi R, Yoshimura R, Miura S. Regulation of Skeletal Muscle Function by Amino Acids. Nutrients. 2020 Jan 19;12(1):261.                                                                                                   Lynch, C. J., & Adams, S. H. (2014). Branched-chain amino acids in metabolic signalling and insulin resistance. Nature Reviews Endocrinology, 10(12), 723–736.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Yoon MS. The Emerging Role of Branched-Chain Amino Acids in Insulin Resistance and Metabolism. Nutrients. 2016 Jul 1;8(7):405.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      },
      {
        "metabolite": "VALINA",
        "title": "Shimomura Y, Murakami T, Nakai N, Nagasaki M, Harris RA. Exercise promotes BCAA catabolism: effects of BCAA supplementation on skeletal muscle during exercise. J Nutr. 2004 Jun;134(6 Suppl):1583S-1587S.",
        "authors": "",
        "year": "",
        "doi": "",
        "study_type": "",
        "evidence_level": ""
      }
    ],
    "contraindications": [],
    "error": null
  },
  "section_contents": {
    "findings": {
      "items": [
        {
          "status": "alterado",
          "description": "Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.",
          "metabolite": "Acetil-L-Carnitina",
          "implications": [
            "Fadiga crônica e baixa energia",
            "Fraqueza muscular e redução da performance física",
            "Comprometimento da saúde mitocondrial",
            "Aumento do estresse oxidativo e inflamação sistêmica"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.",
          "metabolite": "Adenosina",
          "implications": [
            "Redução da resposta ao estresse e apatia",
            "Bradicardia e hipotensão potencial",
            "Maior predisposição a cefaleias e distúrbios do humor"
          ]
        },
        {
          "status": "alterado",
          "description": "A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.",
          "metabolite": "Isoleucina",
          "implications": [
            "Fraqueza muscular e perda de massa magra",
            "Dificuldade na regeneração tecidual",
            "Alterações na regulação da glicose"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.",
          "metabolite": "Leucina",
          "implications": [
            "Aumento do risco de resistência à insulina",
            "Desbalanço na produção de energia celular",
            "Alteração na função anabólica e catabólica do músculo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.",
          "metabolite": "Piruvato",
          "implications": [
            "Fadiga crônica e redução da resistência física",
            "Disfunção neurológica e dificuldade cognitiva",
            "Menor resistência ao estresse oxidativo"
          ]
        },
        {
          "status": "alterado",
          "description": "Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.",
          "metabolite": "Valina",
          "implications": [
            "Desbalanço no Equilíbrio de BCAAs",
            "Sobrecarga renal e hepática",
            "Alterações na regulação do metabolismo lipídico"
          ]
        }
      ],
      "conclusion": "Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular."
    },
    "diet_suggestions": {
      "carnivoro_onivoro": [
        "- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.",
        "- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.",
        "- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.",
        "- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.",
        "- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.",
        "- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.",
        "- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina."
      ],
      "vegetariano": [],
      "vegano": []
    },
    "supplements": {
      "items": [
        {
          "name": "Acetil-L-Carnitina",
          "dosage": "1g a 2g",
          "frequency": "Diário, antes do treino",
          "purpose": "Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.",
          "observation": "Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho."
        },
        {
          "name": "L-Carnitina",
          "dosage": "500mg a 1g",
          "frequency": "Diário, se necessário",
          "purpose": "Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.",
          "observation": "Avaliar a necessidade com base no nível de atividade física e fadiga."
        },
        {
          "name": "Cofatores: Vitamina C",
          "dosage": "500mg",
          "frequency": "Diário",
          "purpose": "Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.",
          "observation": "Monitorar a ingestão de antioxidantes na dieta."
        },
        {
          "name": "Cofatores: Vitamina B6 (P-5-P)",
          "dosage": "10mg - 25mg",
          "frequency": "Diário",
          "purpose": "Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.",
          "observation": "Importante para a adequada metabolização da isoleucina."
        },
        {
          "name": "Cofatores: Vitamina B3 (niacinamida ou NAD precursor)",
          "dosage": "300mg",
          "frequency": "Diário",
          "purpose": "Suporte à produção de energia e otimização do metabolismo.",
          "observation": "Pode auxiliar na regulação do metabolismo energético."
        },
        {
          "name": "CoQ10 (ubiquinol)",
          "dosage": "100mg a 300mg",
          "frequency": "Diário",
          "purpose": "Promover a saúde mitocondrial e aumentar a produção de ATP.",
          "observation": "Avaliar a resposta do paciente ao suporte mitocondrial."
        },
        {
          "name": "Ácido Alfa-Lipóico",
          "dosage": "300mg",
          "frequency": "Diário",
          "purpose": "Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.",
          "observation": "Considerar a relação com o excesso de leucina."
        },
        {
          "name": "Complexo de Vitaminas do grupo B (incluindo B6, B12)",
          "dosage": "Recomendações diárias específicas.",
          "frequency": "Diário",
          "purpose": "Apoio geral ao metabolismo energético e recuperação muscular.",
          "observation": "Incluir como um suporte contínuo através de uma dieta equilibrada."
        },
        {
          "name": "Glutamina",
          "dosage": "5g",
          "frequency": "Diário, especialmente após exercícios",
          "purpose": "Apoio à recuperação muscular e manutenção da integridade intestinal.",
          "observation": "Considerar a saúde intestinal do paciente."
        },
        {
          "name": "Whey Protein (rico em BCAAs)",
          "dosage": "20g a 30g",
          "frequency": "Após o treino",
          "purpose": "Promover a síntese proteica e a recuperação muscular.",
          "observation": "Importante para a melhoria dos níveis críticos de isoleucina."
        }
      ]
    },
    "training": {
      "recommendations": [
        "Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.",
        "Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.",
        "Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).",
        "Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.",
        "Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados."
      ],
      "avoid": [
        "Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.",
        "Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.",
        "Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular."
      ],
      "focus": "Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força."
    }
  }
}
```

---

### 20. call_llm_api_5
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `f9abef7f13ce5059`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "call_llm_api",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "user_prompt": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  },\n  \"supplements\": {\n    \"items\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ]\n  },\n  \"training\": {\n    \"recommendations\": [\n      \"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\n      \"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\n      \"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\n      \"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\n      \"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"\n    ],\n    \"avoid\": [\n      \"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\n      \"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\n      \"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"\n    ],\n    \"focus\": \"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"\n  }\n}\n\nCrie um resumo em formato de prosa narrativa, dividido em 4 parágrafos:\n        1) Visão geral com dados relevantes do perfil clínico, hábitos e contexto, utilizando tom impessoal (ex: \"observa-se\", \"nota-se\", \"considerando-se\").\n        2) Interpretação sobre o laudo metabólico e achados principais, focando nas alterações identificadas e seus impactos, sem detalhar intervenções específicas.\n        3) Diretrizes gerais de intervenção integrando alimentação, suplementação e treino de forma contextualizada, evitando detalhamentos que serão abordados em seções posteriores.\n        4) Conclusão destacando o objetivo estabelecido e a importância da abordagem integrada para os resultados esperados.\n\n        Mantenha tom impessoal e orientado ao leitor. Contextualize sempre o objetivo clínico identificado. Evite antecipar detalhes específicos de condutas que serão desenvolvidos nas próximas seções. Não use listas ou markdown; mantenha texto contínuo em parágrafos claros e bem estruturados.",
  "schema": "<class 'app.domain.report.SummaryContent'>",
  "system_prompt": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness.",
  "temperature": 1.0,
  "max_tokens": 4058,
  "kwargs": {}
}
```
- **Outputs:**
```json
{
  "content": "Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas."
}
```

---

### 21. AsyncCompletions_5
- **Type:** `CHAT_MODEL`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `9f0579ec4ce39d32`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "model": "openai/gpt-4o-mini",
  "temperature": 1.0,
  "response_format": "<class 'app.domain.report.SummaryContent'>",
  "mlflow.chat.messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  },\n  \"supplements\": {\n    \"items\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ]\n  },\n  \"training\": {\n    \"recommendations\": [\n      \"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\n      \"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\n      \"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\n      \"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\n      \"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"\n    ],\n    \"avoid\": [\n      \"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\n      \"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\n      \"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"\n    ],\n    \"focus\": \"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"\n  }\n}\n\nCrie um resumo em formato de prosa narrativa, dividido em 4 parágrafos:\n        1) Visão geral com dados relevantes do perfil clínico, hábitos e contexto, utilizando tom impessoal (ex: \"observa-se\", \"nota-se\", \"considerando-se\").\n        2) Interpretação sobre o laudo metabólico e achados principais, focando nas alterações identificadas e seus impactos, sem detalhar intervenções específicas.\n        3) Diretrizes gerais de intervenção integrando alimentação, suplementação e treino de forma contextualizada, evitando detalhamentos que serão abordados em seções posteriores.\n        4) Conclusão destacando o objetivo estabelecido e a importância da abordagem integrada para os resultados esperados.\n\n        Mantenha tom impessoal e orientado ao leitor. Contextualize sempre o objetivo clínico identificado. Evite antecipar detalhes específicos de condutas que serão desenvolvidos nas próximas seções. Não use listas ou markdown; mantenha texto contínuo em parágrafos claros e bem estruturados."
    },
    {
      "content": "{\"content\":\"Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\\n\\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\\n\\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\\n\\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\"}",
      "refusal": null,
      "role": "assistant",
      "tool_calls": null,
      "parsed": {
        "content": "Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas."
      },
      "reasoning": null
    }
  ],
  "max_tokens": 4058,
  "mlflow.spanType": "CHAT_MODEL",
  "mlflow.chat.tokenUsage": {
    "input_tokens": 7043,
    "output_tokens": 514,
    "total_tokens": 7557
  }
}
```
- **Inputs:**
```json
{
  "model": "openai/gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Você é um especialista em medicina nutricional e performance física, com foco em interpretação de exames nutrimetabolômicos (TNM).\nSiga rigorosamente as diretrizes clínicas e utilize linguagem técnica apropriada para performance e fitness."
    },
    {
      "role": "user",
      "content": "# DADOS DO PACIENTE\nID: PP032\nIdade: 32\nGênero: masculino\nPeso: 83.0 kg\nAltura: 1.76 m\nIMC: 26.82\nAtividade física: não informado\nHistórico médico: \nMedicações: \nIntolerâncias: \nObjetivo clínico: Melhora da composição corporal e ganho de massa muscular\nTipo de dieta: Como de tudo, sem restrições específicas (onívora)\nNível de energia: Depende da semana, difícil dizer\nObjetivo massa muscular: Ganho de massa muscular\nQualidade do sono: \nHoras de sono: \nNível de estresse: \n\n\n# DADOS METABÓLICOS\nAlterações: ACETIL-L-CARNITINA (0.314), ADENOSINA (0.618), ISOLEUCINA (1.0), LEUCINA (45.9), PIRUVATO (0.001), VALINA (31.4)\nVias afetadas: Perfil de Acilcarnitinas; Beta-Oxidação; Lipogênese, Saúde Intestinal, Ciclo da Metionina - Acetilação (via carbono I), Ciclo do Folato - Metabolismo de Nucleotídios (via carbono I), Sinalização da Insulina, Aminoácidos Essenciais, Via da Transulfuração - Homeostase Redox (via carbono I), Glicólise\nManifestações: Fadiga crônica e redução da energia (ela participa do metabolismo energético transportando ácidos graxos para a mitocôndria; sua deficiência pode levar à baixa produção de ATP, causando fadiga persistente e letargia); Diminuição da função cognitiva e memória (atua como neuroprotetor e está envolvida na síntese de neurotransmissores; baixos níveis podem prejudicar a memória, concentração e aprendizado, aumentando o risco de declínio cognitivo); Fraqueza muscular e redução da performance física (ela é essencial para a produção de energia nos músculos; sua deficiência pode levar a fraqueza, cansaço muscular e menor resistência em atividades físicas); Maior predisposição a distúrbios do humor (depressão e ansiedade) (influencia neurotransmissores como dopamina e serotonina; baixos níveis estão associados a um maior risco de sintomas depressivos e ansiosos); Comprometimento da saúde mitocondrial (pode afetar a função mitocondrial, resultando em menor eficiência metabólica e aumento da produção de radicais livres, contribuindo para o envelhecimento celular); Aumento do estresse oxidativo e inflamação sistêmica (ela possui propriedades antioxidantes; sua deficiência pode aumentar o dano oxidativo e favorecer processos inflamatórios crônicos); Prejuízo na sensibilidade à insulina e maior risco metabólico (pode comprometer a regulação da glicose e aumentar o risco de resistência à insulina e diabetes tipo 2)., Excesso de sonolência e fadiga excessiva (promove maior indução ao sono, podendo causar sonolência diurna intensa e fadiga constante); Redução da pressão arterial e episódios de hipotensão (a adenosina é um potente vasodilatador; níveis elevados podem levar a quedas de pressão arterial, tontura e desmaios em alguns casos); Bradicardia e redução do ritmo cardíaco (atua na regulação da frequência cardíaca; altos níveis podem levar à bradicardia, sensação de fraqueza e risco de síncope em indivíduos predispostos); Maior propensão a cefaleias e enxaquecas (a adenosina tem um papel na dilatação dos vasos cerebrais; sua elevação excessiva pode desencadear dores de cabeça e enxaquecas frequentes); Redução da excitabilidade neural e déficit cognitivo (pode inibir excessivamente a atividade neuronal, causando lentificação do raciocínio, dificuldade de concentração e sensação de “mente nebulosa”); Diminuição da capacidade de resposta ao estresse (a adenosina modula a liberação de catecolaminas; quando em excesso, pode reduzir a resposta ao estresse e causar sensação de apatia e falta de motivação); Possível supressão do sistema imune (atua na modulação da resposta imune; níveis elevados podem levar a uma imunossupressão leve, aumentando o risco de infecções em alguns indivíduos)., Fadiga e redução da resistência física (a isoleucina é um aminoácido essencial envolvido na produção de energia muscular, e sua deficiência pode comprometer a resistência ao exercício e a recuperação pós-esforço); Fraqueza muscular e perda de massa magra (pode prejudicar a síntese proteica e a manutenção da massa muscular, levando a atrofia muscular e dificuldade na recuperação pós-exercício); Alterações na regulação da glicose e maior risco de hipoglicemia (podendo levar a níveis instáveis de açúcar no sangue, causando tontura, tremores e confusão mental); Dificuldade na regeneração e reparação tecidual (pode levar a uma regeneração mais lenta de tecidos lesionados); Deficiência na regulação da imunidade (pode comprometer a resposta imunológica e aumentar a susceptibilidade a infecções); Déficits cognitivos e problemas de concentração (pode afetar a neurotransmissão e o metabolismo cerebral, levando a dificuldades cognitivas, falta de foco e menor desempenho mental); Dificuldade na regulação do metabolismo lipídico (a isoleucina auxilia na oxidação de gorduras e pode levar ao acúmulo de lipídios no fígado e no tecido adiposo, contribuindo para resistência à insulina e obesidade); Diminuição da regulação da temperatura corporal (a isoleucina influencia o metabolismo energético, e sua deficiência pode comprometer a termorregulação, resultando em sensibilidade ao frio e dificuldade de adaptação térmica)., Aumento do risco de resistência à insulina (excesso de leucina pode sobrecarregar a via de sinalização da insulina, reduzindo sua eficácia e contribuindo para resistência à insulina e síndrome metabólica); Sobrecarga hepática e renal (pela conversão excessiva de leucina em metabólitos nitrogenados e amônia, aumentando o esforço do fígado e rins para sua eliminação); Diminuição da captação de outros aminoácidos essenciais (como triptofano e fenilalanina, devido à competição pelo transporte através da barreira hematoencefálica, podendo afetar a síntese de serotonina e dopamina) - levando a alterações no humor, sono e cognição; Possível relação com neurotoxicidade e alteração da sinalização de neurotransmissores (pode interferir no equilíbrio entre glutamato e GABA, potencialmente impactando a função cerebral e aumentando o risco de transtornos neurológicos); Desbalanço na produção de energia e acúmulo de metabólitos intermediários (pode gerar sobrecarga no metabolismo energético, levando ao acúmulo de ácidos orgânicos como o isovalerato, que pode ser tóxico em altas concentrações); Alteração na expressão da via mTOR e risco de proliferação celular exacerbada (por estimular excessivamente a via de crescimento celular, podendo estar associado ao aumento do risco de certas condições metabólicas e cânceres); Diminuição da autofagia e reciclagem celular (pode inibir processos de degradação celular essenciais para a renovação de organelas e proteínas danificadas) - contribuindo para o envelhecimento celular e acúmulo de danos oxidativos; Alterações no metabolismo lipídico e aumento do risco de dislipidemia (excesso de leucina pode modular vias metabólicas que favorecem a lipogênese, contribuindo para acúmulo de gordura hepática e elevação de triglicerídeos e colesterol)., Déficit na produção de energia (ATP) (menor disponibilidade de piruvato reduz o fluxo para o ciclo de Krebs e a geração de ATP, resultando em menor eficiência metabólica); Fadiga crônica e redução da resistência física (comprometimento na produção de energia leva a menor tolerância ao esforço físico e maior fadiga muscular); Hipoglicemia e dificuldade na regulação glicêmica (pode indicar menor conversão de glicose em energia, levando a episódios de hipoglicemia e instabilidade glicêmica); Fraqueza muscular e cãibras (redução da energia celular afeta a contração e recuperação muscular); Disfunção neurológica e dificuldade cognitiva ( afeta a função neuronal, podendo causar névoa mental, lapsos de memória e dificuldade de concentração); Acidose láctica em casos de deficiência na conversão de piruvato (como em distúrbios genéticos da piruvato desidrogenase); Menor resistência ao estresse oxidativo (piruvato tem propriedades antioxidantes, e sua deficiência pode levar a maior vulnerabilidade ao dano oxidativo); Prejuízo na síntese de neurotransmissores (piruvato é um precursor indireto de acetil-CoA, essencial para a produção de neurotransmissores como acetilcolina)., Alterações neurológicas (agitação; irritabilidade; dificuldade de concentração devido ao impacto no equilíbrio de neurotransmissores excitatórios); Distúrbios gastrointestinais (náuseas; desconforto digestivo; possível diarreia em casos extremos); Desequilíbrios no metabolismo de aminoácidos (interferência na absorção de outros aminoácidos como triptofano e tirosina, podendo impactar a síntese de serotonina e dopamina); Alterações na regulação da glicose (possível impacto na resistência à insulina, devido à interação com vias metabólicas energéticas); Sobrecarga renal e hepática (metabolismo excessivo de valina pode aumentar a demanda sobre rins e fígado, especialmente em indivíduos com disfunções pré-existentes); Desbalanço no Equilíbrio de BCAAs (desequilíbrio com leucina e isoleucina, podendo afetar a homeostase muscular e energética).\nSuplementos recomendados pelo KG: Acetil-L-Carnitina; L-Carnitina (se necessário); Cofatores: Vitamina C, Vitamina B6 (P-5-P), Vitamina B3 (niacinamida ou NAD precursor); Ferro (se ferritina < 40 ng/mL): bisglicinato ou quelato; Lisina, se necessário. Apoio mitocondrial: CoQ10 (ubiquinol); Ácido alfa-lipóico; PQQ, NAC, resveratrol (se indicado). A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ACETIL-L-CARNITINA), Cafeína (com cautela): antagonista competitivo dos receptores de adenosina A1 e A2A — pode reduzir os efeitos indesejados do excesso; Vitamina C: suporte ao controle do estresse oxidativo (que estimula liberação de ATP/adenosina); Riboflavina (B2), niacina (B3) e CoQ10: suporte à cadeia transportadora de elétrons e produção de ATP. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ADENOSINA), BCAA ou isoleucina isolada ou Whey protein (rico em BCAAs naturalmente); Melhoria da digestão: HCl betaina ou enzimas digestivas, se necessário; Aminoácidos essenciais combinados (EAAs) — se o quadro for crônico ou catabólico; Cofatores: Magnésio, B6, B12, zinco; Suporte intestinal: glutamina, probióticos. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para ISOLEUCINA), Reduzir suplementação de BCAAs ou leucina; Suporte ao metabolismo de BCAAs: B6 (P-5-P), B1, B2, B3, Ácido lipóico, Magnésio (malato, glicina), zinco; Suporte mitocondrial para degradação de BCAAs: CoQ10, carnitina, ácido alfa-lipoico. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para LEUCINA), Suporte à glicólise e piruvato: Vitaminas B1, B2, B3 (niacinamida), B6 ativa (P-5-P), Magnésio; Suporte mitocondrial (para que o piruvato seja eficientemente oxidado): CoQ10, ácido alfa-lipóico, carnitina, NAC, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para PIRUVATO), Estimular o metabolismo de valina: Vitaminas: B6 (P-5-P), B1 (tiamina), biotina; Magnésio (essencial para descarboxilação enzimática); L-carnitina (suporte à oxidação mitocondrial de aminoácidos). Suporte mitocondrial: CoQ10, ácido alfa-lipoico, NADH, creatina. A individualização da suplementação deve ser feita com base nas necessidades e condições clínicas do paciente levando em consideração a análise integrada do teste metabólico. (para VALINA)\nAlimentos recomendados pelo KG: Fontes de L-carnitina: Carnes magras (carne bovina, frango, peixe), especialmente carne vermelha, para fornecer o precursor deste metabólito (ALCAR); Alimentos ricos em antioxidantes: Frutas vermelhas, espinafre, brócolis, cenouras, que protegem contra o estresse oxidativo e melhoram a função celular; Fontes de vitamina C e E: Frutas cítricas, pimentões, morangos, abacates, nozes e sementes para proteger as células nervosas e mitocôndrias; Fontes de ômega-3: Peixes gordurosos (salmão, sardinha, cavala), chia e linhaça para reduzir inflamação e promover a saúde cerebral; Vitaminas do complexo B: Ovos, peixe, carne magra, legumes, que são cruciais para o metabolismo energético e a produção de neurotransmissores; Ácidos graxos monoinsaturados: Azeite de oliva, abacate, e nozes, que promovem a função mitocondrial e reduzem o estresse oxidativo. Evitar: Excesso de alimentos ultraprocessados, ricos em gorduras trans e aditivos artificiais, que podem prejudicar a função mitocondrial; Deficiência de proteínas na dieta, que pode afetar a produção de carnitina e ALCAR; Excesso de açúcar refinado, que pode sobrecarregar as mitocôndrias e gerar radicais livres. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ACETIL-L-CARNITINA), Fontes de antioxidantes para reduzir o estresse oxidativo, como frutas e vegetais frescos (cabelos vermelhos, cenouras, tomates, pepinos, brócolis); Ácidos graxos saudáveis: Azeite de oliva, abacate, peixes gordurosos (salmão, sardinha), que ajudam a reduzir inflamação e melhorar a circulação; Alimentos ricos em magnésio: Espinafre, amêndoas, abacate, bananas para equilibrar os efeitos da adenosina sobre o sistema cardiovascular; Probiotics e prebióticos: Alimentos fermentados, como iogurte natural, kefir e alimentos ricos em fibras, para reduzir a inflamação e melhorar a saúde intestinal. Evitar: Estímulos vasodilatadores excessivos, como cafeína ou suplementos energéticos, que podem elevar os níveis de adenosina de forma indesejada; Alimentos ultraprocessados, ricos em aditivos e conservantes que podem aumentar a inflamação e comprometer a função cardiovascular; Excessiva exposição ao estresse e insônia, que pode causar um desequilíbrio na modulação de adenosina. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ADENOSINA), Fontes de proteínas completas, como carnes magras (frango, peixe, carne bovina magra), ovos, leite e derivados, que fornecem todos os aminoácidos essenciais, incluindo isoleucina; Leguminosas e grãos, como feijão, lentilhas, quinoa e grão-de-bico, que são fontes vegetais de proteínas e aminoácidos essenciais; Fontes de vitamina B6 e B12, como ovos, fígado, peixe, carnes e vegetais verdes, que ajudam na metabolização adequada de aminoácidos; Carboidratos complexos como batata-doce, quinoa e aveia, para fornecer energia contínua e otimizar a utilização de aminoácidos no corpo; Alimentos ricos em antioxidantes, como frutas vermelhas e chá verde, para ajudar na recuperação celular e mitocondrial após exercícios. Evitar: Dietas veganas ou vegetarianas restritivas sem um planejamento adequado, pois podem levar a deficiências de aminoácidos essenciais, incluindo a isoleucina; Excessos de alimentos processados e ricos em gorduras trans, que prejudicam a absorção de nutrientes e podem afetar o metabolismo energético; Dieta desequilibrada em carboidratos, que pode impactar negativamente na recuperação muscular e na utilização de aminoácidos. Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para ISOLEUCINA), Vegetais crucíferos, cúrcuma e alimentos anti-inflamatórios (melhoram sensibilidade anabólica). Alimentos ricos em magnésio, zinco e B6 (cofatores do metabolismo proteico). Fontes de carboidrato de baixo índice glicêmico (melhora captação muscular). Evitar em excesso: Suplementos de leucina/BCAA isolados sem indicação. Dietas hiperproteicas mal planejadas. Jejuns longos + treinos extenuantes (aumentam degradação muscular). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para LEUCINA), Fontes complexas de carboidratos: batata-doce, inhame, quinoa, arroz integral, aveia. Frutas com baixo índice glicêmico: maçã, frutas vermelhas, pêssego, kiwi. Fontes de vitamina B3, B6, cromo: ovos, peixes, levedura nutricional, banana. Sementes e oleaginosas (fornecem cofatores + energia estável). Evitar: Dietas muito restritivas ou cetogênicas sem controle clínico. Consumo muito baixo de carboidratos (<40g/dia) por períodos prolongados. Uso excessivo de estimulantes (cafeína, pré-treinos) com baixa energia basal. (para PIRUVATO), Reduzir ingestão/suplementação de BCAAs; Ajustar ingestão proteica total, se desbalanceada; Evitar carnes vermelhas e processadas; Incluir fontes vegetais de proteína (feijão, lentilhas, grão-de-bico, tofu, quinoa, arroz integral); Aumentar o consumo de frutas, vegetais e grãos integrais para melhorar o metabolismo; Evitar alimentos com alto índice glicêmico; Aumentar a ingestão de antioxidantes (alimentos ricos em vitaminas C e E, como frutas cítricas, pimentões, frutas vermelhas). Manter uma hidratação adequada; Evitar o uso excessivo de álcool e tabaco; Gerenciar o estresse e praticar exercícios físicos regulares. Além de realizar investigação médica para causas subjacentes. (para VALINA)\n\n\n# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"findings\": {\n    \"items\": [\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n        \"metabolite\": \"Acetil-L-Carnitina\",\n        \"implications\": [\n          \"Fadiga crônica e baixa energia\",\n          \"Fraqueza muscular e redução da performance física\",\n          \"Comprometimento da saúde mitocondrial\",\n          \"Aumento do estresse oxidativo e inflamação sistêmica\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n        \"metabolite\": \"Adenosina\",\n        \"implications\": [\n          \"Redução da resposta ao estresse e apatia\",\n          \"Bradicardia e hipotensão potencial\",\n          \"Maior predisposição a cefaleias e distúrbios do humor\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n        \"metabolite\": \"Isoleucina\",\n        \"implications\": [\n          \"Fraqueza muscular e perda de massa magra\",\n          \"Dificuldade na regeneração tecidual\",\n          \"Alterações na regulação da glicose\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n        \"metabolite\": \"Leucina\",\n        \"implications\": [\n          \"Aumento do risco de resistência à insulina\",\n          \"Desbalanço na produção de energia celular\",\n          \"Alteração na função anabólica e catabólica do músculo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n        \"metabolite\": \"Piruvato\",\n        \"implications\": [\n          \"Fadiga crônica e redução da resistência física\",\n          \"Disfunção neurológica e dificuldade cognitiva\",\n          \"Menor resistência ao estresse oxidativo\"\n        ]\n      },\n      {\n        \"status\": \"alterado\",\n        \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n        \"metabolite\": \"Valina\",\n        \"implications\": [\n          \"Desbalanço no Equilíbrio de BCAAs\",\n          \"Sobrecarga renal e hepática\",\n          \"Alterações na regulação do metabolismo lipídico\"\n        ]\n      }\n    ],\n    \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n  },\n  \"diet_suggestions\": {\n    \"carnivoro_onivoro\": [\n      \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n      \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n      \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n      \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n      \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n      \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n      \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n    ],\n    \"vegetariano\": [],\n    \"vegano\": []\n  },\n  \"supplements\": {\n    \"items\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ]\n  },\n  \"training\": {\n    \"recommendations\": [\n      \"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\n      \"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\n      \"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\n      \"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\n      \"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"\n    ],\n    \"avoid\": [\n      \"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\n      \"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\n      \"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"\n    ],\n    \"focus\": \"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"\n  }\n}\n\nCrie um resumo em formato de prosa narrativa, dividido em 4 parágrafos:\n        1) Visão geral com dados relevantes do perfil clínico, hábitos e contexto, utilizando tom impessoal (ex: \"observa-se\", \"nota-se\", \"considerando-se\").\n        2) Interpretação sobre o laudo metabólico e achados principais, focando nas alterações identificadas e seus impactos, sem detalhar intervenções específicas.\n        3) Diretrizes gerais de intervenção integrando alimentação, suplementação e treino de forma contextualizada, evitando detalhamentos que serão abordados em seções posteriores.\n        4) Conclusão destacando o objetivo estabelecido e a importância da abordagem integrada para os resultados esperados.\n\n        Mantenha tom impessoal e orientado ao leitor. Contextualize sempre o objetivo clínico identificado. Evite antecipar detalhes específicos de condutas que serão desenvolvidos nas próximas seções. Não use listas ou markdown; mantenha texto contínuo em parágrafos claros e bem estruturados."
    }
  ],
  "temperature": 1.0,
  "max_tokens": 4058,
  "response_format": "<class 'app.domain.report.SummaryContent'>"
}
```
- **Outputs:**
```json
{
  "id": "gen-1757099094-akJmVzFhT0AkjPCIWItb",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "{\"content\":\"Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\\n\\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\\n\\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\\n\\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\"}",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "parsed": {
          "content": "Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas."
        },
        "reasoning": null
      },
      "native_finish_reason": "stop"
    }
  ],
  "created": 1757099094,
  "model": "openai/gpt-4o-mini",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_8bda4d3a2c",
  "usage": {
    "completion_tokens": 514,
    "prompt_tokens": 7043,
    "total_tokens": 7557,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "provider": "OpenAI"
}
```

---

### 22. call_llm_api_6
- **Type:** `llm`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `d280763c8298c2da`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "mlflow.spanFunctionName": "call_llm_api",
  "mlflow.spanType": "llm"
}
```
- **Inputs:**
```json
{
  "user_prompt": "# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"final_report\": {\n    \"report_id\": \"vida_PP032_20250905_190423\",\n    \"patient_id\": \"PP032\",\n    \"anamnesis_id\": \"anam_PP032_20250905\",\n    \"exam_id\": \"exam_PP032_20250814\",\n    \"version\": \"1.0\",\n    \"timestamp\": \"2025-09-05T19:04:23.061565\",\n    \"summary\": {\n      \"content\": \"Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\\n\\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\\n\\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\\n\\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\"\n    },\n    \"findings\": {\n      \"items\": [\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n          \"metabolite\": \"Acetil-L-Carnitina\",\n          \"implications\": [\n            \"Fadiga crônica e baixa energia\",\n            \"Fraqueza muscular e redução da performance física\",\n            \"Comprometimento da saúde mitocondrial\",\n            \"Aumento do estresse oxidativo e inflamação sistêmica\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n          \"metabolite\": \"Adenosina\",\n          \"implications\": [\n            \"Redução da resposta ao estresse e apatia\",\n            \"Bradicardia e hipotensão potencial\",\n            \"Maior predisposição a cefaleias e distúrbios do humor\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n          \"metabolite\": \"Isoleucina\",\n          \"implications\": [\n            \"Fraqueza muscular e perda de massa magra\",\n            \"Dificuldade na regeneração tecidual\",\n            \"Alterações na regulação da glicose\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n          \"metabolite\": \"Leucina\",\n          \"implications\": [\n            \"Aumento do risco de resistência à insulina\",\n            \"Desbalanço na produção de energia celular\",\n            \"Alteração na função anabólica e catabólica do músculo\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n          \"metabolite\": \"Piruvato\",\n          \"implications\": [\n            \"Fadiga crônica e redução da resistência física\",\n            \"Disfunção neurológica e dificuldade cognitiva\",\n            \"Menor resistência ao estresse oxidativo\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n          \"metabolite\": \"Valina\",\n          \"implications\": [\n            \"Desbalanço no Equilíbrio de BCAAs\",\n            \"Sobrecarga renal e hepática\",\n            \"Alterações na regulação do metabolismo lipídico\"\n          ]\n        }\n      ],\n      \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n    },\n    \"diet_suggestions\": {\n      \"carnivoro_onivoro\": [\n        \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n        \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n        \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n        \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n        \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n        \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n        \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n      ],\n      \"vegetariano\": [],\n      \"vegano\": []\n    },\n    \"supplements\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ],\n    \"training\": {\n      \"recommendations\": [\n        \"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\n        \"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\n        \"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\n        \"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\n        \"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"\n      ],\n      \"avoid\": [\n        \"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\n        \"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\n        \"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"\n      ],\n      \"focus\": \"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"\n    }\n  }\n}\n\n# OBJETIVO\n    Crie um relatório de performance em formato markdown, utilizando os dados do JSON fornecido em \"CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\".\n\n    **Use EXATAMENTE a seguinte estrutura e títulos:**\n\n\n    # RELATÓRIO FINAL - Vida Nova\n\n    (Cri um texto introdutório de `summary.content` do JSON como o texto principal aqui)\n\n    ---\n\n    ## Sugestão Alimentar\n    (Use o conteúdo da seção `diet_suggestions` para criar uma visão consolidada e direta das recomendações alimentares, formatando cada recomendação como um item de lista simples com \"-\" para melhor legibilidade)\n\n    ---\n\n    ## Suplementação Sugerida\n    (Liste cada suplemento da seção `supplements`, formatando com nome em negrito e os demais campos como tópicos)\n\n    ---\n\n    ## Dica de Treino\n    (Use o conteúdo da seção `training` para descrever as recomendações, o que evitar e o foco)\n    ",
  "schema": null,
  "system_prompt": "Você é um especialista em comunicação médica e formatação de relatórios de performance (Vida Nova) em markdown.\n    Sua tarefa é usar os dados estruturados de um paciente para criar um relatório claro, profissional e focado em performance, seguindo uma estrutura pré-definida.\n    A linguagem deve ser técnica, mas acessível. O output deve ser unicamente o relatório em markdown.",
  "temperature": 1.0,
  "max_tokens": 4058,
  "kwargs": {}
}
```
- **Outputs:**
```json
# RELATÓRIO FINAL - Vida Nova

Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.

A análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.

Integrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.

Em conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.

---

## Sugestão Alimentar
- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.
- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.
- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.
- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.
- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.
- Frutas vermelhas (morango, framboesa): Fonte de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.
- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.

---

## Suplementação Sugerida
- **Acetil-L-Carnitina**
  - Dosagem: 1g a 2g
  - Frequência: Diário, antes do treino
  - Propósito: Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.
  - Observação: Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.

- **L-Carnitina**
  - Dosagem: 500mg a 1g
  - Frequência: Diário, se necessário
  - Propósito: Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.
  - Observação: Avaliar a necessidade com base no nível de atividade física e fadiga.

- **Cofatores: Vitamina C**
  - Dosagem: 500mg
  - Frequência: Diário
  - Propósito: Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.
  - Observação: Monitorar a ingestão de antioxidantes na dieta.

- **Cofatores: Vitamina B6 (P-5-P)**
  - Dosagem: 10mg - 25mg
  - Frequência: Diário
  - Propósito: Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.
  - Observação: Importante para a adequada metabolização da isoleucina.

- **Cofatores: Vitamina B3 (niacinamida ou NAD precursor)**
  - Dosagem: 300mg
  - Frequência: Diário
  - Propósito: Suporte à produção de energia e otimização do metabolismo.
  - Observação: Pode auxiliar na regulação do metabolismo energético.

- **CoQ10 (ubiquinol)**
  - Dosagem: 100mg a 300mg
  - Frequência: Diário
  - Propósito: Promover a saúde mitocondrial e aumentar a produção de ATP.
  - Observação: Avaliar a resposta do paciente ao suporte mitocondrial.

- **Ácido Alfa-Lipóico**
  - Dosagem: 300mg
  - Frequência: Diário
  - Propósito: Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.
  - Observação: Considerar a relação com o excesso de leucina.

- **Complexo de Vitaminas do grupo B (incluindo B6, B12)**
  - Dosagem: Recomendações diárias específicas.
  - Frequência: Diário
  - Propósito: Apoio geral ao metabolismo energético e recuperação muscular.
  - Observação: Incluir como um suporte contínuo através de uma dieta equilibrada.

- **Glutamina**
  - Dosagem: 5g
  - Frequência: Diário, especialmente após exercícios
  - Propósito: Apoio à recuperação muscular e manutenção da integridade intestinal.
  - Observação: Considerar a saúde intestinal do paciente.

- **Whey Protein (rico em BCAAs)**
  - Dosagem: 20g a 30g
  - Frequência: Após o treino
  - Propósito: Promover a síntese proteica e a recuperação muscular.
  - Observação: Importante para a melhoria dos níveis críticos de isoleucina.

---

## Dica de Treino
- Recomendações:
  - Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.
  - Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.
  - Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).
  - Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.
  - Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.

- Evitar:
  - Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.
  - Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.
  - Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.

- Foco: Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.
```

---

### 23. AsyncCompletions_6
- **Type:** `CHAT_MODEL`
- **State:** `SpanStatus(status_code=<SpanStatusCode.OK: 'OK'>, description='')`
- **Parent:** `58ca3707eca07c17`
- **Attributes:**
```json
{
  "mlflow.traceRequestId": "d9de4018c1154fe8af66ec56a3bb902c",
  "model": "openai/gpt-4o-mini",
  "temperature": 1.0,
  "mlflow.chat.messages": [
    {
      "role": "system",
      "content": "Você é um especialista em comunicação médica e formatação de relatórios de performance (Vida Nova) em markdown.\n    Sua tarefa é usar os dados estruturados de um paciente para criar um relatório claro, profissional e focado em performance, seguindo uma estrutura pré-definida.\n    A linguagem deve ser técnica, mas acessível. O output deve ser unicamente o relatório em markdown."
    },
    {
      "role": "user",
      "content": "# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"final_report\": {\n    \"report_id\": \"vida_PP032_20250905_190423\",\n    \"patient_id\": \"PP032\",\n    \"anamnesis_id\": \"anam_PP032_20250905\",\n    \"exam_id\": \"exam_PP032_20250814\",\n    \"version\": \"1.0\",\n    \"timestamp\": \"2025-09-05T19:04:23.061565\",\n    \"summary\": {\n      \"content\": \"Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\\n\\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\\n\\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\\n\\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\"\n    },\n    \"findings\": {\n      \"items\": [\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n          \"metabolite\": \"Acetil-L-Carnitina\",\n          \"implications\": [\n            \"Fadiga crônica e baixa energia\",\n            \"Fraqueza muscular e redução da performance física\",\n            \"Comprometimento da saúde mitocondrial\",\n            \"Aumento do estresse oxidativo e inflamação sistêmica\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n          \"metabolite\": \"Adenosina\",\n          \"implications\": [\n            \"Redução da resposta ao estresse e apatia\",\n            \"Bradicardia e hipotensão potencial\",\n            \"Maior predisposição a cefaleias e distúrbios do humor\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n          \"metabolite\": \"Isoleucina\",\n          \"implications\": [\n            \"Fraqueza muscular e perda de massa magra\",\n            \"Dificuldade na regeneração tecidual\",\n            \"Alterações na regulação da glicose\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n          \"metabolite\": \"Leucina\",\n          \"implications\": [\n            \"Aumento do risco de resistência à insulina\",\n            \"Desbalanço na produção de energia celular\",\n            \"Alteração na função anabólica e catabólica do músculo\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n          \"metabolite\": \"Piruvato\",\n          \"implications\": [\n            \"Fadiga crônica e redução da resistência física\",\n            \"Disfunção neurológica e dificuldade cognitiva\",\n            \"Menor resistência ao estresse oxidativo\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n          \"metabolite\": \"Valina\",\n          \"implications\": [\n            \"Desbalanço no Equilíbrio de BCAAs\",\n            \"Sobrecarga renal e hepática\",\n            \"Alterações na regulação do metabolismo lipídico\"\n          ]\n        }\n      ],\n      \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n    },\n    \"diet_suggestions\": {\n      \"carnivoro_onivoro\": [\n        \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n        \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n        \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n        \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n        \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n        \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n        \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n      ],\n      \"vegetariano\": [],\n      \"vegano\": []\n    },\n    \"supplements\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ],\n    \"training\": {\n      \"recommendations\": [\n        \"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\n        \"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\n        \"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\n        \"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\n        \"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"\n      ],\n      \"avoid\": [\n        \"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\n        \"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\n        \"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"\n      ],\n      \"focus\": \"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"\n    }\n  }\n}\n\n# OBJETIVO\n    Crie um relatório de performance em formato markdown, utilizando os dados do JSON fornecido em \"CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\".\n\n    **Use EXATAMENTE a seguinte estrutura e títulos:**\n\n\n    # RELATÓRIO FINAL - Vida Nova\n\n    (Cri um texto introdutório de `summary.content` do JSON como o texto principal aqui)\n\n    ---\n\n    ## Sugestão Alimentar\n    (Use o conteúdo da seção `diet_suggestions` para criar uma visão consolidada e direta das recomendações alimentares, formatando cada recomendação como um item de lista simples com \"-\" para melhor legibilidade)\n\n    ---\n\n    ## Suplementação Sugerida\n    (Liste cada suplemento da seção `supplements`, formatando com nome em negrito e os demais campos como tópicos)\n\n    ---\n\n    ## Dica de Treino\n    (Use o conteúdo da seção `training` para descrever as recomendações, o que evitar e o foco)\n    "
    },
    {
      "content": "# RELATÓRIO FINAL - Vida Nova\n\nObserva-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\n\n---\n\n## Sugestão Alimentar\n- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\n- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\n- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\n- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\n- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\n- Frutas vermelhas (morango, framboesa): Fonte de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\n- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\n\n---\n\n## Suplementação Sugerida\n- **Acetil-L-Carnitina**\n  - Dosagem: 1g a 2g\n  - Frequência: Diário, antes do treino\n  - Propósito: Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\n  - Observação: Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\n  \n- **L-Carnitina**\n  - Dosagem: 500mg a 1g\n  - Frequência: Diário, se necessário\n  - Propósito: Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\n  - Observação: Avaliar a necessidade com base no nível de atividade física e fadiga.\n\n- **Cofatores: Vitamina C**\n  - Dosagem: 500mg\n  - Frequência: Diário\n  - Propósito: Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\n  - Observação: Monitorar a ingestão de antioxidantes na dieta.\n\n- **Cofatores: Vitamina B6 (P-5-P)**\n  - Dosagem: 10mg - 25mg\n  - Frequência: Diário\n  - Propósito: Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\n  - Observação: Importante para a adequada metabolização da isoleucina.\n\n- **Cofatores: Vitamina B3 (niacinamida ou NAD precursor)**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Suporte à produção de energia e otimização do metabolismo.\n  - Observação: Pode auxiliar na regulação do metabolismo energético.\n\n- **CoQ10 (ubiquinol)**\n  - Dosagem: 100mg a 300mg\n  - Frequência: Diário\n  - Propósito: Promover a saúde mitocondrial e aumentar a produção de ATP.\n  - Observação: Avaliar a resposta do paciente ao suporte mitocondrial.\n\n- **Ácido Alfa-Lipóico**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\n  - Observação: Considerar a relação com o excesso de leucina.\n\n- **Complexo de Vitaminas do grupo B (incluindo B6, B12)**\n  - Dosagem: Recomendações diárias específicas.\n  - Frequência: Diário\n  - Propósito: Apoio geral ao metabolismo energético e recuperação muscular.\n  - Observação: Incluir como um suporte contínuo através de uma dieta equilibrada.\n\n- **Glutamina**\n  - Dosagem: 5g\n  - Frequência: Diário, especialmente após exercícios\n  - Propósito: Apoio à recuperação muscular e manutenção da integridade intestinal.\n  - Observação: Considerar a saúde intestinal do paciente.\n\n- **Whey Protein (rico em BCAAs)**\n  - Dosagem: 20g a 30g\n  - Frequência: Após o treino\n  - Propósito: Promover a síntese proteica e a recuperação muscular.\n  - Observação: Importante para a melhoria dos níveis críticos de isoleucina.\n\n---\n\n## Dica de Treino\n- Recomendações:\n  - Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\n  - Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\n  - Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\n  - Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\n  - Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\n\n- Evitar:\n  - Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\n  - Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\n  - Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\n\n- Foco: Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.",
      "refusal": null,
      "role": "assistant",
      "reasoning": null
    }
  ],
  "max_tokens": 4058,
  "mlflow.spanType": "CHAT_MODEL",
  "mlflow.chat.tokenUsage": {
    "input_tokens": 3208,
    "output_tokens": 1922,
    "total_tokens": 5130
  }
}
```
- **Inputs:**
```json
{
  "model": "openai/gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Você é um especialista em comunicação médica e formatação de relatórios de performance (Vida Nova) em markdown.\n    Sua tarefa é usar os dados estruturados de um paciente para criar um relatório claro, profissional e focado em performance, seguindo uma estrutura pré-definida.\n    A linguagem deve ser técnica, mas acessível. O output deve ser unicamente o relatório em markdown."
    },
    {
      "role": "user",
      "content": "# CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\n{\n  \"final_report\": {\n    \"report_id\": \"vida_PP032_20250905_190423\",\n    \"patient_id\": \"PP032\",\n    \"anamnesis_id\": \"anam_PP032_20250905\",\n    \"exam_id\": \"exam_PP032_20250814\",\n    \"version\": \"1.0\",\n    \"timestamp\": \"2025-09-05T19:04:23.061565\",\n    \"summary\": {\n      \"content\": \"Observa-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\\n\\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\\n\\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\\n\\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\"\n    },\n    \"findings\": {\n      \"items\": [\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Níveis de Acetil-L-Carnitina estão reduzidos. O ALCAR é fundamental no transporte de ácidos graxos para as mitocôndrias, crucial para a produção de ATP e desempenho muscular.\",\n          \"metabolite\": \"Acetil-L-Carnitina\",\n          \"implications\": [\n            \"Fadiga crônica e baixa energia\",\n            \"Fraqueza muscular e redução da performance física\",\n            \"Comprometimento da saúde mitocondrial\",\n            \"Aumento do estresse oxidativo e inflamação sistêmica\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Adenosina estão elevados. A adenosina regula diversas funções, incluindo a modulação da frequência cardíaca e a resposta ao estresse.\",\n          \"metabolite\": \"Adenosina\",\n          \"implications\": [\n            \"Redução da resposta ao estresse e apatia\",\n            \"Bradicardia e hipotensão potencial\",\n            \"Maior predisposição a cefaleias e distúrbios do humor\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"A Isoleucina está em nível crítico, o que pode comprometer a síntese proteica e a recuperação muscular.\",\n          \"metabolite\": \"Isoleucina\",\n          \"implications\": [\n            \"Fraqueza muscular e perda de massa magra\",\n            \"Dificuldade na regeneração tecidual\",\n            \"Alterações na regulação da glicose\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Leucina estão excessivos, o que pode sobrecarregar a via de sinalização da insulina.\",\n          \"metabolite\": \"Leucina\",\n          \"implications\": [\n            \"Aumento do risco de resistência à insulina\",\n            \"Desbalanço na produção de energia celular\",\n            \"Alteração na função anabólica e catabólica do músculo\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Piruvato estão reduzidos. Um menor fluxo para o ciclo de Krebs pode prejudicar a produção de energia.\",\n          \"metabolite\": \"Piruvato\",\n          \"implications\": [\n            \"Fadiga crônica e redução da resistência física\",\n            \"Disfunção neurológica e dificuldade cognitiva\",\n            \"Menor resistência ao estresse oxidativo\"\n          ]\n        },\n        {\n          \"status\": \"alterado\",\n          \"description\": \"Os níveis de Valina estão elevados, o que pode comprometer o equilíbrio do metabolismo de BCAAs.\",\n          \"metabolite\": \"Valina\",\n          \"implications\": [\n            \"Desbalanço no Equilíbrio de BCAAs\",\n            \"Sobrecarga renal e hepática\",\n            \"Alterações na regulação do metabolismo lipídico\"\n          ]\n        }\n      ],\n      \"conclusion\": \"Os achados indicam um desequilíbrio no perfil de aminoácidos e metabólitos fundamentais para a energia, desempenho físico e bem-estar mental. É necessário implementar um protocolo de suplementação e ajustes dietéticos focados na melhoria da função mitocondrial, na regulação da insulina e na recuperação muscular.\"\n    },\n    \"diet_suggestions\": {\n      \"carnivoro_onivoro\": [\n        \"- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\",\n        \"- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\",\n        \"- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\",\n        \"- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\",\n        \"- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\",\n        \"- Frutas vermelhas (morango, framboesa): Fontes de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\",\n        \"- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\"\n      ],\n      \"vegetariano\": [],\n      \"vegano\": []\n    },\n    \"supplements\": [\n      {\n        \"name\": \"Acetil-L-Carnitina\",\n        \"dosage\": \"1g a 2g\",\n        \"frequency\": \"Diário, antes do treino\",\n        \"purpose\": \"Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\",\n        \"observation\": \"Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\"\n      },\n      {\n        \"name\": \"L-Carnitina\",\n        \"dosage\": \"500mg a 1g\",\n        \"frequency\": \"Diário, se necessário\",\n        \"purpose\": \"Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\",\n        \"observation\": \"Avaliar a necessidade com base no nível de atividade física e fadiga.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina C\",\n        \"dosage\": \"500mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\",\n        \"observation\": \"Monitorar a ingestão de antioxidantes na dieta.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B6 (P-5-P)\",\n        \"dosage\": \"10mg - 25mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\",\n        \"observation\": \"Importante para a adequada metabolização da isoleucina.\"\n      },\n      {\n        \"name\": \"Cofatores: Vitamina B3 (niacinamida ou NAD precursor)\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Suporte à produção de energia e otimização do metabolismo.\",\n        \"observation\": \"Pode auxiliar na regulação do metabolismo energético.\"\n      },\n      {\n        \"name\": \"CoQ10 (ubiquinol)\",\n        \"dosage\": \"100mg a 300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Promover a saúde mitocondrial e aumentar a produção de ATP.\",\n        \"observation\": \"Avaliar a resposta do paciente ao suporte mitocondrial.\"\n      },\n      {\n        \"name\": \"Ácido Alfa-Lipóico\",\n        \"dosage\": \"300mg\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\",\n        \"observation\": \"Considerar a relação com o excesso de leucina.\"\n      },\n      {\n        \"name\": \"Complexo de Vitaminas do grupo B (incluindo B6, B12)\",\n        \"dosage\": \"Recomendações diárias específicas.\",\n        \"frequency\": \"Diário\",\n        \"purpose\": \"Apoio geral ao metabolismo energético e recuperação muscular.\",\n        \"observation\": \"Incluir como um suporte contínuo através de uma dieta equilibrada.\"\n      },\n      {\n        \"name\": \"Glutamina\",\n        \"dosage\": \"5g\",\n        \"frequency\": \"Diário, especialmente após exercícios\",\n        \"purpose\": \"Apoio à recuperação muscular e manutenção da integridade intestinal.\",\n        \"observation\": \"Considerar a saúde intestinal do paciente.\"\n      },\n      {\n        \"name\": \"Whey Protein (rico em BCAAs)\",\n        \"dosage\": \"20g a 30g\",\n        \"frequency\": \"Após o treino\",\n        \"purpose\": \"Promover a síntese proteica e a recuperação muscular.\",\n        \"observation\": \"Importante para a melhoria dos níveis críticos de isoleucina.\"\n      }\n    ],\n    \"training\": {\n      \"recommendations\": [\n        \"Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\",\n        \"Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\",\n        \"Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\",\n        \"Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\",\n        \"Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\"\n      ],\n      \"avoid\": [\n        \"Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\",\n        \"Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\",\n        \"Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\"\n      ],\n      \"focus\": \"Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.\"\n    }\n  }\n}\n\n# OBJETIVO\n    Crie um relatório de performance em formato markdown, utilizando os dados do JSON fornecido em \"CONTEXTO ADICIONAL (RELATÓRIO ESTRUTURADO)\".\n\n    **Use EXATAMENTE a seguinte estrutura e títulos:**\n\n\n    # RELATÓRIO FINAL - Vida Nova\n\n    (Cri um texto introdutório de `summary.content` do JSON como o texto principal aqui)\n\n    ---\n\n    ## Sugestão Alimentar\n    (Use o conteúdo da seção `diet_suggestions` para criar uma visão consolidada e direta das recomendações alimentares, formatando cada recomendação como um item de lista simples com \"-\" para melhor legibilidade)\n\n    ---\n\n    ## Suplementação Sugerida\n    (Liste cada suplemento da seção `supplements`, formatando com nome em negrito e os demais campos como tópicos)\n\n    ---\n\n    ## Dica de Treino\n    (Use o conteúdo da seção `training` para descrever as recomendações, o que evitar e o foco)\n    "
    }
  ],
  "temperature": 1.0,
  "max_tokens": 4058
}
```
- **Outputs:**
```json
{
  "id": "gen-1757099106-j7Pn1ByHFS5AeSGQX2bt",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "# RELATÓRIO FINAL - Vida Nova\n\nObserva-se que o paciente possui 32 anos, gênero masculino, pesando 83 kg e medindo 1,76 m, resultando em um IMC de 26,82. O histórico médico do indivíduo é escasso em informações, e a atividade física não foi claramente informada. O paciente apresenta como objetivo clínico a melhora da composição corporal e o ganho de massa muscular, apresentando uma dieta onívora sem restrições específicas. Notam-se variações em seu nível de energia, associado a uma qualidade de sono não detalhada, o que pode impactar seu desempenho em atividades físicas e sua saúde geral.\n\nA análise do laudo metabólico revela diversas alterações significativas. Os níveis de Acetil-L-Carnitina estão reduzidos, o que pode comprometer a produção de ATP, culminando em fadiga crônica e fraqueza muscular. A adenosina, por sua vez, encontra-se elevada, indicando potenciais riscos de bradicardia e diminuição na resposta ao estresse. Os níveis críticos de isoleucina sugerem uma deficiência que pode prejudicar a síntese proteica e a recuperação muscular, enquanto a leucina está em níveis excessivos, o que pode aumentar o risco de resistência à insulina. Por fim, a redução dos níveis de piruvato e o excesso de valina indicam desbalanceamentos adicionais no perfil de aminoácidos, impactando negativamente no metabolismo energético e na performance física.\n\nIntegrando os achados bioquímicos à intervenção proposta, é necessário adotar um plano que contemple ajustes na alimentação, suplementação e prática de exercícios. A ênfase será na inclusão de grupos alimentares que favoreçam a saúde mitocondrial e a recuperação muscular, complementada por suplementação de cofatores e aminoácidos específicos que ajudem a restaurar o equilíbrio metabólico. A prática regular de atividade física será direcionada para o treinamento de força, visando otimizar o ganho de massa muscular e a resistência física, de forma a abordar as deficiências e excessos identificados nos exames.\n\nEm conclusão, o objetivo estabelecido é promover a melhora da composição corporal e o aumento da massa muscular, utilizando uma abordagem integrada que considera a interrelação entre alimentação, suplementação e treino. Esta estratégia abrangente é fundamental para a restauração do equilíbrio metabólico e para a maximização dos resultados desejados, tendo em vista as alterações significativas identificadas nas análises metabolômicas.\n\n---\n\n## Sugestão Alimentar\n- Carnes magras (como peito de frango e carne bovina magra): Ricas em proteínas completas e L-carnitina, ajudam a aumentar a produção de ATP e podem melhorar a energia muscular, compensando a redução observada de Acetil-L-Carnitina.\n- Peixes gordurosos (salmão, sardinha e cavala): Fontes de ômega-3, que possuem propriedades anti-inflamatórias e podem ajudar a reduzir o estresse oxidativo e melhorar a saúde cardiovascular, beneficiando a performance física e mitigando alguns efeitos da elevação da adenosina.\n- Ovos: Ricos em vitamina B12, B6 e proteínas de alta qualidade, os ovos suportam a síntese proteica e a recuperação muscular, abordando a deficiência observada na isoleucina.\n- Produtos lácteos fermentados (iogurte natural, kefir): Fornecem probióticos que podem melhorar a saúde intestinal e ajudar na regulação do estresse oxidativo, além de fornecer proteínas e aminoácidos essenciais para a recuperação muscular.\n- Vegetais crucíferos (brócolis, couve-flor, couve-de-bruxelas): Ricos em antioxidantes e vitaminas, ajudam a reduzir a inflamação e melhoram a sensibilidade à insulina, essencial diante da sobrecarga na via de sinalização da insulina gerada pelo excesso de leucina.\n- Frutas vermelhas (morango, framboesa): Fonte de antioxidantes e vitamina C, podem auxiliar na redução do estresse oxidativo e melhorar a função celular, pois a deficiência de Acetil-L-Carnitina está associada ao aumento do estresse oxidativo.\n- Quinoa e arroz integral: Fontes de carboidratos complexos que auxiliam na estabilização da glicose, oferecendo energia contínua e ajudando na recuperação muscular, crucial com os níveis críticos de isoleucina.\n\n---\n\n## Suplementação Sugerida\n- **Acetil-L-Carnitina**\n  - Dosagem: 1g a 2g\n  - Frequência: Diário, antes do treino\n  - Propósito: Melhorar o transporte de ácidos graxos para a mitocôndria e aumentar a produção de ATP, contribuindo para a performance física e redução da fadiga.\n  - Observação: Considerar a situação clínica do paciente em relação a histórico de fadiga e desempenho.\n  \n- **L-Carnitina**\n  - Dosagem: 500mg a 1g\n  - Frequência: Diário, se necessário\n  - Propósito: Suporte adicional para o transporte de ácidos graxos e aumento de energia durante atividades físicas.\n  - Observação: Avaliar a necessidade com base no nível de atividade física e fadiga.\n\n- **Cofatores: Vitamina C**\n  - Dosagem: 500mg\n  - Frequência: Diário\n  - Propósito: Suporte ao controle do estresse oxidativo, melhorando a função celular e energização.\n  - Observação: Monitorar a ingestão de antioxidantes na dieta.\n\n- **Cofatores: Vitamina B6 (P-5-P)**\n  - Dosagem: 10mg - 25mg\n  - Frequência: Diário\n  - Propósito: Apoiar o metabolismo de aminoácidos e melhorar a recuperação muscular.\n  - Observação: Importante para a adequada metabolização da isoleucina.\n\n- **Cofatores: Vitamina B3 (niacinamida ou NAD precursor)**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Suporte à produção de energia e otimização do metabolismo.\n  - Observação: Pode auxiliar na regulação do metabolismo energético.\n\n- **CoQ10 (ubiquinol)**\n  - Dosagem: 100mg a 300mg\n  - Frequência: Diário\n  - Propósito: Promover a saúde mitocondrial e aumentar a produção de ATP.\n  - Observação: Avaliar a resposta do paciente ao suporte mitocondrial.\n\n- **Ácido Alfa-Lipóico**\n  - Dosagem: 300mg\n  - Frequência: Diário\n  - Propósito: Fornecer suporte antioxidante e melhorar a sensibilidade à insulina.\n  - Observação: Considerar a relação com o excesso de leucina.\n\n- **Complexo de Vitaminas do grupo B (incluindo B6, B12)**\n  - Dosagem: Recomendações diárias específicas.\n  - Frequência: Diário\n  - Propósito: Apoio geral ao metabolismo energético e recuperação muscular.\n  - Observação: Incluir como um suporte contínuo através de uma dieta equilibrada.\n\n- **Glutamina**\n  - Dosagem: 5g\n  - Frequência: Diário, especialmente após exercícios\n  - Propósito: Apoio à recuperação muscular e manutenção da integridade intestinal.\n  - Observação: Considerar a saúde intestinal do paciente.\n\n- **Whey Protein (rico em BCAAs)**\n  - Dosagem: 20g a 30g\n  - Frequência: Após o treino\n  - Propósito: Promover a síntese proteica e a recuperação muscular.\n  - Observação: Importante para a melhoria dos níveis críticos de isoleucina.\n\n---\n\n## Dica de Treino\n- Recomendações:\n  - Treinos de força 4 a 5 vezes por semana focando em grandes grupos musculares como pernas, costas e peito.\n  - Incluir exercícios compostos como agachamentos, levantamento terra, supino e remada.\n  - Programar sessões de alta intensidade, utilizando sobrecargas progressivas (aumentar gradualmente os pesos utilizados).\n  - Adicionar exercícios de isolamento para músculos menores, como tríceps e bíceps, com repetições moderadas a altas para promover hipertrofia.\n  - Implementar exercícios de core (abdominais e lombares) para estabilização, essenciais para suporte em levantamentos pesados.\n\n- Evitar:\n  - Evitar treinos excessivos sem descanso adequado, diminuindo o volume e a intensidade quando sinais de fadiga excessiva aparecerem.\n  - Excluir exercícios que perturbem a técnica, como levantamentos com muitas repetições a altas intensidades, que podem aumentar o risco de lesões.\n  - Não realizar atividades aeróbicas excessivas que possam interferir na recuperação e no ganho de massa muscular.\n\n- Foco: Reduzir a fadiga crônica, melhorar a produção de ATP e maximizar o ganho de massa muscular através de um protocolo de treino estruturado em força.",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "reasoning": null
      },
      "native_finish_reason": "stop"
    }
  ],
  "created": 1757099106,
  "model": "openai/gpt-4o-mini",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_8bda4d3a2c",
  "usage": {
    "completion_tokens": 1922,
    "prompt_tokens": 3208,
    "total_tokens": 5130,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "provider": "OpenAI"
}
```

---
