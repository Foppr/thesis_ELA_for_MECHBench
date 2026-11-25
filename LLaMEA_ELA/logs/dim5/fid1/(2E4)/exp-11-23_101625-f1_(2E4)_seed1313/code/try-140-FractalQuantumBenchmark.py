import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced scaling
        result = 0.2 * np.sum(x**2)
        
        # Enhanced fractal ridge structures with multi-scale interference
        for i in range(self.dim):
            ridge_sum = 0.0
            for k in range(1, 8):
                scale = 3**k
                freq = 3.0 * np.pi * scale
                ridge_sum += (1.0 / (scale * 1.5)) * np.sin(freq * x[i])
            result += 4.2 * ridge_sum**2
            
        # Modified quantum tunneling with enhanced well interactions
        for i in range(self.dim):
            well_depth = 4.8 + 1.8 * np.sin(i * 0.9 + np.sum(x) * 0.35)
            well_position = 2.5 * np.cos(i * 0.7 + np.sum(x) * 0.48)
            tunneling_effect = well_depth * np.exp(-0.5 * ((x[i] - well_position) / 0.6)**2)
            result += tunneling_effect
            
        # Complex dynamic energy wells with cross-dimensional coupling
        for i in range(self.dim):
            well_energy = 0.0
            for j in range(min(4, self.dim)):
                pos = 3.2 * np.cos(i * 0.55 + j * 0.4 + np.sum(x) * 0.25)
                depth = 3.1 + 0.6 * np.sin(i * j * 0.3 + np.sum(x) * 0.38)
                width = 0.85 + 0.4 * np.cos(i + j * 0.7)
                well_energy += depth * np.exp(-0.5 * ((x[i] - pos) / width)**2)
            result += 1.2 * well_energy
            
        # Enhanced harmonic interference with modified phase coupling
        for i in range(self.dim):
            scale = 3**(i % 4 + 1)
            phase = 0.6 * np.sin(i * 0.55 + np.sum(x) * 0.28)
            result += 2.8 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.65 + phase)
            
        # Advanced fractal dimensionality effect with recursive scaling
        fractal_factor = 1.2
        for k in range(1, 5):
            if self.dim >= k:
                fractal_factor += 0.5 * np.sin(np.sum(x[:k]) * 0.35 + k * 0.42)
        result *= fractal_factor
        
        # Complex quantum interference terms with multi-dimensional coupling
        quantum_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                distance = np.abs(x[i] - x[j])
                coupling = 1.5 * np.cos(0.4 * (x[i] + x[j]) + np.sum(x) * 0.18)
                quantum_terms += coupling * np.exp(-0.5 * (distance / 0.65)**2)
        result += 0.8 * quantum_terms
        
        # Enhanced asymmetric exponential barrier with multi-scale scaling
        barrier_scale = 1.4 + 0.8 * np.sin(self.dim * 0.45 + np.sum(x) * 0.32)
        for i in range(self.dim):
            result += barrier_scale * np.exp(2.3 * abs(x[i]) / 5.0) * (1 + 0.4 * np.sin(x[i] * 3.1))
            
        # Additional complex fractal harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 5.8 + 2.5 * np.sin(r * 0.18)
            result += 2.4 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.35)
            
        # Cross-dimensional coupling with modified interaction weights
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction = (x[i]**2 + x[j]**2) * np.cos(0.2 * (x[i] - x[j]))
                cross_terms += cross_interaction
        result += 0.6 * cross_terms
        
        return result