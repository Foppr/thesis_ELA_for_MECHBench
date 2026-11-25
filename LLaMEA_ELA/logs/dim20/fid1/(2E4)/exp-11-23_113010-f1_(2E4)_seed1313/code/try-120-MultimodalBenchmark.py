import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components with varying condition numbers
        rbf_sum = 0.0
        for i in range(self.dim):
            # Adaptive condition number based on dimension and index
            cond_num = 10**(0.5 + 0.3 * np.sin(i * np.pi / self.dim))
            # Radial basis with Gaussian kernel
            rbf_sum += np.exp(-cond_num * np.sum((x_norm - np.sin(i * np.pi / self.dim))**2))
        
        # Embedded saddle point structure with hyperbolic tangent modulations
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Saddle point interaction with varying strength
                strength = 0.5 * (1 + np.tanh((i - j) / self.dim))
                saddle_term += strength * np.tanh(x_norm[i]) * np.tanh(x_norm[j])
        
        # Multi-scale periodic modulation with frequency coupling
        periodic_mod = 0.0
        for i in range(self.dim):
            freq = 2**(i + 1) * (1 + 0.3 * np.sin(i * np.pi / self.dim))
            periodic_mod += np.cos(freq * x_norm[i]) * np.sin(freq * x_norm[i]**2)
        
        # Adaptive basin depth with fractal-like scaling
        basin_depth = 0.0
        for i in range(self.dim):
            # Fractal scaling with dimension-dependent exponents
            exponent = 1.5 + 0.5 * np.sin(i * np.pi / self.dim)
            basin_depth += np.abs(x_norm[i])**exponent
        
        # Cross-dimensional coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Weighted interaction with dimension-dependent coupling strength
                weight = (i + 1) * (j + 1) / ((self.dim + 1)**2)
                coupling_term += weight * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # Global scaling factor with dimension-dependent adjustment
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) / (1 + np.abs(np.log(self.dim + 1)))
        
        # Combine all components
        return scale_factor * (2.0 * rbf_sum + 1.5 * saddle_term + 1.0 * periodic_mod + 
                              0.8 * basin_depth + 0.6 * coupling_term)