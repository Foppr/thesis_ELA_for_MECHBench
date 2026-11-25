import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component with memory
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            phase = 0.5 * np.cos(i * np.pi / (self.dim + 2))
            # Add memory effect using previous dimension values
            memory_factor = 1.0
            if i > 0:
                memory_factor = 1.0 + 0.1 * np.sin(x[i-1])
            quantum_harmonic += np.sin(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2) * memory_factor
        
        # Fractional Brownian motion effect with Hurst parameter modulation and chaotic perturbation
        fbm_effect = 0
        hurst = 0.3 + 0.4 * np.sin(self.dim * np.pi / 8)
        for i in range(self.dim):
            # Add chaotic perturbation to the random component
            chaotic_pert = 0.1 * np.sin(x[i] * self.dim)
            fbm_effect += (np.random.normal(0, 1) + chaotic_pert) * \
                          np.exp(-hurst * abs(x[i])) * \
                          np.cos(hurst * x[i])
        
        # Adaptive penalty landscape with dynamic threshold and chaotic scaling
        penalty = 0
        for i in range(self.dim):
            threshold = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 3))
            # Add chaotic scaling to the penalty threshold
            chaotic_scale = 1.0 + 0.2 * np.cos(i * np.pi / (self.dim + 4))
            threshold *= chaotic_scale
            if abs(x[i]) > threshold:
                penalty += 10.0 * (abs(x[i]) - threshold)**2
        
        # Nested sinusoidal modulations with dynamic frequencies and chaotic coupling
        nested_modulation = 0
        for i in range(self.dim):
            freq1 = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 4))
            freq2 = 0.5 + 1.0 * np.cos(i * np.pi / (self.dim + 5))
            # Add chaotic modulation to the frequencies
            freq1 *= (1.0 + 0.1 * np.sin(x[i] * self.dim))
            freq2 *= (1.0 + 0.1 * np.cos(x[i] * self.dim))
            nested_modulation += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Dynamic coupling weights with chaotic modulation and memory-dependent interactions
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength using logistic map with memory
                r = 3.8 + 0.2 * np.sin(i * np.pi / (self.dim + 6))
                # Add memory effect to coupling
                memory_coupling = 1.0 + 0.1 * np.sin(x[i-1] if i > 0 else x[j])
                coupling = r * np.sin(x[i]) * np.cos(x[j]) * memory_coupling
                cross_terms += coupling * x[i] * x[j]
        
        # Global scaling factor with chaotic modulation and adaptive exponent
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi / 7) + 0.2 * np.cos(self.dim * np.pi / 9)
        # Add adaptive exponent for nonlinearity
        adaptive_exp = 1.0 + 0.1 * np.sin(self.dim * np.pi / 10)
        scale_factor = scale_factor ** adaptive_exp
        
        # Combine all components with weighted contributions and chaotic weight adjustments
        weight1 = 0.25 + 0.05 * np.sin(self.dim * np.pi / 6)
        weight2 = 0.35 + 0.05 * np.cos(self.dim * np.pi / 7)
        weight3 = 0.20 + 0.05 * np.sin(self.dim * np.pi / 8)
        weight4 = 0.15 + 0.05 * np.cos(self.dim * np.pi / 9)
        
        # Add chaotic adjustment to weights
        weight1 *= (1.0 + 0.05 * np.sin(x[0] if len(x) > 0 else 0))
        weight2 *= (1.0 + 0.05 * np.cos(x[1] if len(x) > 1 else 0))
        weight3 *= (1.0 + 0.05 * np.sin(x[2] if len(x) > 2 else 0))
        weight4 *= (1.0 + 0.05 * np.cos(x[3] if len(x) > 3 else 0))
        
        return (weight1 * quantum_harmonic + 
                weight2 * fbm_effect + 
                weight3 * penalty + 
                weight4 * cross_terms) * scale_factor