import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with nested exponential and polynomial terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.exp(-r**2) + 0.5 * np.exp(-0.3 * r**2) * np.sin(5 * r) + 
                 0.2 * np.exp(-0.1 * r**3) * np.cos(4 * r)) * (1 + 0.3 * np.sin(8 * r))
        
        # Multi-frequency trigonometric complexity with cross-dimensional coupling
        trig = np.sum(np.cos(7 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled) + 
                     0.6 * np.sin(5 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                     0.3 * np.cos(9 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with long-range coupling
        exp_interaction = np.sum(np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.8 * np.exp(-0.2 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.4 * np.exp(-0.05 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Nested chaotic component with fractional power radial dependence
        chaotic = np.sum(np.sin(10 * r**2.5) * np.cos(7 * r**2.5) + 
                        0.4 * np.sin(15 * r**1.8) * np.cos(12 * r**1.8) + 
                        0.2 * np.sin(20 * r**1.2))
        
        # Highly multi-modal component with adaptive frequency modulation
        multimodal = 0.6 * np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled)) + \
                    0.3 * np.sum(np.sin(12 * np.pi * x_scaled)**2 + 
                                0.5 * np.sin(8 * np.pi * x_scaled)**3) + \
                    0.1 * np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled))
        
        # Add a cross-dimensional coupling term for increased complexity
        cross_coupling = 0.2 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(2 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Combine all components with optimized weights
        return 0.3 * radial + 0.25 * trig + 0.2 * exp_interaction + 0.18 * chaotic + 0.07 * multimodal + 0.05 * cross_coupling