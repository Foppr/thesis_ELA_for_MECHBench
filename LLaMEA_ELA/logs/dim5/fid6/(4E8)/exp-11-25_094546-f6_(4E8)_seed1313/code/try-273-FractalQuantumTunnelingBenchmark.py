import numpy as np

class FractalQuantumTunnelingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal harmonic potential with nested self-similarity
            fractal_potential = 0.0
            for k in range(1, 15):
                scale = 3**k
                fractal_potential += (1.0 / scale**1.7) * np.sin(scale * xi + k * 0.4) * np.cos(scale * xi * 0.6)
            
            # Enhanced quantum tunneling with adaptive barrier heights and multi-scale tunneling
            tunneling_effect = 0.0
            for k in range(1, 25):
                barrier_height = 1.5 + 0.8 * np.sin(k * xi + self.dim * 0.3) * np.cos(k * 0.2)
                tunneling_effect += (1.0 / k**2.5) * np.exp(-k * barrier_height * np.abs(xi)) * np.sin(k * xi + 0.4 * k)
            
            # Dynamic phase transition with multi-frequency modulation
            phase_transition = 1.0 * np.sin(self.dim * 0.5 + xi * 4.0) + 0.3 * np.cos(self.dim * 0.7 + xi * 6.0) + 0.2 * np.sin(xi * 8.0)
            
            # Enhanced cross-dimensional coupling with fractal interference patterns
            cross_coupling = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    coupling_strength = 1.0 / (1.0 + distance**3.0)
                    fractal_interaction = np.sin(xi * x_norm[j] * 8.0 + 0.3 * np.sin(i + j))
                    cross_coupling += coupling_strength * fractal_interaction
            
            # Enhanced dimension-dependent weighting with quantum-like probabilistic factors
            weight = 1.2 + 0.5 * np.sin(xi * 5.0) * np.cos(self.dim * 0.4) + 0.3 * np.cos(xi * 4.0) + 0.1 * np.sin(xi * 7.0)
            
            # Hyperchaotic resonance with multi-frequency interactions and time-varying parameters
            resonance = 0.4 * np.sin(13.0 * xi + 0.6 * i) * np.cos(10.0 * xi - 0.3 * i) + \
                       0.2 * np.sin(19.0 * xi) + \
                       0.15 * np.sin(25.0 * xi + 0.15 * i**1.4) + \
                       0.1 * np.cos(31.0 * xi - 0.2 * i)
            
            # Multi-scale interference terms
            interference = 0.0
            for scale in [2, 4, 8, 16]:
                interference += 0.05 * np.sin(self.dim * 0.4 + scale * np.sum(np.cos(x_norm * scale))) / scale
            
            # Combine all components with weighted sum
            component = weight * (fractal_potential + tunneling_effect + phase_transition + 0.6 * cross_coupling + resonance + interference)
            result += component**2
            
        # Global scaling with enhanced fractal dimension correction
        fractal_dim_correction = 1.2 + 0.4 * np.sin(np.log(self.dim + 1) * 2.0) + 0.2 * np.cos(np.log(self.dim + 1) * 3.2)
        
        # Add multi-fractal interference pattern with varying scales and enhanced complexity
        interference_pattern = 0.0
        for scale in [4, 8, 16, 32]:
            interference_pattern += 0.1 * np.sin(self.dim * 0.4 + scale * np.sum(np.cos(x_norm * scale))) / scale
            
        # Add adaptive difficulty factor based on dimensionality
        difficulty_factor = 1.0 + 0.3 * np.sin(self.dim * 0.2) * np.cos(self.dim * 0.1)
        
        # Final normalization and correction
        normalized_result = result / self.dim
        return fractal_dim_correction * normalized_result * (1.0 + interference_pattern) * difficulty_factor