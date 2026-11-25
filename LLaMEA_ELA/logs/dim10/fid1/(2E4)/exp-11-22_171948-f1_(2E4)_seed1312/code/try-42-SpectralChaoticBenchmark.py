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
        
        # Polynomial chaos expansion component with enhanced nonlinearity
        for i in range(self.dim):
            poly_term = (x[i]**7 + 0.6 * x[i]**5 + 0.4 * x[i]**3 + 0.2 * x[i]) * self.weights[i]
            result += poly_term
        
        # Spectral decomposition with dynamic frequencies and phase shifts
        for i in range(self.dim):
            spec_component = np.sin(self.freqs[i] * x[i] + np.cos(x[i])) * np.cos(0.3 * x[i]**2 + 0.1 * x[i])
            result += 1.0 * spec_component
        
        # Multi-scale harmonic interference with amplitude modulation
        for i in range(self.dim):
            harmonic_sum = (np.sin(7 * x[i]) + 
                           0.8 * np.sin(21 * x[i]) + 
                           0.4 * np.sin(63 * x[i]) +
                           0.1 * np.sin(126 * x[i]))
            result += 0.7 * harmonic_sum**2
        
        # Cross-dimensional coupling with frequency modulation and phase locking
        for i in range(self.dim - 1):
            coupling_freq = 1.5 + 0.8 * np.sin(x[i] * x[i+1])
            coupling = np.exp(-0.4 * (x[i] - x[i+1])**2) * np.sin(coupling_freq * (x[i] + x[i+1]) + np.cos(x[i] - x[i+1]))
            result += 0.5 * coupling
        
        # Adaptive conditioning with dimension-dependent scaling and dynamic exponents
        condition_factor = 1.0 + 0.7 * np.cos(self.dim * 0.15)
        for i in range(self.dim):
            conditioned_poly = condition_factor * (x[i]**6 - 0.9 * x[i]**4 + 0.3 * x[i]**2 + 0.1 * x[i])
            result += 0.4 * conditioned_poly
        
        # Fractal-like structure with recursive scaling and multi-fractal dimensions
        for i in range(self.dim):
            fractal_term = np.sin(15 * x[i]) * np.exp(-0.15 * x[i]**2) + \
                          0.6 * np.cos(30 * x[i]) * np.exp(-0.08 * x[i]**2) + \
                          0.3 * np.sin(45 * x[i]) * np.exp(-0.05 * x[i]**2)
            result += 0.6 * fractal_term
        
        # Chaotic modulation with time-like dependency and memory effects
        chaotic_mod = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.8) * np.pi + 0.5 * np.sin(x[i])
            chaotic_mod += np.sin(15 * x[i] + phase) * np.cos(7 * x[i] + phase)
        result += 0.5 * chaotic_mod
        
        # Multi-modal ridge structure with varying amplitudes and dynamic peaks
        for i in range(self.dim):
            ridge = (np.sin(10 * x[i]) + 
                    0.7 * np.sin(30 * x[i]) + 
                    0.3 * np.sin(90 * x[i]) +
                    0.1 * np.sin(180 * x[i]))
            result += 0.8 * ridge**3
        
        # Dynamic global scaling based on solution quality with memory
        global_scale = 1.0 + 0.4 * np.sin(np.sum(x**2) / self.dim + 0.5 * np.sum(np.abs(x)))
        result *= global_scale
        
        # Add novel hyper-chaotic cross-term interactions
        for i in range(self.dim - 2):
            hyper_term = np.sin(3 * x[i]) * np.cos(4 * x[i+1]) * np.sin(5 * x[i+2])
            result += 0.3 * hyper_term
        
        # Add dimensionally dependent noise modulation
        noise_mod = np.random.randn() * 0.1
        for i in range(self.dim):
            noise_mod += np.sin(x[i] * (i + 1)) * 0.05
        result += noise_mod
        
        # Normalize by dimension and add final chaotic scaling
        result /= self.dim
        result *= (1.0 + 0.2 * np.sin(self.dim))
        
        return result