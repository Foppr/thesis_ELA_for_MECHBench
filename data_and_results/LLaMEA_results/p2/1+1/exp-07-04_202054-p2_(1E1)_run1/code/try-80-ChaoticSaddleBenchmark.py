import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.5
        self.c = 2.0
        self.d = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_value = np.sum(x**2)
        
        # Chaotic sine-based component with exponential decay
        for i in range(self.dim):
            f_value += 0.5 * np.sin(self.a * x[i]) * np.exp(-self.b * np.abs(x[i]))
            
        # Asymmetric basin structure with polynomial and trigonometric mix
        for i in range(self.dim):
            if x[i] >= 0:
                f_value += 0.3 * (x[i]**3) * np.cos(self.c * x[i])
            else:
                f_value += 0.3 * (x[i]**4) * np.sin(self.d * x[i])
                
        # Multi-scale correlation structure with exponentially decaying weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_factor = np.exp(-0.1 * (i + j))
                f_value += 0.2 * corr_factor * np.sin(2 * x[i]) * np.cos(3 * x[j])
                
        # Saddle-point perturbation with varying amplitude
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += np.sin(0.5 * x[i]) * np.cos(0.7 * x[i]) * np.sin(1.2 * x[i])
        f_value += 0.4 * saddle_term**2
        
        # Add asymmetric noise with exponential decay
        noise = np.random.normal(0, 0.05, self.dim)
        for i in range(self.dim):
            f_value += 0.1 * noise[i] * np.exp(-0.2 * np.abs(x[i]))
            
        # Fractional polynomial interactions for non-integer behavior
        for i in range(self.dim):
            f_value += 0.15 * x[i]**1.5 * np.sin(2.5 * x[i])
            
        # Cross-variable chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.05 * (i + j))
                
        return f_value