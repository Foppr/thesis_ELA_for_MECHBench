import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for chaotic behavior
        self.coefficients = np.random.uniform(0.5, 2.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        self.amplitudes = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Apply domain clipping to ensure x is within [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2) * 0.01
        
        # Sinusoidal modulation with chaotic parameters
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += self.amplitudes[i] * np.sin(self.frequencies[i] * x[i]) * np.cos(self.coefficients[i] * x[i])
        
        # Exponential barrier terms to create sharp gradients near boundaries
        barriers = 0.0
        for i in range(self.dim):
            barriers += np.exp(10.0 * (x[i] - 5.0)) + np.exp(10.0 * (-5.0 - x[i]))
        
        # Add a chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            if i == 0:
                prev_val = x[-1]
            else:
                prev_val = x[i-1]
            chaotic += np.sin(3.0 * x[i] + 0.5 * prev_val) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components
        result = quadratic - sinusoidal + barriers + chaotic
        
        return result