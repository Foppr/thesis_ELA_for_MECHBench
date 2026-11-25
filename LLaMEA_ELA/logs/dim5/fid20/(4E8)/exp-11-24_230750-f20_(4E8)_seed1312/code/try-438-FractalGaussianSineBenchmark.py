import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for logistic map
        self.logistic_r = np.random.uniform(3.57, 4.0, dim)
        self.gaussian_centers = np.random.uniform(-2.0, 2.0, dim)
        self.gaussian_widths = np.random.uniform(0.3, 1.5, dim)
        # Fractal dimension and scaling factors
        self.fractal_dims = np.random.uniform(1.1, 2.9, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like Gaussian peaks with varying dimensions
        fractal_gaussian = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Add fractal scaling based on dimension
            fractal_factor = np.power(2.0, self.fractal_dims[i])
            fractal_gaussian += np.exp(-0.5 * ((x[i] - center) / (sigma * fractal_factor))**2)
        
        # Memory-enhanced sine-wave couplings with chaotic modulation
        memory_sine = 0.0
        prev_x = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map for chaotic modulation
            logistic_val = self.logistic_r[i] * xi * (1 - xi)
            # Memory effect with sine coupling
            memory_sine += np.sin(2 * np.pi * xi + 0.5 * np.sin(prev_x)) * np.exp(-0.1 * logistic_val**2)
            prev_x = xi
        
        # Adaptive conditioning based on fractal dimension and position
        conditioning = 0.0
        for i in range(self.dim):
            # Dimensional conditioning factor
            cond_factor = 1.0 + 0.5 * np.sin(0.3 * x[i]) * (self.fractal_dims[i] - 1.0)
            # Position-based conditioning
            pos_cond = 1.0 + 0.2 * np.cos(0.4 * x[i])
            conditioning += cond_factor * pos_cond
        
        # Deceptive gradient component with multiple local optima
        deceptive = 0.0
        for i in range(self.dim):
            # Add multiple sine waves with different frequencies and phases
            deceptive += (np.sin(3 * np.pi * x[i]) + 
                         0.5 * np.sin(9 * np.pi * x[i]) + 
                         0.2 * np.sin(15 * np.pi * x[i]))
        
        # Cross-dimensional cubic couplings with chaotic weights
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Chaotic weight based on logistic map
                weight = 1.0 + 0.3 * np.sin(self.logistic_r[i] * x[i] * (1 - x[i]))
                cubic_coupling += weight * (x[i]**3 - x[j]**3) * np.cos(0.5 * (x[i] + x[j]))
        
        # Combine all components with dynamic scaling
        dim_factor = 1.0 + 0.2 * np.log(self.dim)
        return (0.30 * fractal_gaussian + 0.25 * memory_sine + 
                0.20 * conditioning + 0.15 * deceptive + 0.10 * cubic_coupling) * dim_factor