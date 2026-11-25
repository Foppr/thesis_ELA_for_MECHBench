import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with multiple exponential terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.3 * np.exp(-0.5 * r**2) * np.sin(3 * r)) * (1 + 0.4 * np.cos(7 * r))
        
        # Increased trigonometric complexity with higher frequency components
        trig = np.sum(np.cos(5 * np.pi * x_scaled) * np.sin(6 * np.pi * x_scaled) + 
                     0.5 * np.sin(4 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Enhanced exponential interaction terms with cross-dimension coupling
        exp_interaction = np.sum(np.exp(-0.3 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.7 * np.exp(-0.1 * (x_scaled[:-2] - x_scaled[2:])**2))
        
        # Additional chaotic component with polynomial radial dependence
        chaotic = np.sum(np.sin(8 * r**3) * np.cos(5 * r**3) + 0.3 * np.sin(12 * r**2))
        
        # Add a multi-modal component for increased complexity
        multimodal = 0.5 * np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled)) + \
                    0.2 * np.sum(np.sin(10 * np.pi * x_scaled)**2)
        
        # Combine all components with optimized weights
        return 0.35 * radial + 0.25 * trig + 0.2 * exp_interaction + 0.15 * chaotic + 0.05 * multimodal