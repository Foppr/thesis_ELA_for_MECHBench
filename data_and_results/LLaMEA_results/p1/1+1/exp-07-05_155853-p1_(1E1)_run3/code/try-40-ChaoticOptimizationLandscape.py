import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional polynomial terms with non-integer exponents
        fractional_poly = 0
        for i in range(self.dim):
            fractional_poly += (0.2 * x[i]**2.7 - 0.15 * x[i]**3.3 + 
                               0.1 * x[i]**1.8 - 0.05 * x[i]**4.2)
        
        # Enhanced chaotic component with multi-scale sinusoids and dynamic modulation
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(7 * x[i]) + 
                       0.6 * np.sin(22 * x[i]) * np.cos(14 * x[i]) * np.sin(9 * x[i]) + 
                       0.2 * np.sin(30 * x[i]) * np.cos(20 * x[i]))
        
        # Dynamic cross-dimensional coupling with varying strength
        cross_interaction = 0
        for i in range(self.dim - 1):
            strength = 1.0 + 0.5 * np.sin(0.5 * (x[i] + x[i+1]))
            cross_interaction += strength * (x[i]**2.5 + x[i+1]**2.5 + 
                                           0.3 * x[i] * x[i+1] * np.cos(5 * (x[i] - x[i+1])))
        
        # Multi-scale sinusoidal modulation with varying frequencies
        modulation = 0
        for i in range(self.dim):
            modulation += (0.5 * np.sin(3 * x[i]) * np.cos(2 * x[i]) + 
                          0.3 * np.sin(8 * x[i]) * np.cos(6 * x[i]) + 
                          0.2 * np.sin(12 * x[i]) * np.cos(10 * x[i]))
        
        # Global scaling factor with time-varying component
        global_scale = 2.0 + 0.8 * np.sin(0.4 * np.sum(x**2)) * np.cos(0.3 * np.sum(x**3)) + \
                       0.3 * np.sin(0.1 * np.sum(x**4))
        
        # Add a complex noise term with multiple frequency components
        noise = 0.02 * np.sum(np.sin(40 * x) + 0.5 * np.sin(80 * x) + 0.3 * np.sin(120 * x))
        
        # Combine all components
        return global_scale * (fractional_poly + chaotic + cross_interaction + modulation) + noise