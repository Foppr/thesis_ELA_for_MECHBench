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
            result += 2.5 * ridge_sum**2
            
        # Quantum tunneling effects with probabilistic potential wells
        for i in range(self.dim):
            # Create dynamic energy wells with quantum-like behavior
            well_depth = 3.0 + 1.5 * np.sin(i * 0.7 + np.sum(x) * 0.2)
            well_position = 2.0 * np.cos(i * 0.5 + np.sum(x) * 0.3)
            tunneling_effect = well_depth * np.exp(-0.5 * ((x[i] - well_position) / 0.8)**2)
            result += tunneling_effect
            
        # Dynamic energy wells with time-varying parameters
        for i in range(self.dim):
            # Create multiple interacting wells
            well_energy = 0.0
            for j in range(min(3, self.dim)):
                pos = 3.0 * np.cos(i * 0.4 + j * 0.3 + np.sum(x) * 0.15)
                depth = 2.0 + 0.5 * np.sin(i * j * 0.2 + np.sum(x) * 0.25)
                width = 0.8 + 0.3 * np.cos(i + j)
                well_energy += depth * np.exp(-0.5 * ((x[i] - pos) / width)**2)
            result += 0.7 * well_energy
            
        # Multi-scale harmonic interference with quantum phase coupling
        for i in range(self.dim):
            scale = 2**(i % 3 + 1)
            phase = 0.5 * np.sin(i * 0.4 + np.sum(x) * 0.18)
            result += 1.8 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.5 + phase)
            
        # Fractal dimensionality effect with recursive scaling
        fractal_factor = 1.0
        for k in range(1, 4):
            if self.dim >= k:
                fractal_factor += 0.3 * np.sin(np.sum(x[:k]) * 0.25 + k * 0.3)
        result *= fractal_factor
        
        # Quantum-like interference terms with complex amplitude modulation
        quantum_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = 1.2 * np.cos(0.3 * (x[i] + x[j]) + np.sum(x) * 0.1)
                quantum_terms += coupling * np.exp(-0.5 * (distance / 0.6)**2)
        result += 0.5 * quantum_terms
        
        # Asymmetric exponential barrier with quantum scaling
        barrier_scale = 1.2 + 0.6 * np.sin(self.dim * 0.35 + np.sum(x) * 0.2)
        for i in range(self.dim):
            result += barrier_scale * np.exp(1.8 * abs(x[i]) / 5.0) * (1 + 0.3 * np.sin(x[i] * 2.5))
            
        # Additional fractal harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            fractal_freq = 4.0 + 2.0 * np.sin(r * 0.12)
            result += 1.5 * np.sin(fractal_freq * r) * np.cos(fractal_freq * r * 0.25)
            
        return result