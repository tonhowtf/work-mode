# WorkMode - Bloqueador de Aplicações Durante o Trabalho

![projeto funcionando](work-mode.gif "workmode funcionando")

## Descrição
WorkMode é um script robusto que termina processos indesejados (como Telegram e Discord) durante suas horas de trabalho.

## Funcionalidades
- **Bloqueio de Aplicações**: Monitora e finaliza processos indesejados (ex.: Telegram e Discord) tanto em Linux quanto Windows.
- **Timer de Trabalho**: Permite definir o tempo de bloqueio via linha de comando, aceitando números decimais e valores menores que 1.
- **Feedback Visual**: Usa `rich` e `alive_progress` para mostrar uma barra de progresso e feedback em tempo real.
- **Multi-Plataforma**: Funciona em Linux e Windows.

## Pré-Requisitos
- Python 3.6 ou superior
- Bibliotecas Python:
  - `psutil`
  - `rich`
  - `alive-progress`

Instale as dependências com:
```bash
pip install psutil rich alive-progress
```

## Uso
Execute o script passando o tempo desejado (em horas) como argumento:
```bash
python workmode.py 2.5
```
Isso bloqueará os processos especificados por 2,5 horas.

## Como Funciona
1. **Monitoramento de Processos**:  
   O script utiliza `psutil` para iterar sobre os processos ativos e identificar aqueles que estão na lista de vítimas.

2. **Identificação e Finalização**:  
   Se o nome do processo corresponder a um dos nomes na lista (com ou sem ".exe"), ele é finalizado imediatamente. Isso evita distrações e mantém seu ambiente de trabalho limpo.

3. **Timer de Bloqueio**:  
   Durante o período definido, o script roda um loop de contagem regressiva (em segundos) usando `alive_progress` para fornecer feedback visual do progresso.

4. **Feedback Visual e Logs**:  
   Mensagens de status são exibidas utilizando `rich` para garantir que você saiba exatamente o que está acontecendo.


## Eu me inspirei nesse projeto bashbunni que é um pomodoro cli❤️:
https://gist.github.com/bashbunni/f6b04fc4703903a71ce9f70c58345106

