import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base fractal component with recursive self-similarity
        def fractal_component(x_vec):
            result = 0.0
            scale = 1.0
            for i in range(1, 6):  # 5 levels of recursion
                # Scale and shift coordinates
                scaled_x = x_vec * scale
                # Apply nested trigonometric patterns
                pattern = np.sin(scaled_x * (2**i)) * np.cos(scaled_x * (3**i))
                # Add fractal scaling factor
                result += (1.0 / (2**i)) * np.sum(pattern**2)
                scale *= 0.5
            return result
        
        # Radial fractal component
        r = np.sqrt(np.sum(x_norm**2))
        radial_fractal = fractal_component(x_norm)
        
        # Angular fractal component with multiple scales
        if self.dim == 1:
            angular_fractal = 0.0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_fractal = 0.0
            for i in range(1, 4):
                angular_fractal += (1.0 / (3**i)) * np.sin(angles * (5**i)) * np.cos(angles * (7**i))
        
        # Multi-scale cross-dimensional coupling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                # Apply fractal scaling to coupling strength
                coupling_strength = 1.0 / (1.0 + dist**2)
                # Nested oscillatory interaction
                cross_coupling += coupling_strength * (
                    np.sin(10 * (x_norm[i]**2 + x_norm[j]**2)) * 
                    np.cos(15 * (x_norm[i]**3 + x_norm[j]**3)) +
                    0.5 * np.sin(20 * (x_norm[i]**4 + x_norm[j]**4)) *
                    np.cos(25 * (x_norm[i]**5 + x_norm[j]**5))
                )
        
        # Fractal noise component with multiple frequencies
        noise = 0.0
        for i in range(1, 8):
            freq = 2**i
            noise += (1.0 / (2**i)) * np.sin(freq * np.pi * x_norm) ** (i + 1)
        
        # Scale-invariant periodic structure
        periodic = 0.0
        for i in range(1, 6):
            wavelength = 2**i
            periodic += (1.0 / (2**i)) * np.sin(r * wavelength) * np.cos(r * wavelength)
        
        # Global conditioning with fractal dimension scaling
        cond_factor = 1.0 + 2.0 * (self.dim / (self.dim + 1.0))
        
        # Combine all components with fractal weighting
        return cond_factor * (
            radial_fractal + 
            angular_fractal + 
            cross_coupling + 
            noise + 
            periodic
        ) * (1.0 + 0.2 * np.sin(5 * r))