import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters with more structured dimension-dependent scaling
        self.fractal_dims = [0.5 + 0.4 * np.sin(0.5 * i + 1.0) for i in range(dim)]
        self.curvature_params = [1.2 + 0.3 * np.cos(0.7 * i + 0.5) for i in range(dim)]
        self.interference_amplitudes = [0.9 + 0.1 * np.sin(0.4 * i + 0.3) for i in range(dim)]
        self.scale_factors = [1.1 + 0.2 * np.cos(0.6 * i + 0.8) for i in range(dim)]
        # Add rotational coupling terms
        self.rotation_angles = [0.1 * np.sin(0.3 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add fractal-like self-similar patterns with varying dimensions
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dims[i]
            # Multi-scale fractal component using power-law scaling with enhanced smoothness
            result += np.sin(xi) * np.cos(xi) * (1.0 + 0.4 * np.sin(fractal_dim * xi))
            
        # Add dynamic curvature structures with dimension coupling and rotational effects
        for i in range(self.dim):
            xi = x[i]
            curvature = self.curvature_params[i]
            # Adaptive quadratic curvature with fractal-like modulation and rotation
            rotated_xi = xi * np.cos(self.rotation_angles[i]) - x[(i+1) % self.dim] * np.sin(self.rotation_angles[i])
            result += curvature * (rotated_xi**2) * (1.0 + 0.2 * np.cos(curvature * rotated_xi))
            
        # Add multi-scale interference patterns with varying frequencies and enhanced coupling
        for i in range(self.dim):
            xi = x[i]
            amp = self.interference_amplitudes[i]
            scale = self.scale_factors[i]
            # Multi-frequency interference with dynamic scaling and phase shifts
            for k in range(1, 5):
                freq = k * scale * (1.0 + 0.3 * np.sin(k * xi + k * 0.5))
                phase_shift = 0.2 * np.cos(k * xi)
                result += amp * np.sin(freq * xi + phase_shift) * np.cos(freq * xi + phase_shift)
                
        # Add hierarchical fractal components with exponential decay and adaptive smoothness
        for i in range(self.dim):
            xi = x[i]
            # Fractal ridge structures with varying smoothness and coupling effects
            smoothness = 1.0 + 0.3 * np.sin(0.6 * i + 0.4)
            result += np.exp(-smoothness * xi**2) * np.sin(smoothness * xi) * (1.0 + 0.1 * np.cos(xi))
            
        # Add dimensionality-dependent global scaling and improved asymmetry
        global_factor = 1.0 + 0.15 * np.sin(0.4 * self.dim + 0.2)
        asymmetry = 0.08 * np.cos(0.5 * self.dim + 0.3)
        result = result * global_factor + asymmetry * np.sum(x**3)
        
        # Add final stochastic modulation with better balance
        stochastic_mod = 0.03 * np.sum(np.sin(12.0 * x) * np.cos(6.0 * x))
        result += stochastic_mod
        
        # Add a new term to improve landscape regularity and reduce bias
        regularity_term = 0.05 * np.sum(np.abs(x)**1.5)
        result += regularity_term
        
        return result