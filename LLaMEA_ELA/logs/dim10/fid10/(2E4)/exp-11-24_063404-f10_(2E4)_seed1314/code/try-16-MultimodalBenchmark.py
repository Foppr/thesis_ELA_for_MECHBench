import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with modified exponential terms and trigonometric modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-0.5 * r**2) * (1.0 + 0.4 * np.sin(6 * r)) + 
                  0.3 * np.exp(-r**2) * np.cos(4 * r) + 
                  0.1 * np.exp(-1.5 * r**2) * np.sin(8 * r))
        
        # Angular component with altered frequencies and cross-terms
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Add multiple angular frequencies with varying amplitudes
            for i in range(min(3, self.dim)):
                angular += (0.6 + 0.2 * np.sin((i+2) * angles)) * (0.8 + 0.2 * np.cos((i+3) * angles))
        
        # High-frequency oscillation with non-uniform frequency distribution
        oscillation = np.sum(np.sin(17 * x_scaled)**2 + np.cos(13 * x_scaled)**2 + 
                           0.6 * np.sin(15 * x_scaled) * np.cos(10 * x_scaled))
        
        # Additional complexity through polynomial and interaction terms
        interaction = 0.15 * np.sum(x_scaled**6) + 0.08 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Combine all components with carefully tuned weights
        return radial + 0.3 * angular + 0.25 * oscillation + 0.15 * interaction + 0.002 * np.sum(x_scaled**4)