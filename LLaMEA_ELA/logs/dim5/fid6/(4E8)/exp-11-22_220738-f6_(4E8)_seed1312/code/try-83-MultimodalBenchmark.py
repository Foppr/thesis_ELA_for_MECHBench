import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = 0.5 * np.sum(x**2)
        
        # Enhanced sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.4 * np.sin(3 * np.pi * x[i]) * np.cos(0.7 * x[i])
            
        # Modified radial basis function peaks with dynamic positioning
        peak_positions = np.linspace(-4.5, 4.5, min(6, self.dim))
        for i in range(len(peak_positions)):
            if i < self.dim:
                pos = peak_positions[i % len(peak_positions)]
                width = 0.3 + 0.7 * np.sin(i * 0.4)
                f_val += 0.5 * np.exp(-0.5 * ((x[i] - pos) / width)**2)
                
        # Cross-dimensional polynomial coupling with stronger interaction terms
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.2 * (x[i]**2 + x[i+1]**2) * np.sin(0.5 * x[i] * x[i+1])
                
        # Saddle point structure with asymmetric behavior and enhanced complexity
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.3 * (x[i] * x[i+1] - x[i+2]**2) * np.cos(0.5 * x[i])
                
        # Additional high-frequency chaotic modulation with increased complexity
        freq_mod = 1.0
        for i in range(self.dim):
            freq_mod = 1 + 0.3 * np.sin(x[i] * freq_mod * 2)
            f_val += 0.08 * np.sin(freq_mod * x[i] * 15)
            
        # Cross-dimensional interaction enhancement with modified coefficients
        if self.dim >= 4:
            for i in range(self.dim - 3):
                f_val += 0.2 * x[i] * x[i+1] * x[i+2] * np.cos(0.2 * x[i+3])
                
        # Introduce a chaotic saddle point with modified coupling
        if self.dim >= 4:
            for i in range(self.dim - 3):
                f_val += 0.1 * (x[i]**3 - 3*x[i]*x[i+1]**2) * np.sin(0.3 * x[i+2])
                
        return f_val