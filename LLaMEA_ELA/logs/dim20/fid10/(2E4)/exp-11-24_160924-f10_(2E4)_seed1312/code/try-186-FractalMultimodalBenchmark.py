import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize time-variant fractal parameters with slightly altered chaotic scaling
        self.fractal_dims = [0.35 + 0.65 * np.sin(0.55 * i + np.cos(i)) for i in range(dim)]
        self.curvature_params = [1.15 + 0.85 * np.cos(0.75 * i + np.sin(i)) for i in range(dim)]
        self.interference_amplitudes = [0.55 + 0.45 * np.cos(0.45 * i + np.sin(2*i)) for i in range(dim)]
        self.scale_factors = [0.85 + 0.35 * np.sin(0.65 * i + np.cos(2*i)) for i in range(dim)]
        # Add slightly modified chaotic time-dependent components
        self.time_factor = 1.05 + 0.25 * np.sin(0.12 * dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic fractal self-similar patterns with time-varying dimensions
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dims[i] * self.time_factor
            # Multi-scale chaotic component using log-periodic scaling
            result += np.sin(xi) * np.cos(xi) * (1.0 + 0.35 * np.sin(fractal_dim * xi + np.cos(xi)))
            
        # Add dynamic curvature with time-dependent modulation
        for i in range(self.dim):
            xi = x[i]
            curvature = self.curvature_params[i] * self.time_factor
            # Time-variant quadratic curvature with chaotic coupling
            result += curvature * (xi**2) * (1.0 + 0.35 * np.cos(curvature * xi + np.sin(xi)))
            
        # Add nested multi-scale interference with chaotic frequency modulation
        for i in range(self.dim):
            xi = x[i]
            amp = self.interference_amplitudes[i] * self.time_factor
            scale = self.scale_factors[i] * self.time_factor
            # Multi-frequency interference with chaotic phase coupling
            for k in range(1, 7):
                freq = k * scale * (1.0 + 0.25 * np.sin(k * xi + np.cos(k * xi)))
                result += amp * np.sin(freq * xi) * np.cos(freq * xi + np.sin(xi))
                
        # Add hierarchical fractal components with chaotic smoothness
        for i in range(self.dim):
            xi = x[i]
            # Fractal ridge structures with time-varying smoothness
            smoothness = 1.0 + 0.45 * np.sin(0.65 * i + np.cos(i)) * self.time_factor
            result += np.exp(-smoothness * xi**2) * np.sin(smoothness * xi + np.cos(xi))
            
        # Add dimensionality-dependent global scaling with chaotic asymmetry
        global_factor = 1.0 + 0.25 * np.sin(0.42 * self.dim + np.cos(self.dim))
        asymmetry = 0.13 * np.cos(0.52 * self.dim + np.sin(self.dim))
        result = result * global_factor + asymmetry * np.sum(x**3)
        
        # Add stochastic resonance with chaotic modulation
        stochastic_mod = 0.07 * np.sum(np.sin(11.5 * x + np.cos(9.5 * x)) * np.cos(8.5 * x + np.sin(6.5 * x)))
        result += stochastic_mod
        
        # Add time-variant chaotic noise component
        chaos_noise = 0.025 * np.sum(np.sin(self.dim * x) * np.cos(self.dim * x + np.sin(x)))
        result += chaos_noise
        
        return result