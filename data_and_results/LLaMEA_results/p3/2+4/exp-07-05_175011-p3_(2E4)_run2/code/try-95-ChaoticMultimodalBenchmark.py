import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Composite sinusoidal waves with varying amplitudes and frequencies
        freqs = np.arange(1, self.dim + 1)
        sinusoidal = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Radial basis function components with shifted centers and varying widths
        rbf = 0.0
        centers = np.linspace(-0.5, 0.5, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                rbf += np.exp(-5 * (x_norm - centers[i])**2) * np.sin(10 * (x_norm - centers[i]))
        
        # Asymmetric saddle points with varying curvature
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**3 - 3 * x_norm[i]) * np.cos(2 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Cross-term with asymmetric interaction and phase modulation
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.sin(x_norm[i] + x_norm[i+1]) * np.cos(x_norm[i] - x_norm[i+1]) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Chaotic perturbation with non-linear coupling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x_norm[i]) * np.cos(12 * x_norm[i]) * np.sin(7 * x_norm[i]**2) * np.exp(-0.3 * np.abs(x_norm[i]))
        
        # Shifted global optimum with additional harmonic components
        shift = 0.5 * np.sum((x_norm - 0.2)**2 + 0.3 * np.sin(5 * x_norm)**2)
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.2 * sinusoidal + 0.8 * rbf + 1.5 * saddle + 0.6 * cross_term + 1.0 * chaotic + 0.4 * shift