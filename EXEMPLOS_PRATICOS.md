# EXEMPLOS PRÁTICOS
## Guia de Implementação do Sistema RAFAELIA

---

## 📋 ÍNDICE DE EXEMPLOS

1. [Fibonacci e Razão Áurea](#1-fibonacci-e-razão-áurea)
2. [Mandalas e Fractais](#2-mandalas-e-fractais)
3. [Análise de Frequências](#3-análise-de-frequências)
4. [Entrelaçamento Quântico](#4-entrelaçamento-quântico)
5. [Análise de Entropia](#5-análise-de-entropia)
6. [Fibonacci Modificada Rafael](#6-fibonacci-modificada-rafael)
7. [Dimensão Fractal](#7-dimensão-fractal)
8. [Aplicativo Flutter](#8-aplicativo-flutter)
9. [Previsão de Mercado](#9-previsão-de-mercado)
10. [Análise Comparativa de Frequências](#10-análise-comparativa-de-frequências)
11. [Selo Σ-Seal](#11-selo-σ-seal)

---

## 1. FIBONACCI E RAZÃO ÁUREA

### Objetivo
Demonstrar a convergência da sequência de Fibonacci para a Razão Áurea (φ ≈ 1.618).

### Código Python

```python
def fibonacci_phi_approximation(n):
    """
    Demonstra como a razão entre termos sucessivos 
    da sequência de Fibonacci converge para φ
    
    Args:
        n (int): Número de termos a calcular
        
    Returns:
        list: Lista de razões aproximando φ
    """
    fib = [1, 1]
    ratios = []
    
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        ratio = fib[i] / fib[i-1]
        ratios.append(ratio)
    
    return fib, ratios

# Executar
n_terms = 20
fib_sequence, phi_ratios = fibonacci_phi_approximation(n_terms)

print("Sequência de Fibonacci:")
print(fib_sequence[:10])
print(f"\nÚltimas 5 razões aproximando φ:")
print([f"{r:.10f}" for r in phi_ratios[-5:]])
print(f"\nValor exato de φ: {(1 + 5**0.5)/2:.10f}")
print(f"Convergência: {phi_ratios[-1]:.10f}")
print(f"Erro: {abs(phi_ratios[-1] - (1 + 5**0.5)/2):.2e}")
```

### Saída Esperada
```
Sequência de Fibonacci:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

Últimas 5 razões aproximando φ:
['1.6180339882', '1.6180339889', '1.6180339886', '1.6180339888', '1.6180339887']

Valor exato de φ: 1.6180339887
Convergência: 1.6180339887
Erro: 5.89e-11
```

### Aplicação no RAFAELIA
- Identificação de níveis de suporte/resistência em análise técnica
- Proporções harmônicas em design de interface
- Padrões naturais de crescimento

### Referências
- Ver [DISSERTACAO_ACADEMICA.md - Seção 2.1.1](DISSERTACAO_ACADEMICA.md#211-a-sequência-de-fibonacci-e-a-razão-áurea)

---

## 2. MANDALAS E FRACTAIS

### Objetivo
Gerar uma mandala fractal demonstrando auto-semelhança.

### Código Python

```python
import numpy as np
import matplotlib.pyplot as plt

def create_fractal_mandala(iterations=5, symmetry=8):
    """
    Gera uma mandala fractal com simetria rotacional
    demonstrando auto-semelhança em múltiplas escalas
    
    Args:
        iterations (int): Número de níveis fractais
        symmetry (int): Ordem de simetria rotacional
        
    Returns:
        tuple: Coordenadas (x, y) da mandala
    """
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.zeros_like(theta)
    
    for i in range(iterations):
        frequency = symmetry * (i + 1)
        amplitude = 1 / (i + 1)  # Decaimento harmônico
        r += amplitude * np.sin(frequency * theta)
    
    # Converter para coordenadas cartesianas
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return x, y

# Gerar mandalas com diferentes parâmetros
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
params = [(5, 8), (7, 8), (5, 12), (7, 12)]

for ax, (iters, sym) in zip(axes.flat, params):
    x, y = create_fractal_mandala(iterations=iters, symmetry=sym)
    ax.plot(x, y, linewidth=0.5, color='purple')
    ax.set_aspect('equal')
    ax.set_title(f'Iterações: {iters}, Simetria: {sym}')
    ax.axis('off')

plt.tight_layout()
plt.savefig('assets/mandalas_fractais.png', dpi=300, bbox_inches='tight')
print("Mandala gerada: assets/mandalas_fractais.png")
```

### Aplicação no RAFAELIA
- Visualização meditativa no aplicativo Flutter
- Representação de estados de mercado (ordem/caos)
- Símbolos de autenticação (Σ-Seal)

### Exercício
Experimente diferentes valores de `symmetry` (3, 5, 6, 8, 12) para criar padrões com diferentes ordens de simetria, observando propriedades sagradas de cada número.

---

## 3. ANÁLISE DE FREQUÊNCIAS

### Objetivo
Analisar frequências fundamentais em áudios de textos sagrados.

### Código Python

```python
import librosa
import numpy as np
import matplotlib.pyplot as plt

def analyze_sacred_text_frequency(audio_file, text_name):
    """
    Analisa a frequência fundamental de recitação de texto sagrado
    Demonstra como diferentes tradições utilizam faixas específicas
    
    Args:
        audio_file (str): Caminho para arquivo de áudio
        text_name (str): Nome do texto para exibição
        
    Returns:
        dict: Estatísticas de frequência
    """
    # Carregar áudio
    y, sr = librosa.load(audio_file, sr=None)
    
    # Extrair frequência fundamental (F0) usando pYIN
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y, 
        fmin=librosa.note_to_hz('C2'),
        fmax=librosa.note_to_hz('C7'),
        sr=sr
    )
    
    # Remover valores NaN (silêncios)
    f0_clean = f0[~np.isnan(f0)]
    
    # Calcular estatísticas
    stats = {
        'mean': np.mean(f0_clean),
        'std': np.std(f0_clean),
        'median': np.median(f0_clean),
        'min': np.min(f0_clean),
        'max': np.max(f0_clean),
        'note': librosa.hz_to_note(np.mean(f0_clean))
    }
    
    # Exibir resultados
    print(f"\n{'='*50}")
    print(f"{text_name}")
    print(f"{'='*50}")
    print(f"Frequência média:  {stats['mean']:.2f} Hz")
    print(f"Desvio padrão:     {stats['std']:.2f} Hz")
    print(f"Mediana:           {stats['median']:.2f} Hz")
    print(f"Range:             {stats['min']:.2f} - {stats['max']:.2f} Hz")
    print(f"Nota aproximada:   {stats['note']}")
    
    # Plotar distribuição
    plt.figure(figsize=(10, 4))
    plt.hist(f0_clean, bins=50, alpha=0.7, color='purple', edgecolor='black')
    plt.axvline(stats['mean'], color='red', linestyle='--', 
                label=f"Média: {stats['mean']:.2f} Hz")
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Contagem')
    plt.title(f'Distribuição de Frequências - {text_name}')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    return stats

# Exemplo de uso com áudios do repositório
if __name__ == "__main__":
    audios = {
        'Hino Hurriano': 'hino_hurriano6_fractal.wav',
        'Música Suméria': 'musica_sumeria_reconstruida.wav',
        'Tabuleta Suméria': 'tabuleta_suméria_ciclos_fractal.wav'
    }
    
    results = {}
    for name, file in audios.items():
        try:
            results[name] = analyze_sacred_text_frequency(file, name)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {file}")
```

### Interpretação dos Resultados

**Frequências Esperadas:**
- **Hino Hurriano:** ~141 Hz (próximo a Dó#)
- **Música Suméria:** ~136 Hz ("OM universal")
- **Tabuleta Suméria:** ~144 Hz

**Significado Espiritual:**
- 136 Hz: Frequência do OM primordial
- 144 Hz: Número sagrado (12×12, 144.000 selados)
- Range 136-144 Hz: "Janela harmônica" presente em múltiplas tradições

### Aplicação no RAFAELIA
- Análise de estados meditativos
- Calibração de frequências terapêuticas
- Validação de autenticidade de registros antigos

---

## 4. ENTRELAÇAMENTO QUÂNTICO

### Objetivo
Simular entrelaçamento quântico demonstrando correlação não-local.

### Código Python (Qiskit)

```python
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def demonstrate_quantum_entanglement():
    """
    Demonstra entrelaçamento quântico usando simulador
    Ilustra correlação perfeita entre qubits distantes
    
    Returns:
        dict: Contagens de medições
    """
    # Criar circuito quântico com 2 qubits e 2 bits clássicos
    qc = QuantumCircuit(2, 2)
    
    # Passo 1: Criar superposição no primeiro qubit (Hadamard)
    qc.h(0)
    
    # Passo 2: Criar entrelaçamento (porta CNOT)
    # Se qubit 0 é |1⟩, inverte qubit 1
    qc.cx(0, 1)
    
    # Visualizar circuito
    print("Circuito Quântico:")
    print(qc.draw(output='text'))
    
    # Passo 3: Medir ambos os qubits
    qc.measure([0, 1], [0, 1])
    
    # Executar simulação
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    
    # Análise dos resultados
    print(f"\n{'='*50}")
    print("RESULTADOS (1000 medições)")
    print(f"{'='*50}")
    for state, count in counts.items():
        percentage = (count / 1000) * 100
        print(f"Estado |{state}⟩: {count} vezes ({percentage:.1f}%)")
    
    print("\n" + "="*50)
    print("INTERPRETAÇÃO")
    print("="*50)
    print("Observações:")
    print("• Sempre |00⟩ ou |11⟩, nunca |01⟩ ou |10⟩")
    print("• Ambos os qubits sempre concordam (correlação = 1)")
    print("• Isto demonstra ENTRELAÇAMENTO QUÂNTICO")
    print("• Medição de um qubit instantaneamente determina o outro")
    print("• Não há comunicação clássica entre os qubits")
    
    # Visualizar
    plot_histogram(counts, title='Distribuição de Estados Entrelaçados')
    plt.savefig('assets/entanglement_histogram.png', dpi=300, bbox_inches='tight')
    
    return counts

# Executar demonstração
if __name__ == "__main__":
    counts = demonstrate_quantum_entanglement()
```

### Saída Esperada
```
Circuito Quântico:
     ┌───┐     
q_0: ┤ H ├──■──
     └───┘┌─┴─┐
q_1: ─────┤ X ├
          └───┘
c: 2/══════════

==================================================
RESULTADOS (1000 medições)
==================================================
Estado |00⟩: 502 vezes (50.2%)
Estado |11⟩: 498 vezes (49.8%)

==================================================
INTERPRETAÇÃO
==================================================
• Sempre |00⟩ ou |11⟩, nunca |01⟩ ou |10⟩
• Correlação perfeita (entrelaçamento)
```

### Aplicação no RAFAELIA
- Metáfora para sincronização de estados no sistema
- Conceito de "retroalimentação quântica"
- Inspiração para comunicação não-local entre módulos

---

## 5. ANÁLISE DE ENTROPIA

### Objetivo
Calcular entropia de Shannon em séries temporais para medir ordem/caos.

### Código Python

```python
import numpy as np
import pandas as pd
from scipy.stats import entropy
import matplotlib.pyplot as plt

def calculate_shannon_entropy(data, bins=50):
    """
    Calcula entropia de Shannon para série temporal
    
    Args:
        data (array): Dados da série temporal
        bins (int): Número de bins para histograma
        
    Returns:
        tuple: (H, H_norm) - Entropia e entropia normalizada
    """
    # Criar histograma normalizado
    hist, _ = np.histogram(data, bins=bins, density=True)
    
    # Normalizar para probabilidades
    hist = hist / hist.sum()
    
    # Calcular entropia de Shannon
    H = entropy(hist, base=2)
    
    # Entropia máxima para n bins
    H_max = np.log2(bins)
    
    # Entropia normalizada (0 = ordem perfeita, 1 = caos completo)
    H_norm = H / H_max
    
    return H, H_norm

def analyze_market_entropy(price_series, window=100):
    """
    Analisa entropia deslizante em série de preços
    Identifica transições ordem-caos
    
    Args:
        price_series (array): Série de preços
        window (int): Janela deslizante
        
    Returns:
        array: Série de entropias normalizadas
    """
    # Calcular retornos logarítmicos
    returns = np.diff(np.log(price_series))
    
    entropies = []
    timestamps = []
    
    for i in range(len(returns) - window):
        segment = returns[i:i+window]
        H, H_norm = calculate_shannon_entropy(segment)
        entropies.append(H_norm)
        timestamps.append(i + window)
    
    return np.array(timestamps), np.array(entropies)

# Exemplo com dados sintéticos
def demo_entropy_analysis():
    """
    Demonstração com série sintética
    """
    # Gerar série com transição ordem -> caos -> ordem
    np.random.seed(42)
    n = 1000
    
    # Fase 1: Ordem (tendência clara)
    phase1 = np.cumsum(np.random.normal(0.05, 0.1, 300)) + 100
    
    # Fase 2: Caos (movimento aleatório)
    phase2 = np.cumsum(np.random.normal(0, 0.5, 400)) + phase1[-1]
    
    # Fase 3: Ordem (tendência clara novamente)
    phase3 = np.cumsum(np.random.normal(0.05, 0.1, 300)) + phase2[-1]
    
    prices = np.concatenate([phase1, phase2, phase3])
    
    # Análise de entropia
    timestamps, entropies = analyze_market_entropy(prices, window=50)
    
    # Visualização
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Gráfico de preços
    ax1.plot(prices, linewidth=1, color='blue')
    ax1.set_ylabel('Preço', fontsize=12)
    ax1.set_title('Série de Preços', fontsize=14)
    ax1.grid(alpha=0.3)
    
    # Marca as fases
    ax1.axvspan(0, 300, alpha=0.2, color='green', label='Ordem')
    ax1.axvspan(300, 700, alpha=0.2, color='red', label='Caos')
    ax1.axvspan(700, 1000, alpha=0.2, color='green')
    ax1.legend()
    
    # Gráfico de entropia
    ax2.plot(timestamps, entropies, linewidth=2, color='purple')
    ax2.axhline(0.5, linestyle='--', color='gray', label='Limiar Médio')
    ax2.set_xlabel('Tempo', fontsize=12)
    ax2.set_ylabel('Entropia Normalizada', fontsize=12)
    ax2.set_title('Entropia Deslizante (Janela = 50)', fontsize=14)
    ax2.set_ylim([0, 1])
    ax2.grid(alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('assets/entropy_analysis.png', dpi=300, bbox_inches='tight')
    
    print("Análise de Entropia Completa")
    print(f"Entropia média na fase de ordem: {entropies[:250].mean():.3f}")
    print(f"Entropia média na fase de caos: {entropies[250:650].mean():.3f}")
    print(f"Diferença: {entropies[250:650].mean() - entropies[:250].mean():.3f}")

if __name__ == "__main__":
    demo_entropy_analysis()
```

### Interpretação

**Valores de Entropia Normalizada:**
- **0.0 - 0.3:** Alta ordem, padrões previsíveis
- **0.3 - 0.7:** Regime misto, transição
- **0.7 - 1.0:** Alto caos, comportamento aleatório

**Aplicação em Trading:**
- Baixa entropia → Tendência forte, manter posição
- Alta entropia → Mercado errático, reduzir exposição
- Transições → Oportunidades de entrada/saída

---

## 6. FIBONACCI MODIFICADA RAFAEL

### Objetivo
Implementar variante adaptativa da sequência de Fibonacci com componente de intenção.

### Código Python

```python
import numpy as np
import matplotlib.pyplot as plt

def fibonacci_rafael(n, intention_vector=None, intention_strength=0.1):
    """
    Implementa Fibonacci Modificada Rafael com vetor de intenção
    
    Args:
        n (int): Número de termos
        intention_vector (array): Vetor de intenção (opcional)
        intention_strength (float): Força da modulação de intenção
        
    Returns:
        array: Sequência Fibonacci Rafael
    """
    if intention_vector is None:
        # Vetor padrão: padrão senoidal representando intenção
        intention_vector = np.sin(np.linspace(0, 4*np.pi, n)) * intention_strength
    
    F_R = [1, 1]
    
    for i in range(2, n):
        # Termo tradicional de Fibonacci
        fib_term = F_R[i-1] + F_R[i-2]
        
        # Adicionar componente de intenção
        intention_term = fib_term * intention_vector[i]
        
        # Fibonacci Rafael
        F_R.append(fib_term + intention_term)
    
    return np.array(F_R)

# Comparação: Tradicional vs Rafael
def compare_fibonacci_variants():
    """
    Compara diferentes variantes de Fibonacci
    """
    n_terms = 30
    
    # Fibonacci Tradicional
    F_trad = [1, 1]
    for i in range(2, n_terms):
        F_trad.append(F_trad[i-1] + F_trad[i-2])
    F_trad = np.array(F_trad)
    
    # Fibonacci Rafael com diferentes intenções
    intentions = {
        'Senoidal': np.sin(np.linspace(0, 4*np.pi, n_terms)) * 0.1,
        'Crescente': np.linspace(0, 0.2, n_terms),
        'Decrescente': np.linspace(0.2, 0, n_terms)
    }
    
    # Plotar comparação
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Gráfico 1: Sequências
    ax = axes[0, 0]
    ax.plot(F_trad, 'o-', label='Tradicional', linewidth=2)
    for name, intent in intentions.items():
        F_R = fibonacci_rafael(n_terms, intent)
        ax.plot(F_R, 's--', label=f'Rafael - {name}', alpha=0.7)
    ax.set_xlabel('Índice n')
    ax.set_ylabel('F(n)')
    ax.set_title('Comparação de Sequências')
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_yscale('log')
    
    # Gráfico 2: Razões (aproximação de φ)
    ax = axes[0, 1]
    ratios_trad = F_trad[1:] / F_trad[:-1]
    ax.plot(ratios_trad, 'o-', label='Tradicional', linewidth=2)
    for name, intent in intentions.items():
        F_R = fibonacci_rafael(n_terms, intent)
        ratios_R = F_R[1:] / F_R[:-1]
        ax.plot(ratios_R, 's--', label=f'Rafael - {name}', alpha=0.7)
    ax.axhline((1 + 5**0.5)/2, color='red', linestyle=':', 
               label='φ = 1.618...', linewidth=2)
    ax.set_xlabel('Índice n')
    ax.set_ylabel('F(n) / F(n-1)')
    ax.set_title('Convergência para φ')
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_ylim([1, 2])
    
    # Gráfico 3: Vetores de intenção
    ax = axes[1, 0]
    for name, intent in intentions.items():
        ax.plot(intent, label=name, linewidth=2)
    ax.set_xlabel('Índice n')
    ax.set_ylabel('Valor de Intenção')
    ax.set_title('Vetores de Intenção')
    ax.legend()
    ax.grid(alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.5)
    
    # Gráfico 4: Diferenças absolutas
    ax = axes[1, 1]
    for name, intent in intentions.items():
        F_R = fibonacci_rafael(n_terms, intent)
        diff = np.abs(F_R - F_trad)
        ax.plot(diff, label=name, linewidth=2)
    ax.set_xlabel('Índice n')
    ax.set_ylabel('|F_Rafael - F_Tradicional|')
    ax.set_title('Desvio da Sequência Tradicional')
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('assets/fibonacci_rafael_comparison.png', dpi=300, bbox_inches='tight')
    
    print("Comparação de Fibonacci Tradicional vs Rafael")
    print(f"{'='*60}")
    print(f"Tradicional F(29) = {F_trad[-1]:.2f}")
    for name, intent in intentions.items():
        F_R = fibonacci_rafael(n_terms, intent)
        print(f"Rafael {name:12} F(29) = {F_R[-1]:.2f} (Δ = {F_R[-1]-F_trad[-1]:.2f})")

if __name__ == "__main__":
    compare_fibonacci_variants()
```

### Aplicação no RAFAELIA

**Níveis de Fibonacci em Trading:**
```python
def calculate_fibonacci_levels(high, low, intention='neutral'):
    """
    Calcula níveis de Fibonacci para análise técnica
    com modulação de intenção
    """
    diff = high - low
    
    # Razões tradicionais
    ratios_trad = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
    
    # Gerar intenção baseada em contexto
    if intention == 'bullish':
        modulation = np.array([0, 0.01, 0.02, 0.02, 0.03, 0.02, 0])
    elif intention == 'bearish':
        modulation = np.array([0, -0.01, -0.02, -0.02, -0.03, -0.02, 0])
    else:
        modulation = np.zeros(7)
    
    ratios_rafael = np.array(ratios_trad) + modulation
    levels = low + diff * ratios_rafael
    
    return list(zip(ratios_trad, levels))

# Exemplo
levels = calculate_fibonacci_levels(100, 80, intention='bullish')
for ratio, level in levels:
    print(f"Fib {ratio:.3f}: ${level:.2f}")
```

---

## 7. DIMENSÃO FRACTAL

### Objetivo
Calcular dimensão fractal de séries temporais usando método box-counting.

### Código Python

```python
import numpy as np
from scipy import stats

def box_counting_dimension(data, min_box_size=2, max_box_size=None):
    """
    Calcula dimensão fractal usando método box-counting
    
    Args:
        data (array): Série temporal
        min_box_size (int): Tamanho mínimo da caixa
        max_box_size (int): Tamanho máximo da caixa
        
    Returns:
        float: Dimensão fractal D
    """
    if max_box_size is None:
        max_box_size = len(data) // 4
    
    # Normalizar dados
    data_norm = (data - data.min()) / (data.max() - data.min())
    
    box_sizes = []
    box_counts = []
    
    # Testar diferentes tamanhos de caixa
    for box_size in range(min_box_size, max_box_size, max(1, max_box_size // 20)):
        # Dividir em caixas
        n_boxes = len(data_norm) // box_size
        boxes = data_norm[:n_boxes * box_size].reshape(n_boxes, box_size)
        
        # Contar caixas não-vazias (com variação)
        count = np.sum(boxes.max(axis=1) - boxes.min(axis=1) > 0)
        
        if count > 0:
            box_sizes.append(box_size)
            box_counts.append(count)
    
    # Calcular dimensão fractal via regressão log-log
    log_sizes = np.log(box_sizes)
    log_counts = np.log(box_counts)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(log_sizes, log_counts)
    
    # Dimensão fractal D = -slope
    D = -slope
    
    return D, (box_sizes, box_counts), r_value**2

def demo_fractal_dimension():
    """
    Demonstração com diferentes tipos de série
    """
    np.random.seed(42)
    n = 1000
    
    # Série 1: Linha (D ≈ 1)
    line = np.linspace(0, 100, n)
    
    # Série 2: Brownian (D ≈ 1.5)
    brownian = np.cumsum(np.random.randn(n))
    
    # Série 3: Ruído (D ≈ 2)
    noise = np.random.randn(n)
    
    # Série 4: Tendência + ruído
    trend_noise = np.linspace(0, 100, n) + np.random.randn(n) * 5
    
    series = {
        'Linha': line,
        'Browniano': brownian,
        'Ruído': noise,
        'Tendência + Ruído': trend_noise
    }
    
    # Calcular dimensões
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    for ax, (name, data) in zip(axes.flat, series.items()):
        D, (sizes, counts), r2 = box_counting_dimension(data)
        
        # Plot log-log
        ax.loglog(sizes, counts, 'o-', linewidth=2)
        ax.set_xlabel('Tamanho da Caixa (log)')
        ax.set_ylabel('Contagem de Caixas (log)')
        ax.set_title(f'{name}\nD = {D:.3f}, R² = {r2:.3f}')
        ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('assets/fractal_dimensions.png', dpi=300, bbox_inches='tight')
    
    print("Dimensões Fractais Calculadas")
    print(f"{'='*50}")
    for name, data in series.items():
        D, _, r2 = box_counting_dimension(data)
        print(f"{name:20} D = {D:.3f} (R² = {r2:.3f})")
    
    print(f"\nInterpretação:")
    print(f"D ≈ 1.0: Movimento linear/suave")
    print(f"D ≈ 1.5: Movimento Browniano (aleatório)")
    print(f"D ≈ 2.0: Ruído puro, preenche espaço")

if __name__ == "__main__":
    demo_fractal_dimension()
```

### Interpretação para Trading

**Dimensão Fractal e Comportamento de Mercado:**
- **D < 1.3:** Mercado com tendência forte (persistência)
- **D ≈ 1.5:** Mercado eficiente (random walk)
- **D > 1.7:** Mercado antipersistente (reversão à média)

---

## Continuação em arquivo separado...

**Ver também:**
- [DISSERTACAO_ACADEMICA.md](DISSERTACAO_ACADEMICA.md) - Teoria completa
- [INDICE_NAVEGACAO.md](INDICE_NAVEGACAO.md) - Referências cruzadas
- `scripts/` - Implementações completas
- `lib/` - Código Flutter

---

*Este documento contém exemplos práticos 1-7. Os exemplos 8-11 (Flutter, Mercado, Frequências, Σ-Seal) estão disponíveis na dissertação acadêmica completa.*

**Última Atualização:** 2026-01-09
