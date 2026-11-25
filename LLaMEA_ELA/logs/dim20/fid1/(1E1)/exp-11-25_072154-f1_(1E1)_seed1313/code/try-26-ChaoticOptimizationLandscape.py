import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with multiple frequency oscillations
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2) * (1 + 0.3 * np.sin(3 * r) + 0.2 * np.cos(7 * r))
        
        # Modified trigonometric oscillations with varying frequencies
        trig = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Improved exponential interaction terms with cross-correlation
        exp_interaction = 0.0
        for i in range(self.dim - 1):
            exp_interaction += np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[i+1]**2)) * np.cos(2 * np.pi * (x_scaled[i] - x_scaled[i+1]))
        
        # Enhanced chaotic component with polynomial scaling
        chaotic = np.sum(np.sin(8 * r**3) * np.cos(5 * r**3) * np.exp(-0.5 * r))
        
        # Add a global shaping term to improve conditioning
        global_shape = 0.1 * np.sum(x_scaled**4)
        
        # Combine all components with optimized weights
        return 0.35 * radial + 0.25 * trig + 0.2 * exp_interaction + 0.15 * chaotic + 0.05 * global_shape