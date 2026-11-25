import numpy as np

class SaddlePointFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal and saddle point parameters
        self.fractal_exp = np.random.rand(dim) * 0.5 + 0.5
        self.saddle_params = np.random.rand(dim) * 2.0 + 1.0
        self.coupling_strength = np.random.rand(dim, dim) * 0.3 + 0.1
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal-like curvature with varying exponents
            fractal_curvature = np.sum([
                (np.abs(xi)**(1.0 + self.fractal_exp[i] * np.sin(i))) * 
                np.cos(xi * (i + 1) * 2.0) for i in range(self.dim)
            ])
            
            # Saddle point dominance with multiple attracting/repelling forces
            saddle_force = np.sum([
                self.saddle_params[j] * np.tanh(xi - x_norm[j]) * 
                np.exp(-0.5 * (xi - x_norm[j])**2) for j in range(self.dim)
            ])
            
            # Dynamic coupling with varying strength based on dimension indices
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_strength[i, j] * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
            
            # Multi-scale oscillatory behavior with phase shifts
            oscillatory = 0.0
            for k in range(1, min(15, self.dim + 5)):
                oscillatory += (1.0 / k**1.5) * np.sin(k * xi + k * np.cos(i * 0.5))
            
            # Combine terms with adaptive weighting based on dimension
            weight = 1.0 + 0.2 * np.sin(i * 0.8) * np.cos(self.dim * 0.3)
            
            # Create saddle point dominance with fractal-like structure
            term = (weight * (fractal_curvature + saddle_force + coupling + oscillatory)**2 + 
                   0.1 * np.abs(xi)**3 + 0.05 * xi**4)
            
            result += term
            
        # Global scaling with fractal dimension correction
        global_scale = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.0) + \
                      0.1 * np.cos(np.log(self.dim + 1) * 2.5)
        
        return global_scale * result / self.dim