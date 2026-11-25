import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal structure
        self.fractal_scale = 0.5
        self.gaussian_amp = 1.0
        self.adaptive_factor = 2.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Composite Gaussian peaks with fractal scaling
        for i in range(self.dim):
            # Multiple overlapping Gaussians with varying centers and widths
            peak1 = self.gaussian_amp * np.exp(-0.5 * ((x[i] - 2.0) / 0.8)**2)
            peak2 = 0.7 * self.gaussian_amp * np.exp(-0.5 * ((x[i] + 2.0) / 1.2)**2)
            peak3 = 0.4 * self.gaussian_amp * np.exp(-0.5 * ((x[i] - 0.5) / 0.6)**2)
            peak4 = 0.6 * self.gaussian_amp * np.exp(-0.5 * ((x[i] + 1.0) / 1.0)**2)
            
            # Fractal-like scaling factor for each dimension
            fractal_factor = self.fractal_scale ** (i % 3)
            result += (peak1 + peak2 + peak3 + peak4) * fractal_factor
            
        # Adaptive gradient modulation with sine-wave interference
        grad_modulation = 0.0
        for i in range(self.dim):
            # Sine-based adaptive scaling
            scale_factor = 1.0 + 0.5 * np.sin(2.0 * x[i])
            # Cross-dimensional coupling with fractal interaction
            if i > 0:
                coupling = 0.3 * np.sin(x[i-1]) * np.cos(x[i]) * np.sin(0.5 * x[i-1] + 0.7 * x[i])
                grad_modulation += coupling * scale_factor
            
        # Add high-order polynomial basin terms for increased conditioning
        basin_term = 0.05 * np.sum(x**4) + 0.02 * np.sum(x**6) + 0.01 * np.sum(np.abs(x)**3)
        
        # Multi-scale harmonic interference pattern
        interference = 0.0
        for i in range(self.dim):
            interference += np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.5 * np.sin(2 * x[i])**2
        
        # Add adaptive conditioning with non-uniform scaling
        conditioning = 0.03 * np.sum(np.abs(x)**2.8) + 0.01 * np.sum(x**7)
        
        # Fractal self-similarity term with recursive structure
        fractal_self_sim = 0.0
        for i in range(self.dim):
            fractal_self_sim += (0.5 * np.sin(3 * x[i]) + 0.3 * np.cos(2 * x[i]))**2
        
        return result + grad_modulation + basin_term + interference + conditioning + fractal_self_sim