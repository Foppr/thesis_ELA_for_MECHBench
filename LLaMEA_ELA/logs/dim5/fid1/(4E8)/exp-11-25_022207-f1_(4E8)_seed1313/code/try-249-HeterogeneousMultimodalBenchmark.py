import numpy as np

class HeterogeneousMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial component with varying degrees and adaptive weights
        poly_term = np.sum((x_norm**3 + 0.5 * x_norm**5 + 0.2 * x_norm**7) * 
                          (1.0 + 0.3 * np.sin(2.0 * np.pi * x_norm)))
        
        # Trigonometric component with frequency modulation and phase shifts
        trig_term = np.sum(np.sin(4.0 * np.pi * x_norm) * 
                          np.cos(3.0 * np.pi * x_norm) * 
                          np.exp(-0.5 * x_norm**2))
        
        # Radial basis function component with dynamic centers and widths
        rbf_term = 0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            width = 0.3 + 0.2 * np.sin(0.5 * np.pi * i)
            rbf_term += np.exp(-0.5 * ((x_norm - centers[i]) / width)**2)
        
        # Cross-dimensional interaction term with coupling strength
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i] * x_norm[i+1]) * np.sin(3.0 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_factor = np.sum(1.0 / (1.0 + np.exp(-2.0 * x_norm)) * 
                           np.cos(2.0 * np.pi * x_norm) * 
                           (1.0 + 0.1 * np.abs(x_norm)))
        
        # Asymmetric saddle point with dynamic parameters
        saddle_term = np.sum((x_norm**2 - 0.5 * x_norm**4)**2 * 
                          np.exp(-0.3 * x_norm**2) * 
                          np.sin(5.0 * np.pi * x_norm))
        
        # Combined function with adaptive noise
        result = poly_term + trig_term + rbf_term + cross_term + cond_factor + saddle_term
        
        # Add controlled noise for robustness
        noise = 0.02 * np.random.randn() * (1.0 + 0.15 * np.std(x_norm))
        
        return result + noise