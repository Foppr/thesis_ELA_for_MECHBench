import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Composite fractal sinusoidal terms with varying frequencies and amplitudes
        f1 = np.sum(np.sin(2.5 * np.pi * x_norm) * np.cos(3.5 * np.pi * x_norm**2) * 
                   np.exp(-0.6 * x_norm**2))
        
        # Multi-scale wave interactions with fractal dimensionality dependence
        f2 = np.sum(np.sin(4.2 * np.pi * x_norm) * np.cos(2.3 * np.pi * x_norm**1.5) * 
                   np.exp(-0.35 * np.abs(x_norm)**1.8))
        
        # Adaptive conditioning based on dimensionality with fractal scaling
        adaptive_factor = 1.0 + 0.6 * np.log(self.dim + 1) + 0.25 * np.sin(self.dim * 0.6)
        
        # Enhanced cross-dimensional coupling with recursive interaction terms
        f3 = 0.0
        for i in range(self.dim - 1):
            f3 += (np.sin(x_norm[i]) * np.cos(x_norm[i+1]) + 
                   np.cos(x_norm[i]) * np.sin(x_norm[i+1])) * \
                  np.exp(-0.25 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Higher-order polynomial fractal components
        f4 = np.sum((x_norm**3.5 + x_norm**5.5) * np.exp(-0.45 * np.abs(x_norm)**2.5))
        
        # Composite chaotic modulation with dynamic frequency adjustment
        freq_mod = 1.0 + 0.35 * np.sin(np.pi * self.dim / 4.5)
        f5 = np.sum(np.sin(freq_mod * np.pi * x_norm**1.4) * 
                   np.cos(freq_mod * np.pi * x_norm**1.8) * 
                   np.exp(-0.65 * x_norm**2))
        
        # Combine all components with adaptive weighting
        result = (f1 + 0.75 * f2 + 0.55 * f3 + 0.85 * f4 + 0.65 * f5) * adaptive_factor
        
        # Add fractal noise for increased complexity and non-deterministic behavior
        noise = 0.0015 * np.random.random() * (1.0 + 0.12 * np.sin(self.dim * 0.35))
        
        return result + noise