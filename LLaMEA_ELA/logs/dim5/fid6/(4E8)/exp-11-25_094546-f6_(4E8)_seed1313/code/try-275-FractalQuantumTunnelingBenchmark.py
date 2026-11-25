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
            
            # Fractal-based harmonic potential with multi-scale self-similarity
            fractal_potential = 0.0
            for k in range(1, 10):
                scale = 2**k
                fractal_potential += (1.0 / scale**1.5) * np.sin(scale * xi + k * 0.3) * np.cos(scale * xi * 0.5)
            
            # Quantum tunneling with dynamic barrier heights
            tunneling_effect = 0.0
            for k in range(1, 20):
                barrier_height = 1.0 + 0.5 * np.sin(k * xi + self.dim * 0.2)
                tunneling_effect += (1.0 / k**2.2) * np.exp(-k * barrier_height * np.abs(xi)) * np.sin(k * xi + 0.3 * k)
            
            # Dynamic phase transition component with time-varying parameters
            phase_transition = 0.8 * np.sin(self.dim * 0.4 + xi * 3.0) + 0.2 * np.cos(self.dim * 0.6 + xi * 5.0)
            
            # Cross-dimensional coupling with fractal interference patterns - modified interaction strengths
            cross_coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    coupling_strength = 1.5 / (1.0 + distance**2.5)  # Increased coupling strength
                    fractal_interaction = np.sin(xi * x_norm[j] * 7.0 + 0.2 * np.sin(i + j))
                    cross_coupling += coupling_strength * fractal_interaction
            
            # Dimension-dependent weighting with quantum-like probabilistic factors
            weight = 1.0 + 0.4 * np.sin(xi * 4.0) * np.cos(self.dim * 0.3) + 0.2 * np.cos(xi * 3.0)
            
            # Hyperchaotic resonance term with multi-frequency interactions - additional nonlinear terms
            resonance = 0.3 * np.sin(11.0 * xi + 0.5 * i) * np.cos(9.0 * xi - 0.2 * i) + \
                       0.15 * np.sin(17.0 * xi) + \
                       0.1 * np.sin(23.0 * xi + 0.1 * i**1.3) + \
                       0.05 * np.sin(31.0 * xi**3)  # Added cubic nonlinear term
            
            # Combine all components with weighted sum
            component = weight * (fractal_potential + tunneling_effect + phase_transition + 0.5 * cross_coupling + resonance)
            result += component**2
            
        # Global scaling with fractal dimension correction
        fractal_dim_correction = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 1.7) + 0.1 * np.cos(np.log(self.dim + 1) * 2.9)
        
        # Add multi-fractal interference pattern with varying scales
        interference_pattern = 0.0
        for scale in [3, 6, 12, 24]:
            interference_pattern += 0.08 * np.sin(self.dim * 0.3 + scale * np.sum(np.cos(x_norm * scale))) / scale
            
        # Final normalization and correction
        normalized_result = result / self.dim
        return fractal_dim_correction * normalized_result * (1.0 + interference_pattern)