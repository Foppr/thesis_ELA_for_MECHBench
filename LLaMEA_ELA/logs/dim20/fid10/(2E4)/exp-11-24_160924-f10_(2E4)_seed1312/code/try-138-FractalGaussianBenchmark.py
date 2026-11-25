import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add multi-scale Gaussian peaks with varying heights, widths, and positions
        for i in range(self.dim):
            xi = x[i]
            scale = 1.0 + 0.4 * np.sin(0.25 * i)
            height = 1.0 + 0.6 * np.cos(0.3 * i)
            width = 0.4 + 0.2 * np.sin(0.5 * i)
            peak_pos = 1.5 * np.cos(0.4 * i)
            result += height * np.exp(-0.5 * ((xi - peak_pos) / (width * scale))**2)
            
        # Add fractal-like correlation terms with adaptive strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 0.4 * np.sin(0.3 * (i + j)) * np.cos(0.2 * (i - j))
                distance = np.abs(x[i] - x[j])
                result += corr_strength * np.exp(-distance**2 / (1.5 + 0.2 * i * j))
                
        # Add adaptive coupling terms with dimension-dependent modulation
        for i in range(self.dim):
            xi = x[i]
            coupling = 0.6 + 0.2 * np.sin(0.3 * i)
            result += coupling * (xi**6 - 2*xi**4 + xi**2)
            
        # Add multi-scale sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = 1.2 + 0.3 * np.sin(0.4 * i)
            amp = 1.1 + 0.2 * np.cos(0.2 * i)
            result += amp * np.sin(freq * xi) * np.cos(0.6 * xi)
            
        # Add self-similar structure through recursive scaling with variable factors
        if self.dim >= 2:
            for k in range(1, min(5, self.dim)):
                scale_factor = 0.4**(k/3)
                for i in range(self.dim - k):
                    result += scale_factor * np.sin(x[i] + x[i+k])
                    
        # Add saddle point structure with varying curvature and dimensionality
        for i in range(self.dim):
            xi = x[i]
            curvature = 1.2 + 0.5 * np.sin(0.6 * i)
            result += curvature * (xi**4 - 4*xi**2)
            
        # Add irregular noise component with enhanced fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            noise += 0.15 * np.sin(6.0 * x[i] + i) * np.cos(2.5 * x[i] - i)
        result += noise
        
        # Add dimension-dependent complexity factor with enhanced scaling
        dim_factor = 1.1 + 0.3 * np.sin(0.7 * self.dim)
        result *= dim_factor
        
        # Add additional cross-dimensional interaction terms for increased challenge
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = 0.25 * np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                result += interaction * np.abs(x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        return result