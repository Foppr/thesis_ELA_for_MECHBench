import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map based chaotic component
        logistic = np.sum(4.0 * x_scaled * (1.0 - x_scaled))
        
        # Trigonometric coupling with varying frequencies and phases
        trig_coupling = np.sum(np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled) + 
                             0.7 * np.sin(12.0 * x_scaled**2) * np.cos(9.0 * x_scaled**2) + 
                             0.4 * np.sin(15.0 * x_scaled**3) * np.cos(13.0 * x_scaled**3))
        
        # Fractal-like self-similarity with power-law scaling
        fractal = np.sum(np.abs(x_scaled)**1.7 + 0.5 * np.abs(x_scaled)**2.3 + 
                        0.2 * np.abs(x_scaled)**3.1)
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = np.sum(np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) * 
                                np.cos(4.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                                0.6 * np.sin(3.0 * (x_scaled[:-2] * x_scaled[2:])) * 
                                np.cos(2.0 * (x_scaled[:-2] / (x_scaled[2:] + 1e-8))))
        
        # Asymmetric non-smooth regions with piecewise polynomial
        smoothness = np.sum(np.abs(x_scaled)**1.3 + 0.3 * np.abs(x_scaled)**2.7 + 
                          0.1 * np.abs(x_scaled)**4.1)
        
        # Combined chaotic landscape with weighted components
        return 0.4 * logistic + 0.3 * trig_coupling + 0.15 * fractal + 0.1 * cross_interaction + 0.05 * smoothness + 2.1