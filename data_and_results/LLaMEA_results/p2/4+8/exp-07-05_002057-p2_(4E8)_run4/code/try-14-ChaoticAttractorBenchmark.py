import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define the central attractor point
        self.attractor = np.zeros(dim)
        # Generate random perturbation frequencies for each dimension
        self.frequencies = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension does not match the function dimension")
        
        # Central attractor term (quadratic)
        attractor_term = np.sum((x - self.attractor)**2) * 0.05
        
        # Sinusoidal perturbation terms with different frequencies
        sinusoidal_term = 0.0
        for i in range(self.dim):
            sinusoidal_term += np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Chaotic component using a simple chaotic map (logistic-like)
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i]) * np.cos(x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all terms with varying weights
        total = attractor_term + 0.5 * sinusoidal_term + 0.3 * chaotic_term
        
        # Add a small random noise to increase robustness
        noise = np.random.uniform(-0.01, 0.01)
        
        return total + noise