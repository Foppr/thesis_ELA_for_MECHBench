import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Strengthened polynomial base with chaotic exponents
        exponents = np.linspace(3.5, 7.0, self.dim)
        f_val = np.sum(1.2 * (np.abs(x_norm)**exponents))
        
        # Chaotic trigonometric perturbations with variable frequencies and amplitudes
        freqs = np.linspace(4.0, 8.0, self.dim)
        f_val += np.sum(2.5 * np.sin(freqs * np.pi * x_norm) * np.cos(freqs * 0.5 * np.pi * x_norm))
        
        # Enhanced Gaussian attraction with chaotic center distribution
        gaussian_penalty = 0.0
        centers = np.sin(np.linspace(0, 2*np.pi, 9)) * 0.8
        for c in centers:
            gaussian_penalty += 2.0 * np.exp(-20 * np.sum((x_norm - c)**2))
        
        f_val += gaussian_penalty
        
        # Extended cross-dimensional interactions with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = np.sin(2.0 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(1.2 * np.pi * (x_norm[i] - x_norm[j]))
                cross_term += 0.7 * coupling
        f_val += cross_term
        
        # Adaptive penalty term to sharpen global minimum curvature
        f_val += 0.3 * np.sum(np.abs(x_norm)**4.0)
        
        return f_val