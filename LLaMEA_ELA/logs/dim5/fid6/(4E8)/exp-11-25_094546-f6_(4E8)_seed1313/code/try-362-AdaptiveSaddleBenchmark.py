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
            curvature = 1.0 + 0.6 * np.sin(self.dim * 0.3 + i * 0.4) + 0.4 * np.cos(self.dim * 0.5 + i * 0.2)
            quadratic = curvature * xi**2
            
            # Enhanced periodic forcing with multi-frequency components
            periodic_force = 1.0 * np.sin(4 * xi + 0.6 * i) + 0.6 * np.cos(7 * xi - 0.4 * i) + 0.3 * np.sin(10 * xi + 0.2 * i) + 0.2 * np.cos(13 * xi - 0.1 * i)
            
            # Asymmetric basin terms with stronger nonlinearity
            asymmetry = 0.4 * np.sin(self.dim * 0.3 + i * 0.5) * np.cos(xi * 3.0)
            basin_term = asymmetry * (xi**4 + 0.6 * xi**3 - 0.4 * xi**2 - 0.2 * xi)
            
            # Enhanced saddle point interaction with long-range coupling
            saddle_interaction = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    saddle_interaction += (1.0 / (1.0 + distance**3.0)) * np.sin(3 * xi + 4 * x_norm[j] + 0.3 * i + 0.2 * j)
            
            # Improved dimensionality scaling with exponential component
            dim_scaling = 1.0 + 0.3 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4) + 0.15 * np.sin(self.dim * 0.8) + 0.05 * np.exp(-0.02 * self.dim)
            
            # Chaotic modulation with higher frequency components
            chaotic_modulation = 0.15 * np.sin(13 * xi + 2.5 * i) * np.cos(11 * xi - 1.9 * i) + 0.1 * np.sin(17 * xi + 3.3 * i) * np.cos(14 * xi - 2.1 * i) + 0.08 * np.sin(20 * xi + 4.1 * i)
            
            # Stronger hyperdimensional coupling term
            hyper_coupling = 0.12 * np.sin(np.sum(x_norm) * 2.0 + 0.4 * i) * np.cos(np.mean(x_norm) * 3.0 - 0.3 * i)
            
            # Combine all terms with enhanced weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.6) * np.cos(self.dim * 0.2) + 0.2 * np.cos(i * 0.4) + 0.1 * np.sin(self.dim * 0.3)
            
            # Final contribution for this dimension
            result += weight * (quadratic + periodic_force + basin_term + 0.7 * saddle_interaction + chaotic_modulation + hyper_coupling)**2 * dim_scaling
            
        # Improved global scaling factor with enhanced quantum-like correction
        quantum_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 2.0) + 0.15 * np.cos(np.log(self.dim + 1) * 3.0) + 0.1 * np.sin(self.dim * 0.5) + 0.05 * np.cos(self.dim * 0.7)
        return quantum_correction * result / self.dim