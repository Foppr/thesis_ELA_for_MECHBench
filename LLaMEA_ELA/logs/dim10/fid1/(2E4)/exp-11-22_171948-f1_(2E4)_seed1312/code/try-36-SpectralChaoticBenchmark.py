import numpy as np

class SpectralChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spectral weights for chaotic behavior
        self.weights = np.random.randn(dim)
        self.freqs = 2 + np.sin(np.arange(dim)) * 3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_term = (x[i]**6 + 0.5 * x[i]**4 + 0.3 * x[i]**2) * self.weights[i]
            result += poly_term
        
        # Spectral decomposition with dynamic frequencies
        for i in range(self.dim):
            spec_component = np.sin(self.freqs[i] * x[i]) * np.cos(0.5 * x[i]**2)
            result += 0.8 * spec_component
        
        # Multi-scale harmonic interference
        for i in range(self.dim):
            harmonic_sum = (np.sin(5 * x[i]) + 
                           0.7 * np.sin(15 * x[i]) + 
                           0.3 * np.sin(45 * x[i]))
            result += 0.6 * harmonic_sum**2
        
        # Cross-dimensional coupling with frequency modulation
        for i in range(self.dim - 1):
            coupling_freq = 1 + 0.5 * np.sin(x[i] + x[i+1])
            coupling = np.exp(-0.3 * (x[i] - x[i+1])**2) * np.sin(coupling_freq * (x[i] + x[i+1]))
            result += 0.4 * coupling
        
        # Adaptive conditioning with dimension-dependent scaling
        condition_factor = 1.0 + 0.5 * np.cos(self.dim * 0.1)
        for i in range(self.dim):
            conditioned_poly = condition_factor * (x[i]**5 - 0.8 * x[i]**3 + 0.2 * x[i])
            result += 0.3 * conditioned_poly
        
        # Fractal-like structure with recursive scaling
        for i in range(self.dim):
            fractal_term = np.sin(10 * x[i]) * np.exp(-0.1 * x[i]**2) + \
                          0.5 * np.cos(20 * x[i]) * np.exp(-0.05 * x[i]**2)
            result += 0.5 * fractal_term
        
        # Chaotic modulation with time-like dependency
        chaotic_mod = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.7) * np.pi
            chaotic_mod += np.sin(12 * x[i] + phase) * np.cos(6 * x[i] + phase)
        result += 0.4 * chaotic_mod
        
        # Multi-modal ridge structure with varying amplitudes
        for i in range(self.dim):
            ridge = (np.sin(8 * x[i]) + 
                    0.6 * np.sin(24 * x[i]) + 
                    0.2 * np.sin(72 * x[i]))
            result += 0.7 * ridge**3
        
        # Dynamic global scaling based on solution quality
        global_scale = 1.0 + 0.3 * np.sin(np.sum(x**2) / self.dim)
        result *= global_scale
        
        # Normalize by dimension
        result /= self.dim
        
        return result