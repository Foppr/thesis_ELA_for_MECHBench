import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        result = 0.1 * np.sum(x**2)
        
        # Add radial basis functions with varying centers and widths
        centers = np.linspace(-4.0, 4.0, min(6, self.dim))
        widths = np.linspace(0.5, 2.0, min(6, self.dim))
        
        for i in range(min(6, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = widths[i] if i < len(widths) else 1.0
            result += 2.0 * np.exp(-np.sum((x - center)**2) / (2 * width**2))
        
        # Add sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.5 + 0.5 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i])
        
        # Add multi-modal noise with chaotic frequency modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(10 * x[i] + np.sin(7 * x[i]))
        
        # Add adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return result * cond_factor + noise