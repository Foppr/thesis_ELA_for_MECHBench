import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with improved distribution
        self.chaos_params = [0.6 + 0.2 * np.sin(0.5 * i + 1.2) for i in range(dim)]
        self.ridge_scales = [1.2 + 0.3 * np.cos(0.7 * i + 0.4) for i in range(dim)]
        self.harmonic_freqs = [1.8 + 0.4 * np.sin(0.4 * i + 0.3) for i in range(dim)]
        self.saddle_strengths = [0.9 + 0.3 * np.cos(0.8 * i + 0.2) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic gradient components with dimension-specific chaos
        for i in range(self.dim):
            xi = x[i]
            chaos = self.chaos_params[i]
            # Enhanced chaotic modulation with improved nonlinearity
            result += (xi**2) * (1.0 + chaos * np.sin(xi) * np.cos(xi) + 0.1 * np.sin(3*xi))
            
        # Add adaptive ridge structures with modified scales and orientations
        for i in range(self.dim):
            xi = x[i]
            scale = self.ridge_scales[i]
            # Enhanced ridge structure with multi-dimensional coupling and damping
            ridge = np.exp(-scale * xi**2) * np.sin(scale * xi) * (1.0 + 0.2 * np.cos(2*xi))
            result += ridge
            
        # Add harmonic interference patterns with refined frequencies
        for i in range(self.dim):
            xi = x[i]
            freq = self.harmonic_freqs[i]
            # Multi-harmonic interference with phase modulation and amplitude control
            for k in range(1, 5):
                phase = 0.2 * np.sin(k * xi + k * 0.4)
                amp = 1.0 / (k * k + 1.0)
                result += amp * np.sin(freq * k * xi + phase) * np.cos(freq * k * xi + phase)
                
        # Add saddle-point dominance with enhanced coupling
        for i in range(self.dim):
            xi = x[i]
            saddle = self.saddle_strengths[i]
            # Enhanced saddle point with coupled terms and additional nonlinearity
            result += saddle * xi * np.sin(xi) * np.cos(xi) + 0.1 * xi**3
            
        # Add global scaling and asymmetry to control landscape bias
        global_scale = 1.0 + 0.15 * np.sin(0.6 * self.dim + 0.3)
        asymmetry = 0.03 * np.sum(x**3) + 0.02 * np.sum(np.abs(x)**4)
        result = result * global_scale + asymmetry
        
        # Add final chaotic modulation for enhanced optimization difficulty
        chaotic_mod = 0.015 * np.sum(np.sin(8.0 * x) * np.cos(4.0 * x) + 0.5 * np.sin(12.0 * x))
        result += chaotic_mod
        
        return result