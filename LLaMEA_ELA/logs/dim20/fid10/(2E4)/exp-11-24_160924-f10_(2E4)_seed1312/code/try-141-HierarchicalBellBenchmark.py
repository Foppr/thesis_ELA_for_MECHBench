import numpy as np

class HierarchicalBellBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add hierarchical bell-shaped peaks with varying heights, widths, and positions
        for i in range(self.dim):
            xi = x[i]
            height = 2.0 + 1.5 * np.sin(0.5 * i)
            width = 1.0 + 0.5 * np.cos(0.3 * i)
            position = -3.0 + 6.0 * np.random.random()
            result += height * np.exp(-0.5 * ((xi - position) / width)**2)
            
        # Add adaptive correlation terms with dimension-dependent strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 0.4 * np.sin(0.2 * (i + j)) * np.cos(0.1 * (i - j))
                distance = np.abs(x[i] - x[j])
                result += corr_strength * np.exp(-distance**2 / (0.5 + 0.2 * i))
                
        # Add dynamic noise components with fractal-like characteristics
        for i in range(self.dim):
            noise = 0.3 * np.sin(3.0 * x[i] + i) * np.cos(2.0 * x[i] - i)
            result += noise
            
        # Add multi-scale sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = 1.0 + 0.6 * np.sin(0.4 * i)
            amp = 0.8 + 0.4 * np.cos(0.3 * i)
            result += amp * np.sin(freq * xi) * np.cos(0.5 * xi)
            
        # Add hierarchical structure through recursive peak interactions
        if self.dim >= 3:
            for k in range(1, min(3, self.dim)):
                scale_factor = 0.3**(k/2)
                for i in range(self.dim - k):
                    result += scale_factor * np.exp(-0.5 * ((x[i] - x[i+k]) / (0.5 + 0.2 * k))**2)
                    
        # Add adaptive coupling terms with varying influence
        for i in range(self.dim):
            xi = x[i]
            coupling = 0.6 + 0.3 * np.sin(0.5 * i)
            result += coupling * (xi**4 - 4*xi**2 + 2)
            
        # Add dimension-dependent complexity multiplier
        dim_factor = 1.0 + 0.3 * np.sin(0.7 * self.dim)
        result *= dim_factor
        
        # Add saddle point structure with varying curvature
        for i in range(self.dim):
            xi = x[i]
            curvature = 0.8 + 0.4 * np.cos(0.6 * i)
            result += curvature * (xi**3 - 3*xi)
            
        return result