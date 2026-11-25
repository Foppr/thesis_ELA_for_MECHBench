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
                freq = 2.0 * np.pi * scale
                ridge_sum += (1.0 / scale**1.5) * np.sin(freq * x[i])
            result += 3.0 * ridge_sum**2
            
        # Modified quantum tunneling effects with enhanced probabilistic potential wells
        for i in range(self.dim):
            well_depth = 4.0 + 2.0 * np.sin(i * 0.6 + np.sum(x) * 0.25)
            well_position = 1.5 * np.cos(i * 0.4 + np.sum(x) * 0.35)
            tunneling_effect = well_depth * np.exp(-0.5 * ((x[i] - well_position) / 0.7)**2)
            result += tunneling_effect
            
        # Improved dynamic energy wells with stronger interactions
        for i in range(self.dim):
            well_energy = 0.0
            for j in range(min(4, self.dim)):
                pos = 2.5 * np.cos(i * 0.3 + j * 0.25 + np.sum(x) * 0.2)
                depth = 2.5 + 0.8 * np.sin(i * j * 0.15 + np.sum(x) * 0.3)
                width = 0.9 + 0.4 * np.cos(i + j * 0.5)
                well_energy += depth * np.exp(-0.5 * ((x[i] - pos) / width)**2)
            result += 0.8 * well_energy
            
        # Enhanced multi-scale harmonic interference with stronger quantum phase coupling
        for i in range(self.dim):
            scale = 2**(i % 4 + 1)
            phase = 0.6 * np.sin(i * 0.35 + np.sum(x) * 0.2)
            result += 2.0 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.4 + phase)
            
        # Enhanced fractal dimensionality effect with stronger recursive scaling
        fractal_factor = 1.0
        for k in range(1, 5):
            if self.dim >= k:
                fractal_factor += 0.4 * np.sin(np.sum(x[:k]) * 0.3 + k * 0.25)
        result *= fractal_factor
        
        # Enhanced quantum-like interference terms with stronger amplitude modulation
        quantum_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = 1.5 * np.cos(0.4 * (x[i] + x[j]) + np.sum(x) * 0.15)
                quantum_terms += coupling * np.exp(-0.5 * (distance / 0.5)**2)
        result += 0.6 * quantum_terms
        
        # Enhanced asymmetric exponential barrier with stronger quantum scaling
        barrier_scale = 1.5 + 0.8 * np.sin(self.dim * 0.4 + np.sum(x) * 0.25)
        for i in range(self.dim):
            result += barrier_scale * np.exp(2.0 * abs(x[i]) / 5.0) * (1 + 0.4 * np.sin(x[i] * 3.0))
            
        # Additional enhanced fractal harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 5.0 + 2.5 * np.sin(r * 0.15)
            result += 2.0 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.3)
            
        return result