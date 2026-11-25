import numpy as np

class MultiModalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_normalized**2))
        radial = np.sin(5 * np.pi * r) * np.exp(-r**2)
        
        # Trigonometric interactions between dimensions
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arccos(np.clip(x_normalized[i] * x_normalized[j], -1, 1))
                trig_interaction += np.sin(3 * angle) * np.cos(2 * angle)
        
        # Exponentially decaying correlation between dimensions
        correlation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.5 * (i - j)**2)
                correlation += decay * (x_normalized[i] - x_normalized[j])**2
        
        # Multi-modal component with multiple local minima
        modal = 0.0
        for i in range(self.dim):
            modal += (x_normalized[i]**4 - 2 * x_normalized[i]**2 + 1) * np.sin(4 * np.pi * x_normalized[i])
        
        # Combined fitness function
        return 0.3 * radial + 0.4 * trig_interaction + 0.2 * correlation + 0.1 * modal