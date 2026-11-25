import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute angular frequencies and decay rates
        self.omega = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        self.decay = np.array([0.1 + 0.3 * np.cos(i * 0.6) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with angular dependence
        for i in range(self.dim):
            result += self.decay[i] * np.exp(-self.omega[i] * np.abs(x[i])) * (1 + 0.2 * np.sin(self.omega[i] * x[i]))
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(self.omega[i] * x[i]) * np.cos(self.omega[j] * x[j])
                result += 0.3 * coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Spherical harmonic component with varying degrees
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            spherical_term = 0.0
            for i in range(self.dim):
                spherical_term += x[i] * np.sin(r) * np.cos(i * np.pi / self.dim)
            result += 0.2 * spherical_term / r
            
        # Add a modified Rastrigin-like periodic component
        rastrigin_term = 0.0
        for i in range(self.dim):
            rastrigin_term += x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) + 10
        result += 0.1 * rastrigin_term
        
        # Add a cubic polynomial with cross-terms for increased complexity
        cubic_term = 0.0
        for i in range(self.dim):
            cubic_term += 0.05 * x[i]**3 * np.sin(x[i])
        result += cubic_term
        
        # Add noise component to increase irregularity
        noise = 0.005 * np.sum(np.cos(x * 15) * np.sin(x * 7))
        result += noise
        
        # Add a new twist: introduce a modified Ackley-like term for enhanced multimodality
        ackley_term = 0.0
        sum1 = np.sum(x**2)
        sum2 = np.sum(np.cos(2 * np.pi * x))
        ackley_term = -20 * np.exp(-0.2 * np.sqrt(sum1 / self.dim)) - np.exp(sum2 / self.dim) + 20 + np.e
        result += 0.03 * ackley_term
        
        return result