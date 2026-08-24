import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed terms
        poly_chaos = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**3) + 0.2 * np.sum(x_norm**2)
        
        # Radial basis function with multiple centers and varying widths
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(len(centers)):
            for j in range(len(centers)):
                if i != j:
                    rbf_sum += np.exp(-10.0 * ((x_norm[i] - centers[i])**2 + (x_norm[j] - centers[j])**2))
        
        # Coupled harmonic oscillators with frequency modulation
        harmonic_sum = 0.0
        for i in range(min(4, self.dim)):
            freq = 2.0 + 0.5 * i
            harmonic_sum += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Cross-term with sigmoidal coupling
        cross_coupling = 0.0
        for i in range(min(3, self.dim)):
            for j in range(i+1, min(3, self.dim)):
                cross_coupling += (1.0 / (1.0 + np.exp(-x_norm[i] - x_norm[j]))) * np.sin(x_norm[i] * x_norm[j])
        
        # Add noise-like perturbation using trigonometric polynomials
        noise_like = 0.0
        for i in range(min(6, self.dim)):
            noise_like += np.sin(10.0 * x_norm[i]) * np.cos(5.0 * x_norm[i])
        
        # Combine all components with dimensionality-dependent scaling
        dim_factor = 1.0 + 0.1 * (self.dim - 1)
        result = (0.3 * poly_chaos + 
                 0.25 * rbf_sum + 
                 0.2 * harmonic_sum + 
                 0.15 * cross_coupling + 
                 0.1 * noise_like) * dim_factor
        
        return result