import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-scale chaotic component with fractional exponents and varying frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(15 * x[i]**1.3) * np.cos(10 * x[i]**0.7) + 
                       0.6 * np.sin(22 * x[i]**1.5) * np.cos(14 * x[i]**0.8) + 
                       0.4 * np.sin(30 * x[i]**1.2))
        
        # Fractional polynomial potential with non-integer powers and mixed signs
        polynomial = 0
        for i in range(self.dim):
            polynomial += (0.1 * x[i]**4.5 + 0.15 * x[i]**3.7 - 0.2 * x[i]**2.8 + 
                          0.08 * x[i]**1.9 - 0.12 * x[i]**0.6)
        
        # Dynamic cross-dimensional interaction with periodic modulation
        cross_interaction = 0
        for i in range(self.dim - 1):
            distance = (x[i] - x[i+1])**2
            modulation = np.sin(0.5 * np.sum(x**2)) * np.cos(0.3 * np.sum(x**3))
            cross_interaction += np.exp(-0.03 * distance) * (x[i]**2.5 + x[i+1]**2.5 + 
                                                           0.7 * x[i] * x[i+1]) * (1 + 0.2 * modulation)
        
        # Multi-modal scaling factor with multiple sinusoidal components
        global_scale = 2.0 + 0.8 * np.sin(0.4 * np.sum(x**2)) * np.cos(0.25 * np.sum(x**3)) + \
                       0.5 * np.sin(0.6 * np.sum(x**4)) * np.cos(0.3 * np.sum(x**5))
        
        # Add a complex noise term with multiple frequency components
        noise = 0.02 * np.sum(np.sin(60 * x) + 0.5 * np.sin(30 * x) + 0.3 * np.sin(15 * x))
        
        # Combine all components
        return global_scale * (chaotic + polynomial + cross_interaction) + noise