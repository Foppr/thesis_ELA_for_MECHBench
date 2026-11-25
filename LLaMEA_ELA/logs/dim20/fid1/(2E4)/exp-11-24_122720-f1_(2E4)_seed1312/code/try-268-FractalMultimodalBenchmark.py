import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.fractal_dim = 1.5 + 0.5 * np.random.rand()
        self.frequency_base = 2.0 + np.random.rand() * 3.0
        self.scale_factors = [np.power(2.0, i) for i in range(dim)]
        self.rotation_angles = [np.pi * np.random.rand() for _ in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component with self-similar structure
        fractal_term = 0.0
        for i in range(self.dim):
            # Apply rotation and scaling
            rotated_x = x[i] * np.cos(self.rotation_angles[i]) - x[(i+1) % self.dim] * np.sin(self.rotation_angles[i])
            scaled_x = rotated_x * self.scale_factors[i]
            
            # Multi-scale frequency components
            freq = self.frequency_base * np.power(2.0, i)
            fractal_term += np.sin(freq * scaled_x) * np.cos(freq * scaled_x)
            
        # Complex gradient field with curvature modulation
        gradient_field = 0.0
        for i in range(self.dim):
            # Scale-invariant curvature
            curvature = np.power(np.abs(x[i]), 1.5) + 0.5 * np.sin(3.0 * x[i])
            gradient_field += curvature * np.cos(x[i] * self.frequency_base)
            
        # Self-similar basin structure with multiple local minima
        basin_structure = 0.0
        for i in range(self.dim):
            # Create fractal-like valleys
            valley_depth = np.sin(x[i] * self.frequency_base) + 0.3 * np.sin(2.0 * x[i] * self.frequency_base)
            basin_structure += valley_depth * np.exp(-0.1 * x[i]**2)
            
        # Scale-invariant scaling factor
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components
        result = scale_factor * (fractal_term + gradient_field + basin_structure)
        
        return result