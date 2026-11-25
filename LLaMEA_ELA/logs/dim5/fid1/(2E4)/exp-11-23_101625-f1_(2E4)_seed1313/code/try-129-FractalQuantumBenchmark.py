import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Fractal-like ridge structures with self-similar patterns
        for i in range(self.dim):
            # Multi-scale fractal ridges with varying amplitudes
            ridge_sum = 0.0
            for k in range(1, 6):
                scale = 2**k
                freq = 2.0 * np.pi * scale
                ridge_sum += (1.0 / scale) * np.sin(freq * x[i])
            result += 2.8 * ridge_sum**2
            
        # Quantum tunneling effects with probabilistic potential wells
        for i in range(self.dim):
            # Create dynamic energy wells with quantum-like behavior
            well_depth = 3.5 + 1.2 * np.sin(i * 0.75 + np.sum(x) * 0.22)
            well_position = 1.8 * np.cos(i * 0.55 + np.sum(x) * 0.32)
            tunneling_effect = well_depth * np.exp(-0.5 * ((x[i] - well_position) / 0.7)**2)
            result += tunneling_effect
            
        # Dynamic energy wells with time-varying parameters
        for i in range(self.dim):
            # Create multiple interacting wells
            well_energy = 0.0
            for j in range(min(3, self.dim)):
                pos = 2.8 * np.cos(i * 0.42 + j * 0.32 + np.sum(x) * 0.16)
                depth = 2.2 + 0.4 * np.sin(i * j * 0.22 + np.sum(x) * 0.26)
                width = 0.75 + 0.35 * np.cos(i + j)
                well_energy += depth * np.exp(-0.5 * ((x[i] - pos) / width)**2)
            result += 0.8 * well_energy
            
        # Multi-scale harmonic interference with quantum phase coupling
        for i in range(self.dim):
            scale = 2**(i % 3 + 1)
            phase = 0.45 * np.sin(i * 0.42 + np.sum(x) * 0.19)
            result += 1.9 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.52 + phase)
            
        # Fractal dimensionality effect with recursive scaling
        fractal_factor = 1.05
        for k in range(1, 4):
            if self.dim >= k:
                fractal_factor += 0.35 * np.sin(np.sum(x[:k]) * 0.26 + k * 0.32)
        result *= fractal_factor
        
        # Quantum-like interference terms with complex amplitude modulation
        quantum_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = 1.1 * np.cos(0.32 * (x[i] + x[j]) + np.sum(x) * 0.11)
                quantum_terms += coupling * np.exp(-0.5 * (distance / 0.58)**2)
        result += 0.55 * quantum_terms
        
        # Asymmetric exponential barrier with quantum scaling
        barrier_scale = 1.15 + 0.65 * np.sin(self.dim * 0.37 + np.sum(x) * 0.22)
        for i in range(self.dim):
            result += barrier_scale * np.exp(1.9 * abs(x[i]) / 5.0) * (1 + 0.32 * np.sin(x[i] * 2.6))
            
        # Additional fractal harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 4.2 + 1.8 * np.sin(r * 0.13)
            result += 1.6 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.27)
            
        return result