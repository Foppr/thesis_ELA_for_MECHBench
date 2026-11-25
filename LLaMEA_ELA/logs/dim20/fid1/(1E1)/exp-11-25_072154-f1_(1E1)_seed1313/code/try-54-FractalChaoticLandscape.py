import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Base fractal component with recursive-like structure
        fractal = np.sum(np.sin(2 ** (np.abs(x_scaled) * 10)) * np.cos(3 ** (np.abs(x_scaled) * 5)))
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.sum(4 * x_scaled * (1 - np.abs(x_scaled)) + 
                        0.5 * np.sin(10 * x_scaled) * np.cos(8 * x_scaled))
        
        # Dynamic curvature that changes based on position
        curvature = np.sum((x_scaled**2) * (1 + 0.3 * np.sin(15 * x_scaled)) + 
                          0.2 * (x_scaled**4) * np.cos(7 * x_scaled))
        
        # Multi-scale oscillation with varying amplitudes
        oscillation = np.sum(np.sin(20 * x_scaled) * np.exp(-0.5 * x_scaled**2) + 
                           0.7 * np.cos(12 * x_scaled) * np.exp(-0.3 * x_scaled**2) + 
                           0.3 * np.sin(30 * x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Position-adaptive difficulty modifier
        adaptive = np.sum(0.5 * np.sin(5 * x_scaled) * (1 + 0.2 * np.cos(20 * x_scaled)) + 
                         0.3 * np.cos(8 * x_scaled) * (1 + 0.4 * np.sin(15 * x_scaled)))
        
        # Combine all components with dynamic weights
        return 0.25 * fractal + 0.2 * chaotic + 0.25 * curvature + 0.2 * oscillation + 0.1 * adaptive