import numpy as np

class GradientRichBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable polynomial component with varying exponents
        poly_term = np.sum(x_norm**4.5 + 0.5 * x_norm**3.2 + 0.2 * x_norm**2.1)
        
        # Periodic oscillation with adaptive frequency and amplitude
        freqs = np.linspace(1.0, 8.0, self.dim)
        oscillation = np.sum(np.sin(freqs * np.pi * x_norm) * np.cos(freqs * 0.5 * np.pi * x_norm))
        
        # Adaptive conditioning based on dimensionality and position
        condition = np.sum((x_norm**2 + 0.1) * np.exp(-0.5 * x_norm**2))
        
        # Cross-dimensional interaction with exponential coupling
        cross_term = np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           np.sin(2.0 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Chaotic modulation with sine-cosine coupling and dynamic scaling
        chaotic = np.sum(np.sin(3.0 * np.pi * x_norm) * np.cos(2.0 * np.pi * x_norm) * 
                        np.exp(-0.3 * x_norm**2) * np.tan(0.5 * x_norm))
        
        # Adaptive noise component
        noise = 0.05 * np.random.rand() * (1.0 + 0.2 * np.abs(np.mean(x_norm)))
        
        # Combine all terms with dynamic weighting
        result = 0.7 * poly_term + 0.3 * oscillation + 0.5 * condition + 0.4 * cross_term + chaotic + noise
        
        return result