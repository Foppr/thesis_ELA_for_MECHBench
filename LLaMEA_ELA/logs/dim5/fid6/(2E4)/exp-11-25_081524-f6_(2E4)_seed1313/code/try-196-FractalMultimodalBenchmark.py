import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.noise_level = 0.05
        self.iterations = 5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Apply fractal-like transformation using complex polynomial mappings
        for i in range(self.dim):
            # Create a fractal-like component with iterative polynomial mapping
            val = x[i]
            fractal_val = 0.0
            
            for k in range(self.iterations):
                # Complex polynomial mapping with dynamic coefficients
                coeff = np.sin(0.5 * (i + k) * np.pi / self.dim)
                val = val**3 + coeff * val**2 + 0.1 * val + np.random.normal(0, self.noise_level)
                fractal_val += val**2
            
            result += fractal_val
        
        # Add multi-scale harmonic interference
        harmonic_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x[i] - x[j])
                freq = 2.0 + 3.0 * np.sin(0.1 * (i + j))
                harmonic_component += np.sin(freq * dist) * np.cos(freq * dist)
        
        # Add basin-like attraction regions with dynamic centers
        basin_component = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.3 * i + 0.5)
            dist_from_center = np.abs(x[i] - center)
            basin_component += (dist_from_center**4) * np.exp(-dist_from_center)
        
        # Combine components with dynamic weights
        w1 = 0.4 + 0.2 * np.sin(0.3 * self.dim)
        w2 = 0.3 + 0.15 * np.cos(0.2 * self.dim)
        w3 = 0.3 + 0.2 * np.sin(0.4 * self.dim)
        
        result = w1 * result + w2 * harmonic_component + w3 * basin_component
        
        # Apply dimensionality scaling
        if self.dim > 1:
            scale_factor = 1.0 + 0.05 * np.log(self.dim) + 0.005 * self.dim**1.2
            result *= scale_factor
            
        return result