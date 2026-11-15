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
        radial_decay = np.exp(-self.alpha * r)
        
        # Sinusoidal waves in each dimension with varying frequencies
        wave_sum = 0
        for i in range(self.dim):
            wave_sum += np.sin(self.beta * x[i]) * np.cos(self.gamma * x[i])
        
        # Polynomial radial terms with different powers
        poly_radial = 0
        for i in range(self.dim):
            poly_radial += x[i]**4 + 0.5 * x[i]**3 + 0.1 * x[i]**2
        
        # Cross-term interactions with exponential scaling
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        
        # Additional multimodal component with multiple peaks
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.5 * np.sin(7 * x[i])
        
        # Combine all components
        return (0.3 * radial_decay + 
                1.2 * wave_sum + 
                0.8 * poly_radial + 
                0.5 * cross_terms + 
                0.9 * multimodal)