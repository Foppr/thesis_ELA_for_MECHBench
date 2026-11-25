import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaos_factor = 3.8
        self.noise_level = 0.1
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial valley component with varying exponents
        polynomial_valley = np.sum(x_scaled**6) + 0.5 * np.sum(x_scaled**8)
        
        # Sinusoidal chaos component using logistic map-like behavior
        chaos = 0.0
        for i in range(self.dim):
            # Apply chaotic transformation to each dimension
            chaotic_value = np.sin(np.pi * x_scaled[i] * self.chaos_factor)
            chaos += chaotic_value**2
            
        # Saddle point structure with cross-terms
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                saddle += (x_scaled[i]**2 - x_scaled[j]**2) * np.sin(3 * x_scaled[i] * x_scaled[j])
        
        # Sharp transition regions with exponential dampening
        transitions = 0.0
        for i in range(self.dim):
            # Create sharp peaks using modified Gaussian-like functions
            peak_height = np.exp(-0.5 * (x_scaled[i] - 0.3)**2) + 0.5 * np.exp(-0.5 * (x_scaled[i] + 0.7)**2)
            transitions += peak_height
        
        # Noise injection for increased complexity
        noise = self.noise_level * np.sum(np.random.normal(0, 1, self.dim) * x_scaled)
        
        # Combine all components with different weights
        return 4.0 * polynomial_valley + 3.0 * chaos + 2.5 * saddle + 1.5 * transitions + 0.5 * noise