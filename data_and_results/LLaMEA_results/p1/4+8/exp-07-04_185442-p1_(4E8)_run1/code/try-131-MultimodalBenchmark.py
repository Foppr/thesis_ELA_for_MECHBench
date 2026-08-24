import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map dynamics with varying parameter
        tent_map = np.sum(np.where(np.abs(x_norm) < 0.5, 2 * np.abs(x_norm), 2 * (1 - np.abs(x_norm))))
        
        # Adaptive Gabor wavelet transformation
        gabor_real = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(3 * np.pi * x_norm))
        gabor_imag = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(3 * np.pi * x_norm))
        gabor_transform = gabor_real**2 + gabor_imag**2
        
        # Spherical harmonic couplings with degree and order variations
        sph_harm = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sph_harm += (x_norm[i] * x_norm[j]) / (1 + np.abs(x_norm[i] - x_norm[j])**2)
        
        # Non-separable polynomial cross-terms with exponential weights
        poly_cross = np.sum(np.exp(-x_norm**2) * (x_norm**3 + x_norm**4))
        
        # Mixed nonlinear coupling with logarithmic scaling
        log_coupling = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(7 * x_norm))
        
        # Add a small noise term to create more complex landscape
        noise = 0.01 * np.random.random()
        
        # Combine all terms to create a multimodal landscape
        return tent_map + gabor_transform + sph_harm + poly_cross + log_coupling + noise