import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like cosine structure with recursive self-similarity
        fractal = np.sum(np.cos(2 ** (np.arange(self.dim) + 1) * np.pi * x_norm) * 
                        np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Adaptive noise modulation based on local gradient magnitude
        grad_magnitude = np.sqrt(np.sum((np.gradient(x_norm, axis=0))**2))
        adaptive_noise = np.random.normal(0, 1) * (1 + 0.3 * np.tanh(grad_magnitude))
        
        # Multi-scale Gaussian peaks with fractal spacing
        peaks = 0
        for i in range(1, 6):
            scale = 2 ** (-i)
            peak_positions = np.linspace(-1, 1, 2**i + 1)[1::2]  # Midpoints
            for pos in peak_positions:
                peaks += np.exp(-0.5 * ((x_norm - pos) / (scale * 0.5))**2)
        
        # Corridor structure with varying width and orientation
        corridor = np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                         np.cos(4 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                         np.sin(2 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Hyperbolic tangent modulation for gradient complexity
        tanh_mod = np.sum(np.tanh(3 * x_norm) * np.exp(-0.4 * x_norm**2))
        
        # Scale-invariant polynomial coupling with fractal exponentiation
        poly_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**(2 + 0.5 * np.sin(np.pi * x_norm[:-1])) * 
                              np.exp(-0.3 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Dynamic repulsion field with time-varying parameters
        repulsion = np.sum(np.exp(-2 * (x_norm**2).sum()) * 
                          np.sin(5 * np.pi * x_norm) * 
                          np.cos(3 * np.pi * x_norm.sum()) * 
                          np.tan(0.3 * x_norm))
        
        # Combine all components
        result = fractal + peaks + corridor + tanh_mod + poly_coupling + repulsion + adaptive_noise
        
        return result