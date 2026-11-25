import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        radial = np.sum(x**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Trigonometric coupling between dimensions
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Multimodal sine component with varying frequencies
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(3 * x[i]) * np.cos(7 * x[i]) + 0.5 * np.sin(11 * x[i])
            
        # Gaussian-like peaks with different centers and widths
        gaussian_peaks = 0
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                gaussian_peaks += np.exp(-0.5 * ((x[i] - centers[i]) / 1.5)**2) * np.sin(2 * x[i])
                
        # Asymmetric exponential decay component
        asym_decay = 0
        for i in range(self.dim):
            asym_decay += (np.exp(-0.3 * x[i]) - np.exp(-0.7 * x[i])) * np.cos(0.4 * x[i])
            
        # High-frequency oscillation component
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(15 * x[i]) * np.cos(23 * x[i]) * (1 + 0.3 * np.sin(x[i]))
            
        # Combine all components with different weights
        return (0.4 * radial + 
                0.3 * trig_coupling + 
                0.2 * multimodal + 
                0.15 * gaussian_peaks + 
                0.1 * asym_decay + 
                0.25 * high_freq + 
                3 * np.sum(np.cos(x)**2))