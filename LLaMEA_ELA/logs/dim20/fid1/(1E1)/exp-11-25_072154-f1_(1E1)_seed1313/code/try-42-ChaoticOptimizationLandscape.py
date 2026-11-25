import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Fractal-like radial component with self-similar patterns at multiple scales
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.3 * np.exp(-0.5 * r**2) * np.sin(3 * r) + 
                 0.1 * np.exp(-0.1 * r**3) * np.cos(7 * r)) * (1 + 0.4 * np.cos(7 * r))
        
        # Enhanced trigonometric complexity with dynamic frequencies based on input magnitude
        dynamic_freq = 1 + 0.5 * np.abs(x_scaled)
        trig = np.sum(np.cos(dynamic_freq * np.pi * x_scaled) * np.sin(dynamic_freq * np.pi * x_scaled) + 
                     0.5 * np.sin(dynamic_freq * np.pi * x_scaled) * np.cos(dynamic_freq * np.pi * x_scaled))
        
        # Dynamic exponential interaction terms that change based on distance
        dist = np.abs(x_scaled[:-1] - x_scaled[1:])
        exp_interaction = np.sum(np.exp(-0.3 * dist**2) + 
                               0.7 * np.exp(-0.1 * dist**3) + 
                               0.2 * np.exp(-0.05 * dist**4))
        
        # Multi-scale chaotic component with varying amplitude and frequency
        chaotic = np.sum(np.sin(8 * r**3) * np.cos(5 * r**3) + 
                        0.3 * np.sin(12 * r**2) * np.cos(9 * r**2) + 
                        0.1 * np.sin(15 * r**4))
        
        # Highly multimodal component with nested valleys and ridges
        multimodal = 0.5 * np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled)) + \
                    0.2 * np.sum(np.sin(10 * np.pi * x_scaled)**2) + \
                    0.1 * np.sum(np.sin(20 * np.pi * x_scaled)**3)
        
        # Gradient complexity component with varying steepness
        grad_comp = 0.1 * np.sum(np.abs(x_scaled)**3 + 0.5 * np.abs(x_scaled)**4)
        
        # Adaptive coupling term that changes based on dimensionality
        adaptive_coupling = 0.05 * np.sum((x_scaled[:-1] * x_scaled[1:])**2) * (1 + 0.1 * self.dim)
        
        # Combine all components with optimized weights
        return 0.3 * radial + 0.2 * trig + 0.15 * exp_interaction + 0.15 * chaotic + \
               0.1 * multimodal + 0.05 * grad_comp + 0.05 * adaptive_coupling