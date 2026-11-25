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
            
            # Base quadratic term with dynamic curvature
            curvature = 1.0 + 0.6 * np.sin(self.dim * 0.4 + i * 0.3) + 0.4 * np.cos(self.dim * 0.6 + i * 0.2)
            quadratic = curvature * xi**2
            
            # Periodic forcing with amplitude modulation
            periodic_force = 1.0 * np.sin(3 * xi + 0.5 * i) + 0.5 * np.cos(5 * xi - 0.3 * i) + 0.3 * np.sin(7 * xi + 0.1 * i)
            
            # Asymmetric basin terms with dimension-dependent scaling
            asymmetry = 0.4 * np.sin(self.dim * 0.2 + i * 0.4) * np.cos(xi * 2.0)
            basin_term = asymmetry * (xi**3 + 0.5 * xi**2 - 0.3 * xi)
            
            # Dynamic saddle point interaction with stronger coupling
            saddle_interaction = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    saddle_interaction += (1.0 / (1.0 + distance**3.0)) * np.sin(2 * xi + 3 * x_norm[j] + 0.2 * i + 0.1 * j)
            
            # Adaptive dimensionality scaling
            dim_scaling = 1.0 + 0.3 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.3) + 0.15 * np.sin(self.dim * 0.7)
            
            # Multi-scale modulation with chaotic component
            chaotic_modulation = 0.15 * np.sin(11 * xi + 2.3 * i) * np.cos(9 * xi - 1.7 * i) + 0.08 * np.sin(15 * xi + 3.1 * i)
            
            # Add a new hyperdimensional coupling term with increased strength
            hyper_coupling = 0.12 * np.sin(np.sum(x_norm) * 1.5 + 0.3 * i) * np.cos(np.mean(x_norm) * 2.0 - 0.2 * i)
            
            # Combine all terms with dimension-dependent weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.5) * np.cos(self.dim * 0.15) + 0.15 * np.cos(i * 0.3)
            
            # Final contribution for this dimension
            result += weight * (quadratic + periodic_force + basin_term + 0.7 * saddle_interaction + chaotic_modulation + hyper_coupling)**2 * dim_scaling
            
        # Global scaling factor with quantum-like correction
        quantum_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 1.8) + 0.15 * np.cos(np.log(self.dim + 1) * 2.5) + 0.1 * np.sin(self.dim * 0.4)
        return quantum_correction * result / self.dim