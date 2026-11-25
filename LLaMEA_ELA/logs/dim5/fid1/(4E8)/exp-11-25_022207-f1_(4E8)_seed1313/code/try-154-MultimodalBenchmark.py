import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map modulation for non-linearity with dynamic scaling
        chaos_mod = np.sum(3.5 * x_norm * (1 - x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Multi-scale Gaussian peaks with varying heights, widths, and positions
        peaks = 0
        scales = [0.3, 0.7, 1.2, 1.8]
        heights = [1.5, 0.8, 0.4, 0.2]
        positions = [np.sin(i) for i in range(4)]
        for i, (scale, height, pos) in enumerate(zip(scales, heights, positions)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - pos) / scale)**2))
        
        # Gradient-asymmetric corridor structure with dynamic frequency
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.15 * x_norm**2) * 
                              np.sin(4 * np.pi * x_norm) * 
                              np.cos(3 * np.pi * x_norm) * 
                              np.tan(0.5 * x_norm))
        
        # Polynomial coupling with trigonometric modulation and dynamic exponents
        poly_coupling = 0
        for i in range(self.dim - 1):
            term = (x_norm[i]**2 + x_norm[i+1]**2)**4 * \
                   np.cos(5 * np.pi * (x_norm[i] + x_norm[i+1])) * \
                   np.exp(-0.25 * (x_norm[i] - x_norm[i+1])**2)
            poly_coupling += term
        
        # Saddle-point repulsion with exponential decay and adaptive scaling
        saddle_repulse = 0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            sum_vals = x_norm[i] + x_norm[i+1]
            term = (x_norm[i]**2 - x_norm[i+1]**2)**3 * \
                   np.exp(-0.4 * sum_vals**2) * \
                   np.sin(6 * np.pi * diff)
            saddle_repulse += term
        
        # Fractal-like chaotic component with multiple frequency components
        fractal = np.sum(np.sin(12 * np.pi * x_norm) * 
                        np.cos(9 * np.pi * x_norm) * 
                        np.exp(-0.25 * np.abs(x_norm)) * 
                        np.tan(0.4 * x_norm) * 
                        np.sin(0.7 * x_norm))
        
        # Combined function with chaotic noise and dynamic scaling
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal
        
        # Add dynamic random perturbation for robustness
        noise = 0.1 * np.random.rand() * (1 + 0.5 * np.sin(np.sum(x_norm)))
        
        return result + noise