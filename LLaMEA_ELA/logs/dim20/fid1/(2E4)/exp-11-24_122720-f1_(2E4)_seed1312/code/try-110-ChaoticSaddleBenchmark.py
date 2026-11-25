import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            phase = 0.5 * np.cos(i * np.pi / (self.dim + 2))
            quantum_harmonic += np.sin(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Fractional Brownian motion effect with Hurst parameter modulation
        fbm_effect = 0
        hurst = 0.3 + 0.4 * np.sin(self.dim * np.pi / 8)
        for i in range(self.dim):
            fbm_effect += (np.random.normal(0, 1) * 
                          np.exp(-hurst * abs(x[i])) * 
                          np.cos(hurst * x[i]))
        
        # Adaptive penalty landscape with dynamic threshold
        penalty = 0
        for i in range(self.dim):
            threshold = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 3))
            if abs(x[i]) > threshold:
                penalty += 10.0 * (abs(x[i]) - threshold)**2
        
        # Nested sinusoidal modulations with dynamic frequencies
        nested_modulation = 0
        for i in range(self.dim):
            freq1 = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 4))
            freq2 = 0.5 + 1.0 * np.cos(i * np.pi / (self.dim + 5))
            nested_modulation += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Dynamic coupling weights with chaotic modulation
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength using logistic map
                r = 3.8 + 0.2 * np.sin(i * np.pi / (self.dim + 6))
                coupling = r * np.sin(x[i]) * np.cos(x[j])
                cross_terms += coupling * x[i] * x[j]
        
        # Global scaling factor with chaotic modulation
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi / 7) + 0.2 * np.cos(self.dim * np.pi / 9)
        
        # Combine all components with weighted contributions
        weight1 = 0.25 + 0.05 * np.sin(self.dim * np.pi / 6)
        weight2 = 0.35 + 0.05 * np.cos(self.dim * np.pi / 7)
        weight3 = 0.20 + 0.05 * np.sin(self.dim * np.pi / 8)
        weight4 = 0.15 + 0.05 * np.cos(self.dim * np.pi / 9)
        
        return (weight1 * quantum_harmonic + 
                weight2 * fbm_effect + 
                weight3 * penalty + 
                weight4 * cross_terms) * scale_factor