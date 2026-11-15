import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors for multi-scale structure
        self.scales = np.logspace(-1, 1, min(dim, 10))
        # Precompute angular coordinates for radial symmetry
        self.angles = np.linspace(0, 2*np.pi, min(dim, 20), endpoint=False)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-scale trigonometric components with fractal scaling
        result = 0.0
        for i, scale in enumerate(self.scales):
            if i >= self.dim:
                break
            # Radial component with multiple frequencies
            r = np.sqrt(np.sum(x_norm**2))
            freq = 2**(i+1)
            radial_term = np.sin(freq * r) * np.cos(freq * r)
            
            # Angular component with self-similarity
            angle = np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0
            angular_term = np.sin(freq * angle) * np.cos(freq * angle)
            
            # Combine with scale factor
            result += scale * (radial_term + angular_term)
        
        # Add adaptive conditioning based on input magnitude
        condition_factor = 1.0 + 0.5 * np.sum(x_norm**2)
        
        # Introduce fractal-like self-similarity through recursive scaling
        if self.dim >= 2:
            # Create a self-similar pattern using coordinate transformations
            x1, x2 = x_norm[0], x_norm[1]
            fractal_pattern = np.sin(10 * x1) * np.cos(10 * x2) + \
                              np.sin(5 * x1) * np.cos(5 * x2) + \
                              np.sin(2 * x1) * np.cos(2 * x2)
            result += 0.1 * fractal_pattern
        
        # Add a global multimodal structure with multiple local minima
        multimodal = 0.0
        for i in range(min(self.dim, 5)):
            center = np.sin(i * np.pi / 3)
            dist = np.sum((x_norm - center)**2)
            multimodal += np.exp(-dist / (2 * 0.1**2)) * np.sin(5 * dist)
        
        # Combine all components
        total = result * condition_factor + 0.5 * multimodal
        
        # Add a final conditioning term to increase difficulty
        return total * (1 + 0.3 * np.sin(np.sum(x_norm**3)))