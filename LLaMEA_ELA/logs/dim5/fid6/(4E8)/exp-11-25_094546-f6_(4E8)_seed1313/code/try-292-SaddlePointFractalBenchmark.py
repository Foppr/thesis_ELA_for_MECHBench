import numpy as np

class SaddlePointFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal and saddle point parameters with improved conditioning
        self.fractal_exp = np.random.rand(dim) * 0.8 + 0.3
        self.saddle_params = np.random.rand(dim) * 1.5 + 0.5
        self.coupling_strength = np.random.rand(dim, dim) * 0.4 + 0.2
        # Add more structured coupling for better conditioning
        self.coupling_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.coupling_matrix[i, j] = np.sin((i - j) * 0.5) * 0.3 + 0.7
        # Add phase shifts for better complexity
        self.phase_shifts = np.random.rand(dim) * np.pi
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal-like curvature with varying exponents and phase shifts
            fractal_curvature = 0.0
            for j in range(min(10, self.dim)):
                if j < self.dim:
                    exponent = 1.0 + self.fractal_exp[j] * np.sin(xi * (j + 1) * 0.7 + self.phase_shifts[j])
                    fractal_curvature += (np.abs(xi)**exponent) * np.cos(xi * (j + 1) * 1.5)
            
            # Saddle point dominance with modified attracting/repelling forces
            saddle_force = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = xi - x_norm[j]
                    saddle_force += self.saddle_params[j] * np.tanh(diff) * np.exp(-0.3 * diff**2)
            
            # Enhanced dynamic coupling with structured matrix
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_matrix[i, j] * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
            
            # Multi-scale oscillatory behavior with improved frequency control
            oscillatory = 0.0
            for k in range(1, min(20, self.dim + 10)):
                freq = k * (1.0 + 0.1 * np.sin(i * 0.3))
                oscillatory += (1.0 / k**1.2) * np.sin(freq * xi + k * np.cos(i * 0.4))
            
            # Combine terms with adaptive weighting based on dimension
            weight = 1.0 + 0.3 * np.sin(i * 0.6) * np.cos(self.dim * 0.2)
            
            # Create enhanced saddle point dominance with fractal-like structure
            term = (weight * (fractal_curvature + saddle_force + coupling + oscillatory)**2 + 
                   0.15 * np.abs(xi)**3 + 0.08 * xi**4)
            
            result += term
            
        # Global scaling with improved fractal dimension correction
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 2.0) + \
                      0.15 * np.cos(np.log(self.dim + 1) * 1.5)
        
        return global_scale * result / self.dim