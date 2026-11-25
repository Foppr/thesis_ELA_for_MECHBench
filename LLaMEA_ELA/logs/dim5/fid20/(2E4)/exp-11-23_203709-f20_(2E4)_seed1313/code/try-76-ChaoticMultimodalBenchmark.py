import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave components with dynamic frequencies and phases
        chaotic_component = 0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(0.5 * i + 1.0) * np.cos(0.3 * i)
            phase = 0.2 * np.sin(0.7 * i + 0.5)
            chaotic_component += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] / 3.0 + phase)
        
        # Gaussian peaks with adaptive widths and heights
        gaussian_component = 0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            width = 0.5 + 0.5 * np.sin(0.6 * i + 0.2)
            height = 1.0 + 0.5 * np.cos(0.4 * i + 0.3)
            gaussian_component += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Non-separable interaction terms with chaotic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(2.0 * dx) * np.cos(1.0 * dx)
                dist = np.sqrt(dx**2 + dy**2)
                coupling = 0.5 + 0.5 * np.sin(0.3 * (i + j))
                interaction += coupling / (1.0 + dist**2)
        
        # Adaptive conditioning with chaotic scaling factor
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) * np.sin(0.4 * self.dim + 0.1)
        
        # Combine all components with dynamic weights
        total = 3.0 * chaotic_component + 2.0 * gaussian_component + 0.5 * interaction + 30.0 * condition_factor
        
        return total