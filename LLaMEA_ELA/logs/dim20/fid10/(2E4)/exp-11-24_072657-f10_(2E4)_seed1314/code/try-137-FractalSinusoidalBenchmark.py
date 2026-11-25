import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal sinusoidal terms with higher harmonic complexity
        f1 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm**2.5) * 
                   np.exp(-0.4 * x_norm**2))
        
        # Multi-scale wave interactions with enhanced fractal dimensionality dependence
        f2 = np.sum(np.sin(6 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm**1.7) * 
                   np.exp(-0.2 * np.abs(x_norm)**2.2))
        
        # Enhanced adaptive conditioning based on dimensionality with fractal scaling
        adaptive_factor = 1.5 + 0.8 * np.log(self.dim + 1) + 0.3 * np.sin(self.dim * 0.7)
        
        # Stronger cross-dimensional coupling with recursive interaction terms
        f3 = 0.0
        for i in range(self.dim - 1):
            f3 += (np.sin(x_norm[i]) * np.cos(x_norm[i+1]) + 
                   np.cos(x_norm[i]) * np.sin(x_norm[i+1])) * \
                  np.exp(-0.3 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Higher-order polynomial fractal components with enhanced nonlinearity
        f4 = np.sum((x_norm**4 + x_norm**6) * np.exp(-0.5 * np.abs(x_norm)**3))
        
        # Enhanced chaotic modulation with dynamic frequency adjustment and phase coupling
        freq_mod = 1.2 + 0.5 * np.sin(np.pi * self.dim / 3.0)
        phase_mod = 0.8 + 0.2 * np.cos(self.dim * 0.4)
        f5 = np.sum(np.sin(freq_mod * np.pi * x_norm**1.5) * 
                   np.cos(freq_mod * np.pi * x_norm**2.0) * 
                   np.exp(-0.7 * x_norm**2) * phase_mod)
        
        # Additional chaotic interaction terms with exponential coupling
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Composite chaotic modulation with dynamic frequency adjustment
        freq_mod2 = 1.0 + 0.4 * np.sin(np.pi * self.dim / 5.0)
        f7 = np.sum(np.sin(freq_mod2 * np.pi * x_norm**1.8) * 
                   np.cos(freq_mod2 * np.pi * x_norm**1.9) * 
                   np.exp(-0.5 * x_norm**2))
        
        # Combine all components with adaptive weighting
        result = (f1 + 0.8 * f2 + 0.6 * f3 + 0.9 * f4 + 0.7 * f5 + 0.5 * f6 + 0.6 * f7) * adaptive_factor
        
        # Add enhanced fractal noise for increased complexity and non-deterministic behavior
        noise = 0.002 * np.random.random() * (1.0 + 0.2 * np.sin(self.dim * 0.5))
        
        return result + noise