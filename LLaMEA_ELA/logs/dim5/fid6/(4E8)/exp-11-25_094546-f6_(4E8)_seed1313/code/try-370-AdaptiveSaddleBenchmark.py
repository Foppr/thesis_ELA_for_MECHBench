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
            
            # Enhanced quantum-inspired curvature with phase modulation
            phase = np.sin(self.dim * 0.7 + i * 0.4) + 0.3 * np.cos(self.dim * 0.9 + i * 0.2)
            curvature = 1.5 + 0.8 * np.sin(2 * xi + phase) + 0.4 * np.cos(3 * xi - phase)
            quadratic = curvature * xi**2
            
            # Multi-frequency chaotic forcing with dynamic amplitude
            chaotic_force = 0.0
            for freq in [1, 2, 3, 5, 7]:
                amp = 0.6 * np.sin(self.dim * 0.3 + i * 0.1) * np.cos(self.dim * 0.2 + i * 0.3)
                chaotic_force += amp * np.sin(freq * xi + 0.5 * i + 0.1 * freq)
            
            # Asymmetric basin with quantum tunneling probability
            tunnel_prob = 0.2 * np.sin(xi * 3.0) * np.cos(xi * 2.0)
            basin_term = tunnel_prob * (xi**4 - 0.5 * xi**3 + 0.2 * xi**2 - 0.1 * xi)
            
            # Enhanced saddle point interaction with quantum coupling
            saddle_interaction = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    coupling_strength = 0.8 * np.sin(self.dim * 0.5 + i * 0.3) * np.cos(self.dim * 0.4 + j * 0.2)
                    saddle_interaction += coupling_strength * (1.0 / (1.0 + distance**3.0)) * np.sin(3 * xi + 2 * x_norm[j] + 0.3 * i + 0.2 * j)
            
            # Hyperdimensional phase locking with adaptive scaling
            dim_scaling = 1.0 + 0.3 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4) + 0.2 * np.sin(self.dim * 0.8)
            
            # Multi-scale quantum modulation with entanglement coupling
            quantum_modulation = 0.15 * np.sin(13 * xi + 2.7 * i) * np.cos(11 * xi - 1.9 * i) + \
                               0.1 * np.sin(17 * xi + 3.3 * i) * np.cos(14 * xi - 2.1 * i) + \
                               0.08 * np.sin(19 * xi + 3.7 * i)
            
            # Hyperdimensional tunneling coupling
            hyper_coupling = 0.12 * np.sin(np.sum(x_norm) * 2.0 + 0.4 * i) * np.cos(np.mean(x_norm) * 3.0 - 0.3 * i)
            
            # Phase-locked adaptive weighting
            weight = 1.2 + 0.3 * np.sin(i * 0.6) * np.cos(self.dim * 0.2) + \
                    0.2 * np.cos(i * 0.4) * np.sin(self.dim * 0.15) + \
                    0.15 * np.sin(i * 0.8) * np.cos(self.dim * 0.3)
            
            # Final contribution with enhanced nonlinearity
            result += weight * (quadratic + chaotic_force + basin_term + 0.7 * saddle_interaction + quantum_modulation + hyper_coupling)**3 * dim_scaling
            
        # Global quantum correction with adaptive phase locking
        quantum_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 2.0) + \
                           0.15 * np.cos(np.log(self.dim + 1) * 2.8) + \
                           0.12 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.6)
        
        # Add entanglement-induced interference term
        entanglement_term = 0.05 * np.sin(np.sum(x_norm) * 4.0) * np.cos(np.prod(x_norm) * 2.0)
        
        return (quantum_correction * result / self.dim) + entanglement_term