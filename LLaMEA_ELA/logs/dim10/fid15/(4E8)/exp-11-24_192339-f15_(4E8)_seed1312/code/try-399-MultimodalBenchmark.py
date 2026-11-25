import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with fractal scaling
        chaotic = 0
        for i in range(self.dim):
            # Fractal-like modulation with multiple frequencies
            freq_mod = 1.0 + 0.3 * np.sin(2 * x[i]) + 0.2 * np.sin(5 * x[i])
            chaotic += np.sin(freq_mod * x[i] * np.pi) * np.cos(0.5 * x[i]**2)
        
        # Dynamic ridge modulation with multi-scale interference
        ridge = 0
        for i in range(self.dim):
            # Multi-scale harmonic interference with varying amplitudes
            scale1 = 1.0 + 0.4 * np.sin(0.3 * x[i])
            scale2 = 1.0 + 0.3 * np.cos(0.7 * x[i] + self.dim * 0.1)
            ridge += (x[i]**2) * scale1 * scale2 * np.exp(-0.05 * x[i]**2)
        
        # Saddle point structure with enhanced cross-dimensional coupling
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Enhanced coupling with fractal-like interaction
                coupling = np.sin(0.5 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * x[i] * x[j])
                saddle += x[i] * x[j] * coupling
        
        # Multi-scale fractal coupling component
        fractal = 0
        for i in range(self.dim):
            # Fractal-like interaction with varying scales
            scale_factor = 1.0 + 0.25 * np.sin(3 * x[i]) + 0.15 * np.cos(7 * x[i])
            fractal += np.sin(scale_factor * x[i]) * np.cos(scale_factor * x[i] * 0.5)
        
        # Enhanced dynamic weighting based on dimension
        weight1 = 0.35 + 0.15 * np.sin(self.dim * 0.2)
        weight2 = 0.35 + 0.15 * np.cos(self.dim * 0.25)
        weight3 = 0.25 + 0.15 * np.sin(self.dim * 0.3)
        weight4 = 0.20 + 0.10 * np.cos(self.dim * 0.15)
        
        return weight1 * chaotic + weight2 * ridge + weight3 * saddle + weight4 * fractal