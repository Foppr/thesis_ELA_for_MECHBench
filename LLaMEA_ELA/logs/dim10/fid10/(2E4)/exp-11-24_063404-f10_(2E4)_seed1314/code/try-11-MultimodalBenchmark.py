import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with multiple exponential terms and trigonometric modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) * (1.0 + 0.3 * np.sin(5 * r)) + 
                  0.5 * np.exp(-0.5 * r**2) * np.cos(3 * r) + 
                  0.2 * np.exp(-2 * r**2) * np.sin(7 * r))
        
        # Angular component with higher frequency interactions and cross-terms
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Add multiple angular frequencies with varying amplitudes
            for i in range(min(4, self.dim)):
                angular += (0.5 + 0.3 * np.sin((i+1) * angles)) * (0.7 + 0.3 * np.cos((i+2) * angles))
        
        # High-frequency oscillation with non-uniform frequency distribution
        oscillation = np.sum(np.sin(15 * x_scaled)**2 + np.cos(11 * x_scaled)**2 + 
                           0.5 * np.sin(13 * x_scaled) * np.cos(9 * x_scaled))
        
        # Additional complexity through polynomial and interaction terms
        interaction = 0.1 * np.sum(x_scaled**6) + 0.05 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Combine all components with carefully tuned weights
        return radial + 0.4 * angular + 0.2 * oscillation + 0.1 * interaction + 0.001 * np.sum(x_scaled**4)