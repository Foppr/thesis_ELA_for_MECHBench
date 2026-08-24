import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos terms with varying degrees and coefficients
        poly_chaos = np.sum(0.5 * x**12 + 0.3 * x**10 + 0.7 * x**8 + 0.4 * x**6 + 0.6 * x**4 + 0.2 * x**2)
        
        # Radial basis function components with dynamic centers and widths
        centers = np.linspace(-5, 5, self.dim)
        widths = np.linspace(0.5, 2.0, self.dim)
        rbf = np.sum(np.exp(-np.sum(((x - centers) / widths)**2, axis=0)))
        
        # Dynamic coupling with time-varying sinusoidal modulations
        dynamic_coupling = np.sum(np.sin(10 * x) * np.cos(8 * x) * np.sin(6 * x) * np.cos(4 * x) * 
                                 np.sin(2 * x) * np.cos(1 * x) * np.sin(0.5 * x) * np.cos(0.25 * x))
        
        # Multi-scale oscillatory interactions with varying amplitudes
        scale_osc = np.sum(np.sin(50 * x) * np.cos(45 * x) * np.sin(40 * x) * np.cos(35 * x) * 
                          np.sin(30 * x) * np.cos(25 * x) * np.sin(20 * x) * np.cos(15 * x) * 
                          np.sin(10 * x) * np.cos(5 * x))
        
        # Memory-dependent polynomial interactions with exponential decay
        memory_poly = np.sum(np.exp(-0.1 * x**2) * (x**9 - x**7 + x**5 - x**3 + x))
        
        # Cross-dimensional chaotic interactions with varying phase shifts
        chaotic_interaction = np.sum(np.sin(25 * x) * np.cos(23 * x) * np.sin(21 * x) * np.cos(19 * x) * 
                                   np.sin(17 * x) * np.cos(15 * x) * np.sin(13 * x) * np.cos(11 * x) * 
                                   np.sin(9 * x) * np.cos(7 * x))
        
        # Combine all terms with optimized weights
        return 0.3 * poly_chaos + 0.2 * rbf + 0.25 * dynamic_coupling + 0.15 * scale_osc + \
               0.1 * memory_poly + 0.2 * chaotic_interaction + 3.0