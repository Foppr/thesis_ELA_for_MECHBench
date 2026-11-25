import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        sphere = np.sum(x**2)
        
        # Trigonometric chaos component with exponential decay
        trig_chaos = 0
        for i in range(self.dim):
            trig_chaos += np.exp(-0.1 * np.abs(x[i])) * np.sin(5 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Spherical harmonics component with varying angular frequencies
        harmonics = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    harmonics += 0.5 * np.sin(np.pi * (x[i] + x[j])) * np.cos(np.pi * (x[i] - x[j]))
        
        # Exponential interaction terms with dynamic scaling
        exp_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += 0.2 * np.exp(-0.5 * ((x[i] - x[j]) / (0.5 + np.abs(x[i]) + np.abs(x[j])))**2)
        
        # Adaptive noise component
        noise = 0.05 * np.sum(np.sin(10 * np.pi * x) ** 2)
        
        # Global shift and scaling factor
        shift = 0.5 * np.sum(np.abs(x))
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components
        return scale_factor * (sphere + 0.3 * trig_chaos + 0.2 * harmonics + 0.15 * exp_interaction) + shift + noise