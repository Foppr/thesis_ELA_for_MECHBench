import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Enhanced fractal-like ridge structures with stronger self-similar patterns
        for i in range(self.dim):
            ridge_sum = 0.0
            for k in range(1, 7):
                scale = 2**k
                freq = 2.5 * np.pi * scale  # Slightly increased frequency
                ridge_sum += (1.0 / scale**1.5) * np.sin(freq * x[i])
            result += 3.0 * ridge_sum**2
            
        # Modified quantum tunneling effects with enhanced probabilistic potential wells
        for i in range(self.dim):
            well_depth = 4.5 + 2.5 * np.sin(i * 0.6 + np.sum(x) * 0.25)  # Increased depth variability
            well_position = 1.2 * np.cos(i * 0.4 + np.sum(x) * 0.35)  # Slightly shifted position
            tunneling_effect = well_depth * np.exp(-0.5 * ((x[i] - well_position) / 0.7)**2)
            result += tunneling_effect
            
        # Improved dynamic energy wells with stronger interactions
        for i in range(self.dim):
            well_energy = 0.0
            for j in range(min(4, self.dim)):
                pos = 2.2 * np.cos(i * 0.3 + j * 0.25 + np.sum(x) * 0.2)  # Slight shift in position
                depth = 2.8 + 0.9 * np.sin(i * j * 0.15 + np.sum(x) * 0.3)  # Increased depth variation
                width = 0.8 + 0.3 * np.cos(i + j * 0.5)  # Slight change in width
                well_energy += depth * np.exp(-0.5 * ((x[i] - pos) / width)**2)
            result += 0.9 * well_energy  # Increased weight
            
        # Enhanced multi-scale harmonic interference with stronger quantum phase coupling
        for i in range(self.dim):
            scale = 2**(i % 4 + 1)
            phase = 0.7 * np.sin(i * 0.35 + np.sum(x) * 0.2)  # Slightly increased phase modulation
            result += 2.2 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.4 + phase)
            
        # Enhanced fractal dimensionality effect with stronger recursive scaling
        fractal_factor = 1.0
        for k in range(1, 5):
            if self.dim >= k:
                fractal_factor += 0.5 * np.sin(np.sum(x[:k]) * 0.3 + k * 0.25)  # Increased fractal influence
        result *= fractal_factor
        
        # Enhanced quantum-like interference terms with stronger amplitude modulation
        quantum_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = 1.8 * np.cos(0.4 * (x[i] + x[j]) + np.sum(x) * 0.15)  # Increased coupling
                quantum_terms += coupling * np.exp(-0.5 * (distance / 0.5)**2)
        result += 0.7 * quantum_terms  # Slightly increased contribution
        
        # Enhanced asymmetric exponential barrier with stronger quantum scaling
        barrier_scale = 1.6 + 0.9 * np.sin(self.dim * 0.4 + np.sum(x) * 0.25)  # Increased scale
        for i in range(self.dim):
            result += barrier_scale * np.exp(2.2 * abs(x[i]) / 5.0) * (1 + 0.5 * np.sin(x[i] * 3.0))  # Slightly increased barrier
            
        # Additional enhanced fractal harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 5.5 + 3.0 * np.sin(r * 0.15)  # Increased frequency
            result += 2.2 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.3)
            
        return result