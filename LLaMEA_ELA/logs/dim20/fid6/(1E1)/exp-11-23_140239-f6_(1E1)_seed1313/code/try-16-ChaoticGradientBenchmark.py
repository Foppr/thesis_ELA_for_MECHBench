import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.1
        self.c = 0.05
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic sequence
        chaotic_seq = np.zeros(self.dim)
        for i in range(self.dim):
            if i == 0:
                chaotic_seq[i] = 0.5
            else:
                chaotic_seq[i] = self.a * chaotic_seq[i-1] * (1 - chaotic_seq[i-1])
        
        # Apply chaotic modulation to input
        x_mod = x + self.b * np.sin(chaotic_seq) * np.cos(x)
        
        # Compute gradient-based chaotic function with multiple saddle points
        result = 0.0
        for i in range(self.dim):
            xi = x_mod[i]
            # Multiple quadratic terms with different curvatures and offsets
            result += (xi**2 - 4*xi + 4) * np.exp(-self.c * (xi - 1)**2)
            result += (xi**2 + 2*xi + 1) * np.exp(-self.c * (xi + 1)**2)
            result += (xi**2 - 6*xi + 9) * np.exp(-self.c * (xi - 3)**2)
            result += (xi**2 + 4*xi + 4) * np.exp(-self.c * (xi + 2)**2)
            
        # Add chaotic perturbation term
        chaotic_pert = np.sum(np.sin(10 * x_mod) * np.cos(5 * x_mod))
        
        return result + 0.1 * chaotic_pert - 10.0