import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequency factors and interference patterns
        self.freq_factors = np.random.rand(dim) * 3 + 1
        self.interference_coeffs = np.random.rand(dim, dim) * 0.5 + 0.5
        self.harmonic_weights = np.random.rand(dim) * 2 + 1
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base trigonometric components with adaptive frequencies
        base_terms = []
        for i in range(self.dim):
            freq = self.freq_factors[i]
            term = np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
            term += 0.5 * np.sin(2 * freq * x_scaled[i]) * np.cos(2 * freq * x_scaled[i])
            term += 0.3 * np.sin(3 * freq * x_scaled[i]) * np.cos(3 * freq * x_scaled[i])
            base_terms.append(term)
        
        # Spatially varying harmonic interference patterns
        interference = []
        for i in range(self.dim):
            inter_term = 0.0
            for j in range(self.dim):
                coeff = self.interference_coeffs[i][j]
                inter_term += coeff * np.sin(x_scaled[i] + x_scaled[j])
            interference.append(inter_term)
        
        # Multi-scale harmonic modulation with position-dependent weights
        modulated_terms = []
        for i in range(self.dim):
            weight = self.harmonic_weights[i] * (1.0 + 0.3 * np.sin(5 * x_scaled[i]))
            modulated_terms.append(weight * base_terms[i])
        
        # Cross-dimensional coupling with varying strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x_scaled[i] * x_scaled[j]) * np.sin(2 * np.pi * (x_scaled[i] + x_scaled[j]))
        
        # Adaptive amplitude modulation based on global position
        pos_mod = 1.0 + 0.5 * np.sin(np.sum(x_scaled**2))
        
        # Combine all components with proper normalization
        result = pos_mod * (np.sum(modulated_terms) + 0.3 * np.sum(interference) + 
                           0.2 * coupling)
        
        # Add controlled noise for robustness
        noise = 0.01 * np.random.rand() * np.exp(-np.sum(x_scaled**2))
        return result + noise