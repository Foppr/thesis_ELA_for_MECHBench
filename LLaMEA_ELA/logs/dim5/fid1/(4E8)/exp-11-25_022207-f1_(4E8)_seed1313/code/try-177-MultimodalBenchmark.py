import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map modulation with altered coefficient for increased complexity
        chaos_mod = np.sum(3.9 * x_norm * (1 - x_norm))
        
        # Multi-scale Gaussian peaks with shifted locations and modified widths
        peaks = 0
        scales = [0.4, 1.2, 1.8]
        heights = [1.4, 0.6, 0.25]
        for i, (scale, height) in enumerate(zip(scales, heights)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - np.sin(i * 0.35)) / scale)**2))
        
        # Gradient-asymmetric corridor with modified frequency and amplitude
        asym_corridor = np.sum(np.abs(x_norm) * np.exp(-0.2 * x_norm**2) * 
                              np.sin(5.0 * np.pi * x_norm) * 
                              np.cos(1.5 * np.pi * x_norm))
        
        # Polynomial coupling with altered exponent and trigonometric modulation
        poly_coupling = np.sum((x_norm[:-1]**4 + x_norm[1:]**4)**2 * 
                              np.cos(3.0 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                              np.exp(-0.3 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Saddle-point repulsion with modified decay and frequency
        saddle_repulse = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**4 * 
                               np.exp(-0.5 * (x_norm[:-1] + x_norm[1:])**2) * 
                               np.sin(4.0 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Fractal-like chaotic component with altered frequencies and added tanh modulation
        fractal = np.sum(np.sin(10.0 * np.pi * x_norm) * 
                        np.cos(6.5 * np.pi * x_norm) * 
                        np.exp(-0.3 * np.abs(x_norm)) * 
                        np.tanh(0.3 * x_norm))
        
        # Combined function with chaotic noise
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal
        
        # Add small random perturbation for robustness
        noise = 0.025 * np.random.rand()
        
        return result + noise