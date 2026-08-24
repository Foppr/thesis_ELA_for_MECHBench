import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_value = 0.0
        
        # Chaotic logistic map component
        for i in range(self.dim):
            # Logistic map with parameter r_i
            logistic_val = 0.5  # Initial value
            for _ in range(10):  # Iterate to reach chaotic regime
                logistic_val = self.r_values[i] * logistic_val * (1 - logistic_val)
            f_value += 0.5 * logistic_val * np.sin(x[i] + self.phase_shifts[i])**2
        
        # Sinusoidal modulation with varying frequencies
        for i in range(self.dim):
            f_value += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(5 * x[i])
            
        # Saddle-point interactions with multiple variables
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                f_value += 0.2 * (x[i]**2 - x[j]**2) * np.sin(3 * (x[i] + x[j]))
                
        # Multi-scale chaotic sine waves
        f_value += 0.4 * np.sum(np.sin(15 * x) * np.cos(12 * x) * np.sin(8 * x))
        
        # Cross-variable polynomial interactions with chaotic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = np.sin(self.r_values[i] * self.r_values[j])
                f_value += 0.15 * coeff * x[i]**3 * x[j]**2 * np.cos(4 * x[i] + 2 * x[j])
                
        # High-frequency chaotic perturbations
        for i in range(self.dim):
            f_value += 0.25 * np.sin(50 * x[i] + np.sin(20 * x[i])) * np.cos(30 * x[i] + np.cos(15 * x[i]))
            
        # Polynomial chaos with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.3 * x[i]**9 * np.sin(6 * x[i])
            
        # Additional chaotic cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.1 * np.sin(25 * x[i] + 10 * x[j]) * np.cos(15 * x[i] - 5 * x[j]) * (x[i]**2 + x[j]**2)
                
        # Add a global scaling factor based on chaotic dynamics
        chaotic_factor = np.mean([np.sin(self.r_values[i]) for i in range(self.dim)])
        f_value *= (1.0 + 0.2 * chaotic_factor)
        
        return f_value