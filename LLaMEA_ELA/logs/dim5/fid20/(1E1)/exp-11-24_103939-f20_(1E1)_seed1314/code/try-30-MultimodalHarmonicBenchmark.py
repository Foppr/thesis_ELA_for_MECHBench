import numpy as np

class MultimodalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial potential landscape with varying degrees
        f1 = np.sum(x_scaled**4 + 0.5 * x_scaled**3 + 0.2 * x_scaled**2)
        
        # Harmonic interference terms creating intricate local minima
        f2 = 0.6 * np.sum(np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                         np.sin(6 * x_scaled) * np.cos(4 * x_scaled))
        
        # Adaptive scaling based on dimensionality to increase complexity
        adaptive_scale = 1.0 + 0.3 * np.log(self.dim + 1)
        f3 = adaptive_scale * np.sum(np.exp(-x_scaled**2) * 
                                   (np.sin(15 * x_scaled)**2 + 
                                    np.cos(12 * x_scaled)**2))
        
        # Cross-dimensional coupling with non-linear interaction
        f4 = 0.4 * np.sum((x_scaled[0] * x_scaled[1] + 
                          x_scaled[2] * x_scaled[3])**2 if self.dim >= 4 else 0)
        
        # Multi-scale sinusoidal modulation with varying amplitudes
        f5 = 0.5 * np.sum(np.sin(25 * x_scaled) * 
                         np.cos(20 * x_scaled) * 
                         np.sin(15 * x_scaled) * 
                         np.cos(10 * x_scaled))
        
        # Gaussian mixture with varying centers and widths
        centers = np.linspace(-0.5, 0.5, 5)
        f6 = 0.3 * np.sum([np.exp(-0.5 * (x_scaled - c)**2 / 0.1) for c in centers])
        
        # Fractional power law modulation to create rugged terrain
        f7 = 0.4 * np.sum(np.abs(x_scaled)**1.5 * 
                         np.sin(30 * x_scaled)**2)
        
        # Logarithmic barrier terms to induce sharp gradients
        f8 = 0.35 * np.sum(np.log(1 + 0.1 * np.abs(x_scaled)) * 
                          np.cos(25 * x_scaled)**2)
        
        # Additional high-frequency oscillation for increased ruggedness
        f9 = 0.25 * np.sum(np.sin(40 * x_scaled) * 
                          np.cos(35 * x_scaled) * 
                          np.sin(30 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9