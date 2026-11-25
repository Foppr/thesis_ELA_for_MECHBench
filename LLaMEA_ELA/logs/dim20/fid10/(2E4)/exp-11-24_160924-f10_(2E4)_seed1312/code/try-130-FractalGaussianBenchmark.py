import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add multi-scale Gaussian peaks with varying heights and widths
        for i in range(self.dim):
            xi = x[i]
            scale = 1.0 + 0.5 * np.sin(0.3 * i)
            height = 1.0 + 0.7 * np.cos(0.4 * i)
            width = 0.5 + 0.3 * np.sin(0.6 * i)
            peak_pos = 2.0 * np.cos(0.5 * i)
            result += height * np.exp(-0.5 * ((xi - peak_pos) / (width * scale))**2)
            
        # Add fractal-like correlation terms with diminishing returns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 0.3 * np.sin(0.2 * (i + j)) * np.cos(0.1 * (i - j))
                distance = np.abs(x[i] - x[j])
                result += corr_strength * np.exp(-distance**2 / (1.0 + 0.1 * i * j))
                
        # Add adaptive coupling terms that change based on dimension
        for i in range(self.dim):
            xi = x[i]
            coupling = 0.5 + 0.3 * np.sin(0.4 * i)
            result += coupling * (xi**6 - 2*xi**4 + xi**2)
            
        # Add multi-scale sinusoidal modulations
        for i in range(self.dim):
            xi = x[i]
            freq = 1.0 + 0.4 * np.sin(0.5 * i)
            amp = 1.0 + 0.3 * np.cos(0.3 * i)
            result += amp * np.sin(freq * xi) * np.cos(0.7 * xi)
            
        # Add self-similar structure through recursive scaling
        if self.dim >= 2:
            for k in range(1, min(4, self.dim)):
                scale_factor = 0.5**(k/2)
                for i in range(self.dim - k):
                    result += scale_factor * np.sin(x[i] + x[i+k])
                    
        # Add saddle point structure with varying curvature
        for i in range(self.dim):
            xi = x[i]
            curvature = 1.0 + 0.6 * np.sin(0.7 * i)
            result += curvature * (xi**4 - 4*xi**2)
            
        # Add irregular noise component with fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(5.0 * x[i] + i) * np.cos(3.0 * x[i] - i)
        result += noise
        
        # Add dimension-dependent complexity factor
        dim_factor = 1.0 + 0.2 * np.sin(0.8 * self.dim)
        result *= dim_factor
        
        return result