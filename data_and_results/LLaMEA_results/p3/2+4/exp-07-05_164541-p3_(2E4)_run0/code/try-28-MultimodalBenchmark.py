import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay with complex argument
        chaotic_exp = np.sum(np.exp(-0.3 * (x**2 + 0.3 * np.sin(7 * x)**2)) * np.cos(4 * np.pi * x))
        
        # Multi-frequency trigonometric interactions with varying amplitudes
        multi_freq = np.sum(0.5 * np.sin(12 * np.pi * x) * np.cos(9 * np.pi * x) + 
                           0.3 * np.sin(8 * np.pi * x) * np.cos(11 * np.pi * x) + 
                           0.2 * np.sin(6 * np.pi * x) * np.cos(13 * np.pi * x))
        
        # High-degree polynomial coupling with cross-dimensional terms
        poly_coupling = np.sum(0.4 * x**5.2 - 1.8 * x**4.1 + 3.5 * x**3.7 - 2.9 * x**2.3 + 1.1 * x**1.6)
        
        # Cross-dimensional nonlinear correlations with sine and cosine products
        cross_corr = np.sum(np.sin(np.pi * (x[:-1]**1.5 + x[1:]**1.3)) * np.cos(np.pi * (x[:-1]**1.7 - x[1:]**1.4)) * 
                           (x[:-1]**2.1 + x[1:]**2.2))
        
        # Fractional polynomial interactions with non-integer powers and mixed signs
        frac_poly = np.sum(0.25 * x**3.9 - 1.5 * x**2.7 + 2.8 * x**1.8 - 1.3 * x**0.9)
        
        # Enhanced chaotic oscillations with variable frequency
        chaotic_osc = np.sum(np.sin(np.pi * x**1.9) * np.cos(np.pi * x**1.4) * np.exp(-0.4 * np.abs(x)) * 
                            np.sin(3 * np.pi * x**0.8))
        
        # Combine all terms with optimized weights
        return 0.25 * chaotic_exp + 0.2 * multi_freq + 0.15 * poly_coupling + 0.12 * cross_corr + 0.08 * frac_poly + 0.05 * chaotic_osc + 1.5