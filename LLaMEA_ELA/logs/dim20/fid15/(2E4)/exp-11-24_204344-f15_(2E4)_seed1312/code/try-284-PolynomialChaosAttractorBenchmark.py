import numpy as np

class PolynomialChaosAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequences for time-varying dynamics
        self.chaos_seq = np.sin(np.arange(dim) * 0.3 + 1.0)
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion with mixed monomials and chaotic weights
        chaos_poly = 0.0
        for i in range(self.dim):
            w = 1.0 + 0.5 * self.chaos_seq[i] * np.sin(i * 0.7)
            chaos_poly += w * (x[i]**3 - 2*x[i]**2 + x[i]) * np.cos(x[i] * 0.5)
        
        # Adaptive radial basis functions with time-varying centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / self.dim) * np.sin(self.chaos_seq[i] * 2.0)
            width = 0.3 + 0.7 * np.cos(i * 0.5) * (1.0 + 0.2 * np.sin(self.chaos_seq[i]))
            radial += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(x[i] * 0.3)
        
        # Gradient-based attractor field with dynamic attraction points and varying strengths
        attractor = 0.0
        for i in range(self.dim):
            strength = 1.5 + 0.5 * np.cos(i * 0.4 + self.chaos_seq[i])
            target = 2.0 * np.sin(i * 0.6) * np.cos(self.chaos_seq[i])
            attractor += strength * (x[i] - target)**2 * np.exp(-0.1 * (x[i] - target)**2)
        
        # Time-varying coupling terms with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.3 * np.sin(i * j * 0.2 + self.chaos_seq[i] + self.chaos_seq[j])
                coupling += mod * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (x[i]**2 + x[j]**2)
        
        # Multi-scale fractal-like structure with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.8 + self.chaos_seq[i])
            fractal += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.7) * np.exp(-0.05 * x[i]**2)
        
        # Dynamic harmonic landscape with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.4 * np.cos(i * 0.3 + self.chaos_seq[i])
            harmonic += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.8) * (1.0 + 0.2 * np.sin(x[i]))
        
        # Combine all terms with adaptive weighting
        total = 0.2 * chaos_poly + 0.25 * radial + 0.2 * attractor + 0.15 * coupling + 0.1 * fractal + 0.1 * harmonic
        
        # Global scaling with chaotic modulation based on dimensionality
        global_scale = 1.0 + 0.3 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.3)
        
        return total * global_scale