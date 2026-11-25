import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coefficients = np.random.uniform(-1.0, 1.0, dim)
        self.frequency = np.random.uniform(1.0, 5.0, dim)
        self.power_exponents = np.random.uniform(2.0, 4.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term
        basin_term = np.sum(self.coefficients * (x ** self.power_exponents))
        
        # Sinusoidal oscillation term with cross-terms
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(self.frequency[i] * x[i]) * np.cos(self.frequency[i] * x[i])
            for j in range(i+1, self.dim):
                oscillation_term += 0.1 * np.sin(x[i] * x[j]) * np.cos(x[i] * x[j])
        
        # Cross-terms creating complex interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] - x[j])**2 * np.sin(0.5 * (x[i] + x[j]))
        
        # Add chaotic element with small random perturbation
        chaotic_factor = 0.01 * np.sum(np.sin(x * 13.0))
        
        return basin_term + oscillation_term + cross_term + chaotic_factor