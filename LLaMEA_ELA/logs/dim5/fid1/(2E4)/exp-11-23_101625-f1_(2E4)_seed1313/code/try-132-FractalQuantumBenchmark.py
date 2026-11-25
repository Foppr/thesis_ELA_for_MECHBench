import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced scaling
        result = 0.2 * np.sum(x**2)
        
        # Enhanced fractal ridge structures with dynamic scaling
        for i in range(self.dim):
            ridge_sum = 0.0
            for k in range(1, 8):
                scale = 3**k
                freq = 3.0 * np.pi * scale
                ridge_sum += (1.0 / (scale * 1.5)) * np.sin(freq * x[i])
            result += 3.2 * ridge_sum**2
            
        # Enhanced quantum tunneling effects with dynamic wells
        for i in range(self.dim):
            well_depth = 4.0 + 1.8 * np.sin(i * 0.9 + np.sum(x) * 0.3)
            well_position = 2.2 * np.cos(i * 0.7 + np.sum(x) * 0.4)
            tunneling_effect = well_depth * np.exp(-0.5 * ((x[i] - well_position) / 0.8)**2)
            result += tunneling_effect
            
        # Multi-scale interacting wells with dynamic parameters
        for i in range(self.dim):
            well_energy = 0.0
            for j in range(min(4, self.dim)):
                pos = 3.1 * np.cos(i * 0.5 + j * 0.4 + np.sum(x) * 0.2)
                depth = 2.8 + 0.6 * np.sin(i * j * 0.3 + np.sum(x) * 0.3)
                width = 0.9 + 0.4 * np.cos(i + j)
                well_energy += depth * np.exp(-0.5 * ((x[i] - pos) / width)**2)
            result += 1.1 * well_energy
            
        # Multi-scale harmonic interference with enhanced phase coupling
        for i in range(self.dim):
            scale = 3**(i % 4 + 1)
            phase = 0.6 * np.sin(i * 0.5 + np.sum(x) * 0.25)
            result += 2.4 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.6 + phase)
            
        # Enhanced fractal dimensionality effect with recursive scaling
        fractal_factor = 1.1
        for k in range(1, 5):
            if self.dim >= k:
                fractal_factor += 0.4 * np.sin(np.sum(x[:k]) * 0.3 + k * 0.4)
        result *= fractal_factor
        
        # Enhanced quantum-like interference terms with complex modulation
        quantum_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = 1.5 * np.cos(0.4 * (x[i] + x[j]) + np.sum(x) * 0.15)
                quantum_terms += coupling * np.exp(-0.5 * (distance / 0.6)**2)
        result += 0.7 * quantum_terms
        
        # Enhanced asymmetric exponential barrier with dynamic scaling
        barrier_scale = 1.3 + 0.8 * np.sin(self.dim * 0.4 + np.sum(x) * 0.25)
        for i in range(self.dim):
            result += barrier_scale * np.exp(2.2 * abs(x[i]) / 5.0) * (1 + 0.4 * np.sin(x[i] * 3.0))
            
        # Additional enhanced fractal harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 5.0 + 2.2 * np.sin(r * 0.15)
            result += 2.1 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.3)
            
        # Additional high-frequency chaotic modulation
        chaos_factor = 0.0
        for i in range(self.dim):
            chaos_factor += np.sin(7.0 * x[i] + np.sum(x) * 0.5) * np.cos(4.0 * x[i])
        result += 0.8 * chaos_factor
        
        return result