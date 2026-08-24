import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms with chaotic scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.2)**2 + (x[i] + 1.2)**2 + 0.015 * x[i]**4 + 0.003 * x[i]**6
        
        # Chaotic interaction terms with exponential and sinusoidal coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use chaotic scaling with sine modulation
                interaction_strength = np.exp(1.5 * (i + j)) * (1.0 + 0.3 * np.sin(i * j))
                result += interaction_strength * (x[i] - x[j])**2
        
        # Saddle point structure with chaotic sinusoidal modulation
        for i in range(self.dim):
            result += 0.9 * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i]) + 0.4 * np.sin(5.5 * x[i])
        
        # Complex global minimum with nested curvature and high-order polynomial terms
        result += 0.003 * np.sum(x**2) + 0.0008 * np.sum(x**6) + 0.0002 * np.sum(x**8)
        
        # Highly periodic and chaotic component with nested frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4.5 * x[i]) * np.cos(3.5 * x[i]) + 0.6 * np.sin(6.5 * x[i])
        result += 0.2 * periodic_term
        
        # Shifted global minimum with chaotic offset and higher-order polynomial
        result += 0.8 * np.sum((x - 0.4)**2) + 0.1 * np.sum((x - 0.4)**4) + 0.05 * np.sum((x - 0.4)**6)
        
        # Add chaotic noise component with varying amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(12.0 * x[i]) * np.cos(8.0 * x[i]) * (1.0 + 0.2 * np.sin(i))
        result += noise
        
        # Add a nested multimodal structure with dynamic scaling
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.5 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) + 0.2 * np.sin(9.0 * x[i])
        result += 0.1 * nested_term
        
        return result