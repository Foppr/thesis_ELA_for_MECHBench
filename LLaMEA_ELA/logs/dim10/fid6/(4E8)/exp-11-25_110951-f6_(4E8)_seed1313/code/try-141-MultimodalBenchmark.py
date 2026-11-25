import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base separable function with enhanced conditioning and nonlinear interactions
        base = np.sum(0.5 * x_norm**2 + 0.3 * np.sin(7 * x_norm) + 0.1 * x_norm**4)
        
        # Non-separable correlation term with multi-scale chaotic components
        r_squared = np.sum(x_norm**2)
        correlation = -35 * np.exp(-0.2 * np.sqrt(r_squared)) - \
                      np.exp(np.mean(np.cos(7 * np.pi * x_norm))) + 35 + np.e + \
                      0.6 * np.sin(15 * np.mean(x_norm)) * np.cos(11 * np.mean(x_norm))
        
        # Helicoidal distortion with varying pitch and phase modulation
        helix = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[(i+1) % self.dim], x_norm[i])
            helix += (np.sin(11 * angle + i * 0.7) * np.cos(11 * angle + i * 0.7) +
                     0.8 * np.sin(15 * angle + i * 0.5) * np.cos(15 * angle + i * 0.5) +
                     0.4 * np.sin(19 * angle + i * 0.3) * np.cos(19 * angle + i * 0.3))
        
        # Multi-scale sinusoidal modulation with exponential decay and cubic interactions
        modulated = np.sum(np.sin(20 * x_norm) * np.cos(17 * x_norm) * 
                          np.sin(12 * x_norm) * np.cos(9 * x_norm) * 
                          np.exp(-0.15 * np.abs(x_norm)) * (1 + 0.15 * x_norm**3))
        
        # Fractal-like basin with nested minima and chaotic perturbations
        r = np.sqrt(r_squared)
        fractal = 1.2 * np.exp(-r**2) + 0.7 * np.sin(20 * r) * np.cos(12 * r) + \
                 0.4 * np.sin(30 * r) * np.cos(18 * r) + 0.2 * np.sin(40 * r) + \
                 0.25 * np.sin(25 * r) * np.cos(20 * r) * np.exp(-0.07 * r**2)
        
        # Cross-dimensional coupling with polynomial interaction and chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            coupling += x_norm[i]**3 * x_norm[(i+3) % self.dim] * np.sin(13 * x_norm[i])
        coupling = coupling / self.dim
        
        # Chaotic perturbation with higher frequency and stronger nonlinearity
        perturbation = 0.2 * np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * 
                                  np.exp(-0.1 * np.abs(x_norm)) * (1 + 0.08 * x_norm**4))
        
        # Combined function with adaptive scaling
        return 0.4 * base + 0.35 * correlation + \
               0.25 * helix + 0.2 * modulated + fractal + 0.15 * coupling + perturbation