import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with varying exponents
        poly_chaos = np.sum((x**2 + x**3 - x**5 + x**7 - x**9)**2)
        
        # Trigonometric wave interference with multiple frequencies
        wave_interference = np.sum(np.sin(10 * x) * np.cos(15 * x) * 
                                  np.sin(20 * x) * np.cos(25 * x) * 
                                  np.sin(30 * x) * np.cos(35 * x))
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-4.5, 4.5, min(5, self.dim))
        rbf = 0.0
        for i in range(len(centers)):
            rbf += np.exp(-np.sum((x - centers[i])**2) / 2.0)
        
        # Cross-dimensional coupling with sine and cosine products
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(x[i]) * np.cos(x[i+1]) * np.sin(x[i+1]) * np.cos(x[i])
        
        # High-frequency oscillation with amplitude modulation
        high_freq = np.sum(np.sin(50 * x) * np.cos(45 * x) * 
                          np.sin(40 * x) * np.cos(35 * x) * 
                          np.sin(30 * x) * np.cos(25 * x) * 
                          np.sin(20 * x) * np.cos(15 * x))
        
        # Non-separable interaction terms with exponential decay
        interaction = np.sum(np.exp(-0.1 * (x[:-1] - x[1:])**2) * 
                            np.sin(20 * (x[:-1] + x[1:])) * 
                            np.cos(15 * (x[:-1] - x[1:])))
        
        # Global offset and scaling
        return 0.3 * poly_chaos + 0.2 * wave_interference + 0.1 * rbf + 0.25 * coupling + 0.15 * high_freq + 0.1 * interaction + 5.0