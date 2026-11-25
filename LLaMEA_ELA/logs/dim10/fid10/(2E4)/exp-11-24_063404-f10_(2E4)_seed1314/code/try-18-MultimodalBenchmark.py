import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with chaotic exponential modulation and multiple frequency bands
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) * (1.0 + 0.5 * np.sin(7 * r) * np.cos(3 * r)) + 
                  0.4 * np.exp(-0.3 * r**2) * np.sin(9 * r) * np.cos(5 * r) + 
                  0.1 * np.exp(-3 * r**2) * np.sin(11 * r) * np.cos(7 * r) +
                  0.05 * np.exp(-0.7 * r**2) * np.sin(13 * r))
        
        # Chaotic angular component with non-linear coupling and asymmetric interactions
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Add chaotic angular frequencies with non-uniform distribution and asymmetry
            for i in range(min(5, self.dim)):
                freq = (i + 1) * (1.0 + 0.3 * np.sin(i * 0.7))
                angular += (0.6 + 0.4 * np.sin(freq * angles)) * (0.8 + 0.2 * np.cos(freq * angles)) * \
                          np.exp(-0.5 * i * np.abs(angles))
        
        # Multi-scale oscillation with fractal-like frequency distribution
        oscillation = np.sum(np.sin(20 * x_scaled)**3 + np.cos(17 * x_scaled)**3 + 
                           0.3 * np.sin(19 * x_scaled) * np.cos(16 * x_scaled) +
                           0.1 * np.sin(22 * x_scaled) * np.cos(18 * x_scaled))
        
        # Asymmetric interaction terms with polynomial coupling and cross-terms
        interaction = 0.15 * np.sum(x_scaled**7) + 0.08 * np.sum(x_scaled[:-1]**3 * x_scaled[1:]) + \
                     0.05 * np.sum(np.abs(x_scaled[:-2]) * np.abs(x_scaled[1:-1]) * np.abs(x_scaled[2:]))
        
        # Add a small but significant noise component to increase ruggedness
        noise = 0.001 * np.sum(np.sin(50 * x_scaled) * np.cos(47 * x_scaled))
        
        # Combine all components with carefully tuned weights
        return radial + 0.5 * angular + 0.3 * oscillation + 0.15 * interaction + noise + 0.002 * np.sum(x_scaled**5)