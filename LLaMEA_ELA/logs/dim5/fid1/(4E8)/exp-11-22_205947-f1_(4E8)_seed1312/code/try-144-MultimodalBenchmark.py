import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compound harmonic oscillation with multiple frequencies
        oscillation_sum = 0.0
        for i in range(self.dim):
            oscillation_sum += (np.sin(2 * np.pi * x[i]) + 
                               0.5 * np.sin(4 * np.pi * x[i]) + 
                               0.3 * np.sin(8 * np.pi * x[i]))
        
        # Multi-scale Gaussian interference with dynamic centers
        gaussian_interference = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.5) * 2.5
            gaussian_interference += np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.1 * i))**2)
        
        # Cross-dimensional resonance with adaptive coupling
        resonance = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * x[i] * x[j])
                resonance += coupling
        
        # Dynamic conditioning based on dimensionality and position
        r = np.sqrt(np.sum(x**2))
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.5) * np.cos(r * 0.2)
        
        # Spectral modulation with frequency-dependent weights
        spectral_mod = 0.0
        for i in range(self.dim):
            freq_weight = 1.0 + 0.3 * np.sin(i * 0.8)
            spectral_mod += freq_weight * np.cos(3 * x[i]) * np.sin(2 * x[i])
        
        # Compound landscape with multiple interaction terms
        return condition_factor * (0.6 * oscillation_sum + 
                                  0.3 * gaussian_interference + 
                                  0.2 * resonance + 
                                  0.1 * spectral_mod)