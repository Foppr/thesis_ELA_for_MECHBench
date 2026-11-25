import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with modified exponential and polynomial terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (0.8 * np.exp(-r**2) + 0.4 * np.exp(-0.5 * r**2) * np.sin(6 * r) + 
                 0.3 * np.exp(-0.2 * r**3) * np.cos(5 * r)) * (1 + 0.4 * np.sin(9 * r))
        
        # Multi-frequency trigonometric complexity with altered coupling
        trig = np.sum(0.8 * np.cos(8 * np.pi * x_scaled) * np.sin(9 * np.pi * x_scaled) + 
                     0.7 * np.sin(6 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) + 
                     0.4 * np.cos(10 * np.pi * x_scaled) * np.sin(4 * np.pi * x_scaled))
        
        # Multi-scale exponential interaction terms with modified coupling
        exp_interaction = np.sum(np.exp(-0.6 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                               0.9 * np.exp(-0.3 * (x_scaled[:-2] - x_scaled[2:])**2) + 
                               0.5 * np.exp(-0.1 * (x_scaled[:-3] - x_scaled[3:])**2))
        
        # Nested chaotic component with modified fractional power radial dependence
        chaotic = np.sum(0.8 * np.sin(12 * r**2.3) * np.cos(9 * r**2.3) + 
                        0.5 * np.sin(18 * r**1.7) * np.cos(15 * r**1.7) + 
                        0.3 * np.sin(25 * r**1.4))
        
        # Highly multi-modal component with adjusted frequency modulation
        multimodal = 0.7 * np.sum(np.sin(4 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled)) + \
                    0.4 * np.sum(np.sin(14 * np.pi * x_scaled)**2 + 
                                0.6 * np.sin(10 * np.pi * x_scaled)**3) + \
                    0.2 * np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(25 * np.pi * x_scaled))
        
        # Add a modified cross-dimensional coupling term for increased complexity
        cross_coupling = 0.3 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(3 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Combine all components with updated weights
        return 0.25 * radial + 0.3 * trig + 0.25 * exp_interaction + 0.15 * chaotic + 0.06 * multimodal + 0.05 * cross_coupling