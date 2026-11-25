import numpy as np

class ChaoticTentPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Tent map chaotic component with parameter control
        chaos_term = 0.0
        a = 1.8  # Chaotic parameter
        for i in range(self.dim):
            tent_val = x_scaled[i] if x_scaled[i] < 0.5 else 1 - x_scaled[i]
            chaos_term += a * tent_val * (1 - tent_val)
            
        # Polynomial interaction terms with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**2 + x[j]**3) * (i + j + 1)
                
        # Quaternion-inspired rotational symmetry with complex interactions
        rot_symmetry = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi, xj = x_scaled[i], x_scaled[i+1]
                rot_symmetry += (xi**2 + xj**2) * np.sin(xi * xj * 3) * np.cos(xi * xj * 2)
                
        # Fractal-like component using recursive sine and cosine combinations
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(10 * np.sin(5 * x[i])) + 0.5 * np.cos(8 * np.cos(3 * x[i]))
            
        # Cross-dimensional coupling with exponential decay
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += np.exp(-abs(x[i] - x[j]) / (i + j + 1)) * (x[i]**2 + x[j]**2)
                    
        # Adaptive scaling based on coordinate magnitude
        adaptive_scale = 1.0
        for i in range(self.dim):
            adaptive_scale *= (1 + 0.3 * np.sin(x[i] * 0.5) * np.cos(x[i] * 0.7))
            
        # Combine all terms with different weights and add global minimum offset
        return (chaos_term + poly_term + rot_symmetry + fractal_term + 
                coupling_term + adaptive_scale + 3.0)