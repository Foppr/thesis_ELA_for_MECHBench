import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize time-variant fractal parameters with chaotic scaling
        self.fractal_dims = [0.3 + 0.7 * np.sin(0.5 * i + np.cos(i)) for i in range(dim)]
        self.curvature_params = [1.2 + 0.8 * np.cos(0.7 * i + np.sin(i)) for i in range(dim)]
        self.interference_amplitudes = [0.6 + 0.4 * np.cos(0.4 * i + np.sin(2*i)) for i in range(dim)]
        self.scale_factors = [0.8 + 0.4 * np.sin(0.6 * i + np.cos(2*i)) for i in range(dim)]
        # Add chaotic time-dependent components
        self.time_factor = 1.0 + 0.3 * np.sin(0.1 * dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic fractal self-similar patterns with time-varying dimensions
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dims[i] * self.time_factor
            # Multi-scale chaotic component using log-periodic scaling
            result += np.sin(xi) * np.cos(xi) * (1.0 + 0.4 * np.sin(fractal_dim * xi + np.cos(xi)))
            
        # Add dynamic curvature with time-dependent modulation
        for i in range(self.dim):
            xi = x[i]
            curvature = self.curvature_params[i] * self.time_factor
            # Time-variant quadratic curvature with chaotic coupling
            result += curvature * (xi**2) * (1.0 + 0.4 * np.cos(curvature * xi + np.sin(xi)))
            
        # Add nested multi-scale interference with chaotic frequency modulation
        for i in range(self.dim):
            xi = x[i]
            amp = self.interference_amplitudes[i] * self.time_factor
            scale = self.scale_factors[i] * self.time_factor
            # Multi-frequency interference with chaotic phase coupling
            for k in range(1, 8):
                freq = k * scale * (1.0 + 0.3 * np.sin(k * xi + np.cos(k * xi)))
                result += amp * np.sin(freq * xi) * np.cos(freq * xi + np.sin(xi))
                
        # Add hierarchical fractal components with chaotic smoothness
        for i in range(self.dim):
            xi = x[i]
            # Fractal ridge structures with time-varying smoothness
            smoothness = 1.0 + 0.5 * np.sin(0.6 * i + np.cos(i)) * self.time_factor
            result += np.exp(-smoothness * xi**2) * np.sin(smoothness * xi + np.cos(xi))
            
        # Add dimensionality-dependent global scaling with chaotic asymmetry
        global_factor = 1.0 + 0.3 * np.sin(0.4 * self.dim + np.cos(self.dim))
        asymmetry = 0.15 * np.cos(0.5 * self.dim + np.sin(self.dim))
        result = result * global_factor + asymmetry * np.sum(x**3)
        
        # Add stochastic resonance with chaotic modulation
        stochastic_mod = 0.08 * np.sum(np.sin(12.0 * x + np.cos(10.0 * x)) * np.cos(9.0 * x + np.sin(7.0 * x)))
        result += stochastic_mod
        
        # Add time-variant chaotic noise component
        chaos_noise = 0.03 * np.sum(np.sin(self.dim * x) * np.cos(self.dim * x + np.sin(x)))
        result += chaos_noise
        
        return result