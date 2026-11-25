import numpy as np

class ChaoticWeightedMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with polynomial and exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.3 * r + 0.1 * r**2) * np.exp(-0.2 * r**2)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_osc = np.sum(np.sin(8 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) + 
                         0.5 * np.sin(15 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled) + 
                         0.3 * np.sin(22 * np.pi * x_scaled) * np.cos(21 * np.pi * x_scaled))
        
        # Cross-dimensional coupling with interaction terms
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (x_scaled[i]**2 + x_scaled[i+1]**2) * np.sin(5 * np.pi * (x_scaled[i] - x_scaled[i+1]))
        
        # Chaotic component using a modified logistic map-like function
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * r + i * 0.5) * np.cos(9 * r + i * 0.4)
        
        # Multimodal peaks with varying heights and widths
        multimodal = np.sum(np.sin(6 * np.pi * x_scaled)**2 + 
                           0.3 * np.sin(12 * np.pi * x_scaled)**3 + 
                           0.1 * np.sin(18 * np.pi * x_scaled)**4)
        
        # Fractal-like structure using self-similar patterns
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(4 * np.pi * x_scaled[i]**1.5) * np.cos(3 * np.pi * x_scaled[i]**1.5)
        
        # Adaptive weighting based on distance from center
        adaptive_weight = 1.0 / (1.0 + 0.5 * r)
        
        # Combine all components with adaptive weights
        return (0.3 * radial + 0.25 * trig_osc + 0.2 * cross_coupling + 
                0.15 * chaotic + 0.08 * multimodal + 0.02 * fractal) * adaptive_weight