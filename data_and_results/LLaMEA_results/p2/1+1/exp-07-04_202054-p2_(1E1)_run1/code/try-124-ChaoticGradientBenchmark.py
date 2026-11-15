import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.1
        self.c = 0.05
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2) * 0.1
        
        # Chaotic sine-modulated components
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(self.a * x[i]) * np.cos(self.b * x[i]**2) * np.sin(self.c * x[i]**3)
        f_value += 2.0 * chaotic_sum
        
        # Embedded saddle points with varying curvature
        saddle_sum = 0.0
        for i in range(self.dim):
            saddle_sum += x[i]**4 - 2 * x[i]**2 + 0.5 * np.sin(10 * x[i])
        f_value += 0.5 * saddle_sum
        
        # Multi-scale interaction terms with exponential modulation
        interaction_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_sum += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        f_value += 0.3 * interaction_sum
        
        # Variable curvature regions with piecewise polynomial
        curvature_sum = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                curvature_sum += 0.8 * x[i]**5
            else:
                curvature_sum += 1.2 * x[i]**3
        f_value += 0.4 * curvature_sum
        
        # Add noise to increase irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        # Additional chaotic component with time-like parameter
        time_like = np.sum(x**2) / self.dim
        f_value += 0.2 * np.sin(10 * time_like) * np.cos(15 * time_like)
        
        return f_value