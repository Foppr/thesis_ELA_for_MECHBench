import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters with dimension-dependent scaling
        self.fractal_dims = [0.5 + 0.3 * np.sin(0.4 * i) for i in range(dim)]
        self.curvature_params = [1.0 + 0.5 * np.cos(0.6 * i) for i in range(dim)]
        self.interference_amplitudes = [0.8 + 0.2 * np.sin(0.3 * i) for i in range(dim)]
        self.scale_factors = [1.0 + 0.3 * np.cos(0.5 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add fractal-like self-similar patterns with varying dimensions
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dims[i]
            # Multi-scale fractal component using power-law scaling
            result += np.sin(xi) * np.cos(xi) * (1.0 + 0.5 * np.sin(fractal_dim * xi))
            
        # Add dynamic curvature structures with dimension coupling
        for i in range(self.dim):
            xi = x[i]
            curvature = self.curvature_params[i]
            # Adaptive quadratic curvature with fractal-like modulation
            result += curvature * (xi**2) * (1.0 + 0.3 * np.cos(curvature * xi))
            
        # Add multi-scale interference patterns with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            amp = self.interference_amplitudes[i]
            scale = self.scale_factors[i]
            # Multi-frequency interference with dynamic scaling
            for k in range(1, 6):
                freq = k * scale * (1.0 + 0.2 * np.sin(k * xi))
                result += amp * np.sin(freq * xi) * np.cos(freq * xi)
                
        # Add hierarchical fractal components with exponential decay
        for i in range(self.dim):
            xi = x[i]
            # Fractal ridge structures with varying smoothness
            smoothness = 1.0 + 0.4 * np.sin(0.5 * i)
            result += np.exp(-smoothness * xi**2) * np.sin(smoothness * xi)
            
        # Add dimensionality-dependent global scaling and asymmetry
        global_factor = 1.0 + 0.2 * np.sin(0.3 * self.dim)
        asymmetry = 0.1 * np.cos(0.4 * self.dim)
        result = result * global_factor + asymmetry * np.sum(x**3)
        
        # Add final stochastic modulation with improved variance control
        stochastic_mod = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x))
        result += stochastic_mod
        
        # Add enhanced complexity through fractional polynomial terms
        for i in range(self.dim):
            xi = x[i]
            alpha = 0.7 + 0.3 * np.sin(0.2 * i)
            beta = 0.8 + 0.2 * np.cos(0.3 * i)
            result += 0.1 * (np.abs(xi)**alpha) * np.sin(beta * xi)
            
        # Add cross-dimensional coupling with improved smoothness
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                coupling_strength = 0.05 * (1.0 + np.sin(0.1 * (i+j)))
                result += coupling_strength * np.sin(xi) * np.cos(xj) * np.exp(-0.1 * (xi**2 + xj**2))
                
        # Add improved global structure with better conditioning
        result += 0.01 * np.sum((x - np.mean(x))**4)
        
        return result