import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = 0.3 * np.sum(x**2)
        
        # Chaotic gradient modulation with sinusoidal perturbations
        for i in range(self.dim):
            f_val += 0.5 * np.sin(2 * x[i]) * np.cos(1.5 * x[i])
            
        # Non-uniform Gaussian peaks with varying heights and widths
        peak_heights = np.linspace(0.5, 1.5, min(5, self.dim))
        peak_widths = 0.2 + 0.8 * np.sin(np.arange(self.dim) * 0.5)
        for i in range(min(len(peak_heights), self.dim)):
            f_val += peak_heights[i] * np.exp(-0.5 * ((x[i] - 2.0 * np.cos(i)) / peak_widths[i])**2)
            
        # Saddle point structure with asymmetric coupling
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.4 * (x[i]**2 - x[i+1]**2) * np.sin(0.3 * x[i+2])
                
        # Cross-dimensional polynomial interactions with variable exponents
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.25 * (x[i] * x[i+1])**1.5 * np.cos(0.4 * x[i])
                
        # High-frequency chaotic modulation with time-varying parameters
        freq_mod = 1.0
        for i in range(self.dim):
            freq_mod = 1 + 0.2 * np.sin(x[i] * (i + 1) * 3)
            f_val += 0.1 * np.sin(freq_mod * x[i] * 20)
            
        # Enhanced non-linearity with exponential scaling
        if self.dim >= 4:
            for i in range(self.dim - 3):
                f_val += 0.15 * np.exp(0.1 * x[i]) * np.cos(0.2 * x[i+1] * x[i+2])
                
        # Additional chaotic saddle point with coupling strength modulation
        if self.dim >= 4:
            for i in range(self.dim - 3):
                f_val += 0.2 * (x[i]**3 - 3*x[i]*x[i+1]**2) * np.sin(0.5 * x[i+2])
                
        return f_val