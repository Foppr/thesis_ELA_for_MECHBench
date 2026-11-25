import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like scaling factors
        self.scaling_factors = [0.5 + 0.5 * np.sin(0.3 * i) for i in range(dim)]
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        quadratic = 0.1 * np.sum(x**2)
        
        # Composite Gaussian peaks with fractal-like structure
        gaussian_terms = 0.0
        for i in range(self.dim):
            # Multiple overlapping Gaussians with varying widths and heights
            for j in range(3):
                center = 2.0 * np.sin(0.5 * i + j) * 5.0
                width = 0.5 + 0.3 * np.cos(0.4 * i + j)
                height = 1.0 + 0.5 * np.sin(0.6 * i + j)
                gaussian_terms += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
                
            # Add fractal-like self-similarity with recursive scaling
            if i > 0:
                scale = self.scaling_factors[i]
                gaussian_terms += 0.3 * np.exp(-0.5 * ((x[i] - x[i-1]) / (0.2 + 0.1 * scale))**2)
        
        # Adaptive gradient modulation based on position
        adaptive_gradient = 0.0
        for i in range(self.dim):
            # Position-dependent gradient scaling
            grad_scale = 1.0 + 0.3 * np.sin(0.7 * x[i])
            adaptive_gradient += grad_scale * np.sin(x[i])**2
            
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited range coupling
                coupling_strength = 0.2 + 0.1 * np.sin(0.5 * (i + j))
                cross_coupling += coupling_strength * np.sin(x[i]) * np.cos(x[j])
                
        # Add harmonic interference patterns
        interference = 0.0
        for i in range(self.dim):
            interference += 0.2 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            interference += 0.15 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
        
        # Combine all components
        return quadratic + 1.5 * gaussian_terms + 0.8 * adaptive_gradient + 0.6 * cross_coupling + 0.4 * interference