import numpy as np

class AdaptiveSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Base quadratic term with quantum-inspired curvature modulation
            curvature = 1.0 + 0.7 * np.sin(self.dim * 0.5 + i * 0.4) * np.cos(self.dim * 0.3 + i * 0.2) + 0.4 * np.sin(self.dim * 0.8 + i * 0.6)
            quadratic = curvature * xi**2
            
            # Multi-frequency periodic forcing with quantum phase coupling
            periodic_force = 1.2 * np.sin(4 * xi + 0.6 * i) + 0.8 * np.cos(7 * xi - 0.4 * i) + 0.5 * np.sin(11 * xi + 0.2 * i) + 0.3 * np.cos(13 * xi - 0.1 * i)
            
            # Asymmetric basin with quantum tunneling effect
            asymmetry = 0.4 * np.sin(self.dim * 0.3 + i * 0.5) * np.cos(xi * 2.5)
            basin_term = asymmetry * (xi**4 + 0.6 * xi**3 - 0.4 * xi**2 + 0.1 * xi)
            
            # Quantum-like saddle point interaction with phase interference
            saddle_interaction = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    phase = np.sin(3 * xi + 4 * x_norm[j] + 0.3 * i + 0.2 * j)
                    coupling_strength = 1.0 / (1.0 + distance**3.0)
                    saddle_interaction += coupling_strength * phase
            
            # Adaptive dimensionality scaling with quantum resonance
            dim_scaling = 1.0 + 0.3 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4) + 0.2 * np.sin(self.dim * 0.9) + 0.15 * np.cos(self.dim * 0.7)
            
            # Hyperdimensional quantum coupling with fractal modulation
            hyper_coupling = 0.12 * np.sin(np.sum(x_norm) * 2.0 + 0.4 * i) * np.cos(np.mean(x_norm) * 3.0 - 0.3 * i) * np.sin(self.dim * 0.5)
            
            # Chaotic modulation with quantum interference patterns
            chaotic_modulation = 0.15 * np.sin(17 * xi + 3.1 * i) * np.cos(13 * xi - 2.7 * i) + 0.1 * np.sin(19 * xi + 3.5 * i) * np.cos(15 * xi - 2.3 * i)
            
            # Fractal basin boundary with quantum tunneling
            fractal_boundary = 0.08 * np.sin(25 * xi + 4.2 * i) * np.cos(20 * xi - 3.8 * i) + 0.05 * np.sin(30 * xi + 4.7 * i)
            
            # Combine all terms with dimension-dependent weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.6) * np.cos(self.dim * 0.2) + 0.2 * np.cos(i * 0.4) * np.sin(self.dim * 0.15)
            
            # Final contribution for this dimension with quantum amplitude modulation
            amplitude_mod = 1.0 + 0.2 * np.sin(23 * xi + 5.1 * i) * np.cos(19 * xi - 4.7 * i)
            result += weight * (quadratic + periodic_force + basin_term + 0.7 * saddle_interaction + chaotic_modulation + hyper_coupling + fractal_boundary)**2 * dim_scaling * amplitude_mod
            
        # Global quantum correction with fractal scaling
        quantum_correction = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 2.1) + 0.18 * np.cos(np.log(self.dim + 1) * 3.2) + 0.12 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4)
        return quantum_correction * result / self.dim