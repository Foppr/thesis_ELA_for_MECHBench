import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Higher-order polynomial basin term with fractal-like scaling
        poly_basin = 0.005 * np.sum(x**8) + 0.02 * np.sum(x**5) + 0.1 * np.sum(x**3) + 0.05 * np.sum(x**2)
        
        # Enhanced chaotic sinusoidal terms with fractal frequency patterns
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(20 * x[i]) * np.cos(17 * x[i]) * np.sin(13 * x[i]) * np.cos(11 * x[i]) + 
                      np.cos(19 * x[i]) * np.sin(16 * x[i]) * np.cos(14 * x[i]) * np.sin(12 * x[i]) +
                      np.sin(18 * x[i]**2) * np.cos(15 * x[i]**2) * np.sin(10 * x[i]**2))
            
        # Complex cross-term interactions with nested valleys and ridges
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * np.sin((x[i] + x[j])**2) +
                              np.cos(x[i] * x[j]) * np.sin(x[i]**3 + x[j]**3) * np.cos((x[i] - x[j])**3) +
                              np.sin(x[i]**2 * x[j]) * np.cos(x[i] * x[j]**2) * np.sin((x[i] * x[j])**1.5))
                
        # Fractal harmonic components with self-similar patterns at multiple scales
        harmonics = 0
        for i in range(self.dim):
            harmonics += (np.sin(8 * x[i]**5) * np.cos(6 * x[i]**4) * np.sin(4 * x[i]**3) + 
                        np.cos(7 * x[i]**6) * np.sin(5 * x[i]**5) * np.cos(3 * x[i]**4) +
                        np.sin(9 * x[i]**7) * np.cos(8 * x[i]**6) * np.sin(7 * x[i]**5))
        
        # Add nested chaotic scaling factors to create multi-scale complexity
        scale_factor = 1.0 + 0.3 * np.sin(np.sum(x**2) / self.dim)
        
        return scale_factor * (0.3 * poly_basin + 0.4 * chaotic + 0.2 * cross_terms + 0.1 * harmonics)