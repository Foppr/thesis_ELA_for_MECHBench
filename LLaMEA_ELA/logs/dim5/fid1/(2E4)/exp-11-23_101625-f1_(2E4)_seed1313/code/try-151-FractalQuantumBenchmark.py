import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced scaling
        result = 0.3 * np.sum(x**2)
        
        # Enhanced fractal ridge structures with multi-scale interference
        for i in range(self.dim):
            ridge_sum = 0.0
            for k in range(1, 10):
                scale = 4**k
                freq = 3.0 * np.pi * scale  # Increased frequency
                ridge_sum += (1.0 / (scale * 2.0)) * np.sin(freq * x[i])
            result += 5.0 * ridge_sum**2
            
        # Modified quantum tunneling with enhanced well interactions
        for i in range(self.dim):
            well_depth = 5.2 + 2.1 * np.sin(i * 1.1 + np.sum(x) * 0.42)
            well_position = 3.0 * np.cos(i * 0.8 + np.sum(x) * 0.55)
            tunneling_effect = well_depth * np.exp(-0.5 * ((x[i] - well_position) / 0.7)**2)
            result += tunneling_effect
            
        # Complex dynamic energy wells with cross-dimensional coupling
        for i in range(self.dim):
            well_energy = 0.0
            for j in range(min(5, self.dim)):
                pos = 3.8 * np.cos(i * 0.6 + j * 0.5 + np.sum(x) * 0.3)
                depth = 3.7 + 0.8 * np.sin(i * j * 0.4 + np.sum(x) * 0.45)
                width = 0.95 + 0.5 * np.cos(i + j * 0.8)
                well_energy += depth * np.exp(-0.5 * ((x[i] - pos) / width)**2)
            result += 1.5 * well_energy
            
        # Enhanced harmonic interference with modified phase coupling
        for i in range(self.dim):
            scale = 4**(i % 5 + 1)
            phase = 0.7 * np.sin(i * 0.65 + np.sum(x) * 0.35)
            result += 3.2 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.7 + phase)
            
        # Advanced fractal dimensionality effect with recursive scaling
        fractal_factor = 1.4
        for k in range(1, 6):
            if self.dim >= k:
                fractal_factor += 0.6 * np.sin(np.sum(x[:k]) * 0.4 + k * 0.5)
        result *= fractal_factor
        
        # Complex quantum interference terms with multi-dimensional coupling
        quantum_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                distance = np.abs(x[i] - x[j])
                coupling = 2.2 * np.cos(0.5 * (x[i] + x[j]) + np.sum(x) * 0.22)  # Increased coupling
                quantum_terms += coupling * np.exp(-0.5 * (distance / 0.7)**2)
        result += 1.0 * quantum_terms
        
        # Enhanced asymmetric exponential barrier with multi-scale scaling
        barrier_scale = 2.0 + 1.1 * np.sin(self.dim * 0.5 + np.sum(x) * 0.38)  # Increased scale
        for i in range(self.dim):
            result += barrier_scale * np.exp(3.0 * abs(x[i]) / 5.0) * (1 + 0.5 * np.sin(x[i] * 3.5))
            
        # Additional complex fractal harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 7.0 + 3.2 * np.sin(r * 0.22)
            result += 2.8 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.4)
            
        # Cross-dimensional coupling with modified interaction weights
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction = (x[i]**2 + x[j]**2) * np.cos(0.3 * (x[i] - x[j]))  # Slightly modified
                cross_terms += cross_interaction
        result += 0.8 * cross_terms
        
        return result