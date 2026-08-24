import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.shift_params = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - self.shift_params[i])**2 + 0.01 * x[i]**4 + 0.001 * x[i]**6
        
        # Nested sinusoidal modulation with chaotic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with dynamic scaling
                scale = self.chaos_params[i] * self.chaos_params[j]
                result += scale * np.sin(2.0 * np.pi * (x[i] + x[j])) * np.cos(3.0 * np.pi * (x[i] - x[j]))
        
        # Asymmetric saddle points with varying curvature
        for i in range(self.dim):
            # Asymmetric term: different behavior for positive vs negative x
            if x[i] >= 0:
                result += 0.5 * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i]) + 0.2 * x[i]**3
            else:
                result += 0.3 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) + 0.1 * x[i]**5
        
        # Dynamic global minimum based on dimensionality
        dynamic_shift = np.sum(np.sin(np.arange(1, self.dim + 1) * 0.5) * self.shift_params)
        result += 0.005 * np.sum((x - dynamic_shift)**2)
        
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(self.chaos_params[i] * x[i]) * np.cos(self.chaos_params[i] * x[i] * 0.7)
        result += noise
        
        # Add higher-order polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.002 * (x[i]**2 + x[j]**2) * (x[i] - x[j])**2
        
        return result