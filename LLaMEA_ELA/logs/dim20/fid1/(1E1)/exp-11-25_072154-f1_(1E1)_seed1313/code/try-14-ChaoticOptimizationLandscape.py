import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component with high-degree terms
        poly_chaos = np.sum((x_scaled**4 - 2*x_scaled**2 + 1) * np.sin(2 * np.pi * x_scaled))
        
        # Radial basis functions with multiple centers
        r = np.sqrt(np.sum(x_scaled**2))
        rbfs = np.sum(np.exp(-5 * (x_scaled - 0.5)**2) + np.exp(-3 * (x_scaled + 0.3)**2))
        
        # Cross-dimensional coupling with sine interactions
        cross_coupling = np.sum(np.sin(3 * np.pi * x_scaled[:-1]) * np.cos(4 * np.pi * x_scaled[1:]))
        
        # Hyperbolic tangent chaotic component
        tanh_chaos = np.sum(np.tanh(5 * r) * np.sin(8 * r))
        
        # High-frequency oscillation in radial direction
        high_freq = np.sin(20 * r) * np.cos(15 * r)
        
        # Combine all components with different weights
        return 0.3 * poly_chaos + 0.25 * rbfs + 0.2 * cross_coupling + 0.15 * tanh_chaos + 0.1 * high_freq