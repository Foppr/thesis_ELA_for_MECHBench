import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic modular structure with modified logistic map coefficients
        chaos_mod = 0
        for i in range(self.dim):
            chaos_mod += 3.6 * x_norm[i] * (1 - x_norm[i]) * np.sin(2.2 * np.pi * x_norm[i] * (i + 1.2))
        
        # Multi-scale fractal peaks with altered heights and positions
        peaks = 0
        scales = [0.25, 0.55, 1.05, 1.45, 2.05]
        heights = [2.2, 1.3, 0.7, 0.35, 0.15]
        positions = [np.sin(i * 1.25) for i in range(5)]
        for i, (scale, height, pos) in enumerate(zip(scales, heights, positions)):
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - pos) / scale)**2))
        
        # Gradient-asymmetric corridor structure with altered frequencies
        asym_corridor = 0
        for i in range(self.dim):
            asym_corridor += np.abs(x_norm[i]) * np.exp(-0.12 * x_norm[i]**2) * \
                           np.sin(4.8 * np.pi * x_norm[i] + i * 0.55) * \
                           np.cos(3.8 * np.pi * x_norm[i] + i * 0.35) * \
                           np.tan(0.55 * x_norm[i])
        
        # Polynomial coupling with modified exponents and trigonometric modulation
        poly_coupling = 0
        for i in range(self.dim - 1):
            term = (x_norm[i]**2.8 + x_norm[i+1]**2.8)**2.5 * \
                   np.cos(6.8 * np.pi * (x_norm[i] + x_norm[i+1])) * \
                   np.exp(-0.32 * (x_norm[i] - x_norm[i+1])**2)
            poly_coupling += term
        
        # Saddle-point repulsion with modified scaling and interaction
        saddle_repulse = 0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            sum_vals = x_norm[i] + x_norm[i+1]
            term = (x_norm[i]**2.9 - x_norm[i+1]**2.9)**1.8 * \
                   np.exp(-0.48 * sum_vals**2) * \
                   np.sin(7.5 * np.pi * diff)
            saddle_repulse += term
        
        # Fractal-like chaotic component with modified frequencies
        fractal = 0
        freqs = [14, 11, 8, 5, 2]
        for i in range(self.dim):
            fractal += np.sin(freqs[i % len(freqs)] * np.pi * x_norm[i]) * \
                      np.cos(freqs[i % len(freqs)] * np.pi * x_norm[i]) * \
                      np.exp(-0.31 * np.abs(x_norm[i])) * \
                      np.tan(0.48 * x_norm[i]) * \
                      np.sin(0.75 * x_norm[i])
        
        # Combined function with chaotic noise and dynamic scaling
        result = chaos_mod + peaks + asym_corridor + poly_coupling + saddle_repulse + fractal
        
        # Add dynamic random perturbation for robustness
        noise = 0.14 * np.random.rand() * (1 + 0.58 * np.sin(np.sum(x_norm)))
        
        return result + noise