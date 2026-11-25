import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with exponentially increasing scales
        for i in range(self.dim):
            result += (x[i] ** 2) * np.exp(0.1 * i)
            
        # Add multiple local minima using sine waves with chaotic frequency modulation
        for i in range(self.dim):
            freq = 3 ** (i % 5) + 2 * np.sin(i * 0.7)  # Chaotic frequency modulation
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add a complex penalty term with multiple local optima using hybrid functions
        penalty = 0.0
        for i in range(self.dim):
            # Hybrid polynomial and logarithmic penalty with exponential scaling
            penalty += (x[i] ** 11 + x[i] ** 7 + x[i] ** 5 + np.log(1 + abs(x[i]))) * np.exp(0.15 * i)
            
        # Add enhanced cross-dimensional interactions with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction strength and multi-modal nonlinear component
                interaction_strength = np.sin(i * 0.5) * np.cos(j * 0.3) * (i + j)
                cross_term += interaction_strength * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.2 * abs(x[i] - x[j])) * np.log(1 + abs(x[i] * x[j] + 0.1 * np.sin(x[i] + x[j])))
                
        # Add a novel chaotic attractor-like term for increased complexity
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i]) * np.cos(x[(i + 2) % self.dim]) * np.tan(0.5 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        return result + 0.15 * penalty + 0.25 * cross_term + 0.1 * chaotic_term