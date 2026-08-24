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
        
        # Sinusoidal wave component with multiple frequencies
        sin_wave = 0
        for i in range(self.dim):
            sin_wave += np.sin(self.beta * x[i]) * np.cos(self.gamma * x[i])
        
        # Polynomial radial term with varying exponents
        poly_radial = 0
        for i in range(self.dim):
            poly_radial += (x[i]**2 + x[i]**4) * np.exp(-0.1 * x[i]**2)
        
        # Cross-term interactions with exponential coupling
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        
        # Additional multimodal component with Gaussian peaks
        multimodal = 0
        peak_centers = np.linspace(-3, 3, 5)
        for center in peak_centers:
            multimodal += np.exp(-0.5 * np.sum((x - center)**2)) * np.sin(2 * np.pi * (r - center))
        
        # Combine all components
        return (0.3 * radial_decay + 
                1.2 * sin_wave + 
                0.8 * poly_radial + 
                0.5 * cross_terms + 
                0.4 * multimodal)