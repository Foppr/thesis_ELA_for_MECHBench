import numpy as np

class MultimodalConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for consistent scaling
        x_normalized = x / 5.0
        
        # Radial component with varying conditioning
        radius = np.sqrt(np.sum(x_normalized**2))
        radial_conditioning = 1.0 + 0.5 * np.sin(radius * 10)
        
        # Sinusoidal periodic terms with varying frequencies and amplitudes
        periodic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.0 + 0.3 * np.cos(i * 0.3)
            periodic += amp * np.sin(freq * x_normalized[i])
            
        # Multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            # Create multiple valleys using cosine terms
            multimodal += np.cos(3 * x_normalized[i]) + 0.5 * np.cos(6 * x_normalized[i])
            
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine components with dynamic weights
        result = condition_factor * (0.5 * radius**2 + 0.3 * periodic + 0.2 * multimodal)
        
        # Add a global minimum offset
        global_min_offset = 0.1 * np.sum(np.sin(x_normalized * 2))
        result += global_min_offset
        
        return result