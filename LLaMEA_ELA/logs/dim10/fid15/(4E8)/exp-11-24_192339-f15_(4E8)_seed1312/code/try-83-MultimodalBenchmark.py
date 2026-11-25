import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with exponential decay modulations
        multimodal = 0
        for i in range(self.dim):
            # Exponential decay with sinusoidal modulation
            decay = np.exp(-0.1 * (x[i]**2))
            sine_mod = np.sin(2.0 * np.pi * x[i] * (i + 1) / self.dim)
            multimodal += decay * (sine_mod**4 + 0.5 * sine_mod**2)
        
        # Quaternion-inspired cross-dimensional interactions
        quaternion = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-terms for complexity
                if j < self.dim:
                    # Quaternion-like interaction terms
                    term1 = x[i]**2 * x[j]**3
                    term2 = x[i]**3 * x[j]**2
                    quaternion += 0.05 * (term1 + term2) / (1.0 + abs(x[i]) + abs(x[j]))
        
        # Time-varying harmonic components
        time_harmonic = 0
        for i in range(self.dim):
            # Add dynamic scaling based on position
            dynamic_scale = 1.0 + 0.3 * np.sin(0.5 * np.pi * x[i])
            time_harmonic += dynamic_scale * np.cos(3.0 * np.pi * x[i]) * np.sin(2.0 * np.pi * x[i])
        
        # Global shift and scaling
        shift = 0.1 * np.sum(np.abs(x))
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all components with dynamic weighting
        return sphere + scale_factor * (0.3 * multimodal + 0.1 * quaternion) + shift + 0.2 * time_harmonic