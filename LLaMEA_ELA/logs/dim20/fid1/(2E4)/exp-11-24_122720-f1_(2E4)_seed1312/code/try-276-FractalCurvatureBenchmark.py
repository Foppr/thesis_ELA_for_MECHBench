import numpy as np

class FractalCurvatureBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.fractal_dim = 1.5 + 0.5 * np.sin(dim * np.pi / 8)
        self.curvature_scale = 2.0 + 0.5 * np.cos(dim * np.pi / 6)
        self.noise_intensity = 0.3 + 0.1 * np.sin(dim * np.pi / 4)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like component with multi-scale curvature
        fractal_term = 0
        for i in range(self.dim):
            # Multi-scale sinusoidal patterns
            scale_factor = (i + 1) / self.dim
            freq = 2.0 * scale_factor * self.curvature_scale
            # Fractal-like structure with self-similarity
            fractal = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            # Add fractional dimension scaling
            fractal *= np.power(scale_factor, self.fractal_dim)
            fractal_term += fractal
            
        # Multi-scale curvature component
        curvature_term = 0
        for i in range(self.dim):
            # Different curvature scales
            scale = (i + 1) / self.dim
            # Adaptive quadratic with varying coefficients
            coeff = 1.0 + 0.5 * np.sin(scale * np.pi)
            curvature = coeff * x[i]**2 + 0.3 * x[i]**4
            # Scale by dimension
            curvature *= scale
            curvature_term += curvature
            
        # Adaptive noise component
        noise_term = 0
        for i in range(self.dim):
            # Noise with dimensionally adaptive intensity
            noise_intensity = self.noise_intensity * (i + 1) / self.dim
            # Multi-frequency noise
            noise = noise_intensity * (
                np.sin(x[i] * (i + 1)) + 
                0.5 * np.cos(x[i] * (i + 1) * 2) +
                0.3 * np.sin(x[i] * (i + 1) * 3)
            )
            noise_term += noise
            
        # Combine all components with appropriate weights
        result = 1.5 * fractal_term + 1.0 * curvature_term + 0.8 * noise_term
        
        # Add global scaling based on dimensionality
        global_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= global_scale
        
        return result