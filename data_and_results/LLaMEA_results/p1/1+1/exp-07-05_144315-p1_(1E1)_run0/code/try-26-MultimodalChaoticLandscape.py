import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with quadratic base
        r = np.sqrt(np.sum(x**2))
        radial = r**2
        
        # Periodic sinusoidal modulations in each dimension
        periodic = np.sum(np.sin(3 * x) * np.cos(7 * x))
        
        # Cross-dimensional interaction terms with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(2 * x[i] * x[j])
        
        # Multimodal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.5 * np.sin(10 * x[i])
        
        # Add a global scaling factor based on distance from origin
        scaling = 1.0 + 0.2 * np.sin(0.5 * r)
        
        # Combine all components
        return 0.5 * radial + 0.3 * periodic + 0.4 * cross_interaction + 0.6 * multimodal + scaling