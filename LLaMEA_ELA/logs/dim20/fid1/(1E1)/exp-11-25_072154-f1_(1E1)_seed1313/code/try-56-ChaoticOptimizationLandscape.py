import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with modified exponential weights and polynomial terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (0.8 * np.exp(-r**2) + 0.4 * np.exp(-0.3 * r**2) * np.sin(5 * r) + 
                 0.3 * np.exp(-0.1 * r**3) * np.cos(4 * r)) * (1 + 0.2 * np.sin(8 * r))
        
        # Multi-frequency trigonometric complexity with modified coupling
        trig = np.sum(0.9 * np.cos(7 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled) + 
                     0.5 * np.sin(5 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                     0.4 * np.cos(9 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with modified coupling
        exp_interaction = np.sum(np.exp(-0.6 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.7 * np.exp(-0.3 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.5 * np.exp(-0.08 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Nested chaotic component with modified fractional power radial dependence
        chaotic = np.sum(0.9 * np.sin(10 * r**2.5) * np.cos(7 * r**2.5) + 
                        0.3 * np.sin(15 * r**1.8) * np.cos(12 * r**1.8) + 
                        0.1 * np.sin(20 * r**1.2))
        
        # Highly multi-modal component with modified frequency modulation
        multimodal = 0.5 * np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled)) + \
                    0.4 * np.sum(np.sin(12 * np.pi * x_scaled)**2 + 
                                0.6 * np.sin(8 * np.pi * x_scaled)**3) + \
                    0.2 * np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled))
        
        # Modified cross-dimensional coupling term
        cross_coupling = 0.15 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(2 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Combine all components with updated weights
        return 0.25 * radial + 0.3 * trig + 0.25 * exp_interaction + 0.15 * chaotic + 0.06 * multimodal + 0.04 * cross_coupling