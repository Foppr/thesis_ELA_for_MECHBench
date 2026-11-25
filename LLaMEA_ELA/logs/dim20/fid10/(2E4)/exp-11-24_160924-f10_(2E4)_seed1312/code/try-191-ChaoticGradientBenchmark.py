import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = [0.5 + 0.3 * np.sin(0.4 * i + 1.0) for i in range(dim)]
        self.ridge_scales = [1.0 + 0.2 * np.cos(0.6 * i + 0.5) for i in range(dim)]
        self.harmonic_freqs = [2.0 + 0.5 * np.sin(0.3 * i + 0.2) for i in range(dim)]
        self.saddle_strengths = [0.8 + 0.4 * np.cos(0.7 * i + 0.3) for i in range(dim)]
        # Additional parameters for enhanced nonlinearity
        self.poly_orders = [3.0 + 0.5 * np.sin(0.5 * i + 0.1) for i in range(dim)]
        self.coupling_strengths = [0.3 + 0.2 * np.cos(0.8 * i + 0.4) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic gradient components with dimension-specific chaos
        for i in range(self.dim):
            xi = x[i]
            chaos = self.chaos_params[i]
            # Chaotic modulation of polynomial terms with sine-cosine mixing
            result += (xi**self.poly_orders[i]) * (1.0 + chaos * np.sin(xi) * np.cos(xi))
            
        # Add adaptive ridge structures with varying scales and orientations
        for i in range(self.dim):
            xi = x[i]
            scale = self.ridge_scales[i]
            # Ridge structure with exponential decay and multi-dimensional coupling
            ridge = np.exp(-scale * xi**2) * np.sin(scale * xi)
            result += ridge
            
        # Add harmonic interference patterns with dynamic frequencies
        for i in range(self.dim):
            xi = x[i]
            freq = self.harmonic_freqs[i]
            # Multi-harmonic interference with phase modulation
            for k in range(1, 4):
                phase = 0.3 * np.sin(k * xi + k * 0.5)
                result += np.sin(freq * k * xi + phase) * np.cos(freq * k * xi + phase)
                
        # Add saddle-point dominance with dimension coupling
        for i in range(self.dim):
            xi = x[i]
            saddle = self.saddle_strengths[i]
            # Saddle point with coupled terms creating complex curvature
            result += saddle * xi * np.sin(xi) * np.cos(xi)
            
        # Add higher-order coupling terms for enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strengths[i]
                result += coupling * x[i]**2 * x[j]**3 * np.sin(x[i] + x[j])
                
        # Add global scaling and asymmetry to control landscape bias
        global_scale = 1.0 + 0.1 * np.sin(0.5 * self.dim + 0.2)
        asymmetry = 0.05 * np.sum(x**3)
        result = result * global_scale + asymmetry
        
        # Add final chaotic modulation for enhanced optimization difficulty
        chaotic_mod = 0.02 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x))
        result += chaotic_mod
        
        return result