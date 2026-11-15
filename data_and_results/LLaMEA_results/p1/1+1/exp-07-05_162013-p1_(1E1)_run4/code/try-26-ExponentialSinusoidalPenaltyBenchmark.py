import numpy as np

class ExponentialSinusoidalPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters
        self.adaptive_factors = np.random.uniform(0.5, 2.0, dim)
        self.sinusoidal_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with adaptive rates
        for i in range(self.dim):
            result += self.adaptive_factors[i] * np.exp(-self.decay_rates[i] * np.abs(x[i]))
            
        # Sinusoidal modulation with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(self.sinusoidal_frequencies[i] * x[i])
            
        # Cross-term sinusoidal coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(self.sinusoidal_frequencies[i] * x[i] + self.sinusoidal_frequencies[j] * x[j])
                
        # Adaptive penalty landscape
        penalty_center = np.random.uniform(-2.0, 2.0, self.dim)
        for i in range(self.dim):
            result += 0.2 * (x[i] - penalty_center[i])**2 * (1 + 0.1 * np.abs(x[i]))
            
        # Multi-scale oscillation component
        for i in range(self.dim):
            result += 0.1 * np.sin(50 * x[i]) * np.cos(30 * x[i])
            
        # Asymmetric saddle point attraction
        for i in range(self.dim):
            result += 0.05 * (x[i]**3 - 3*x[i])
            
        return result