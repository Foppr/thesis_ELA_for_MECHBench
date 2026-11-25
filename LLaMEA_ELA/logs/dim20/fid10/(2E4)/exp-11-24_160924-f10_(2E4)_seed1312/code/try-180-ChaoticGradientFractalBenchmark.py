import numpy as np

class ChaoticGradientFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors and chaos parameters
        self.fractal_scales = [1.0 + 0.5 * np.sin(0.3 * i) for i in range(dim)]
        self.chaos_params = [0.8 + 0.4 * np.cos(0.5 * i) for i in range(dim)]
        self.periodic_freqs = [2.0 + 0.6 * np.sin(0.4 * i) for i in range(dim)]
        self.curvature_adapt = [1.5 + 0.5 * np.cos(0.6 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base chaotic gradient component with fractal scaling
        for i in range(self.dim):
            xi = x[i]
            scale = self.fractal_scales[i]
            chaos = self.chaos_params[i]
            # Chaotic sine-cosine combination with varying frequency
            result += scale * np.sin(chaos * xi) * np.cos(chaos * xi)
            
        # Multi-scale periodic modulation with adaptive curvature
        for i in range(self.dim):
            xi = x[i]
            freq = self.periodic_freqs[i]
            curve = self.curvature_adapt[i]
            # Adaptive curvature modulation with multiple harmonic components
            result += 0.5 * np.sin(freq * xi) * np.cos(freq * xi) * (1.0 + 0.3 * np.sin(curve * xi))
            
        # Fractal-like interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimension coupling
                xi, xj = x[i], x[j]
                # Fractal interaction with varying strength
                strength = 0.2 * np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                result += strength * np.sin(xi + xj) * np.cos(xi - xj)
                
        # Enhanced chaotic interference pattern
        for i in range(self.dim):
            xi = x[i]
            # High-frequency chaotic modulation with dimension-dependent factor
            result += 0.3 * np.sin(12.0 * xi + 0.5 * i) * np.cos(9.0 * xi + 0.3 * i)
            
        # Adaptive nonlinearity based on coordinate magnitude
        for i in range(self.dim):
            xi = x[i]
            # Nonlinear transformation with dynamic exponent
            exp_factor = 1.0 + 0.4 * np.sin(0.7 * xi)
            result += 0.25 * (xi ** exp_factor) * np.sin(3.0 * xi)
            
        # Global scaling factor that changes with dimensionality
        global_scale = 1.2 + 0.2 * np.cos(0.2 * self.dim)
        result *= global_scale
        
        # Add dimensionality-dependent ruggedness
        ruggedness = 0.05 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x))
        result += ruggedness
        
        return result