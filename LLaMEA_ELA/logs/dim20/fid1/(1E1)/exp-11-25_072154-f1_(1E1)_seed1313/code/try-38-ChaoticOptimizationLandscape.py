import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with multiple exponential decays
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.3 * np.exp(-0.5 * r**2)) * (1 + 0.7 * np.sin(7 * r) + 0.3 * np.cos(11 * r))
        
        # High-frequency trigonometric oscillations
        trig = np.sum(np.cos(5 * np.pi * x_scaled) * np.sin(6 * np.pi * x_scaled) + 
                      0.5 * np.sin(8 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled))
        
        # Modified exponential interaction terms with cross-terms
        exp_interaction = np.sum(np.exp(-0.3 * (x_scaled[:-1] - x_scaled[1:])**2)) + \
                         0.5 * np.sum(np.exp(-0.2 * (x_scaled[:-2] - x_scaled[2:])**2))
        
        # Enhanced chaotic component with multiple frequency components
        chaotic = np.sum(np.sin(15 * r**2) * np.cos(13 * r**2) + 
                         0.4 * np.sin(20 * r**2) * np.cos(17 * r**2))
        
        # Add a small Gaussian noise component to increase ruggedness
        noise = 0.05 * np.random.normal(0, 1)
        
        # Combine all components with optimized weights
        return 0.35 * radial + 0.3 * trig + 0.25 * exp_interaction + 0.1 * chaotic + noise