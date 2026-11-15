import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.5
        self.beta = 2.0
        self.gamma = 1.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_exp = np.exp(-self.alpha * r)
        
        # Sinusoidal waves in each dimension with varying frequencies
        wave_sum = 0
        for i in range(self.dim):
            wave_sum += np.sin(self.beta * x[i]) * np.cos(self.gamma * x[i])
        
        # Polynomial radial terms with different powers
        poly_radial = 0
        for i in range(self.dim):
            poly_radial += x[i]**4 + x[i]**3 - 2*x[i]**2
        
        # Cross-terms creating multimodal behavior
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Additional exponential interaction terms
        exp_interaction = 0
        for i in range(self.dim):
            exp_interaction += np.exp(-self.gamma * np.abs(x[i])) * np.sin(self.beta * x[i])
        
        # Combine all components
        return (0.5 * radial_exp + 
                1.2 * wave_sum + 
                0.8 * poly_radial + 
                0.6 * cross_terms + 
                0.4 * exp_interaction)