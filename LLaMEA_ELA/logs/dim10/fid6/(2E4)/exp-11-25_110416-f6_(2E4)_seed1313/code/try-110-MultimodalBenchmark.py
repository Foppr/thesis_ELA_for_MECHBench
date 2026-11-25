import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add nested harmonic oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 3 * (i % 7 + 1)
            freq2 = 7 * (i % 5 + 1)
            result += 0.3 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Add asymmetric exponential barriers with different scaling factors
        for i in range(self.dim):
            barrier1 = 0.5 * np.exp(-0.2 * (x[i] - 1.5)**2) * np.sin(30 * x[i])
            barrier2 = 0.4 * np.exp(-0.3 * (x[i] + 2.0)**2) * np.cos(25 * x[i])
            result += barrier1 + barrier2
            
        # Add cross-dimensional saddle-point interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                saddle = 0.15 * (x[i]**2 - x[j]**2) * np.sin(15 * (x[i] + x[j]))
                result += saddle
                
        # Add multi-scale frequency modulation with recursive structure
        for i in range(self.dim):
            freq_mod = 10 * np.sin(5 * np.sin(3 * x[i])) * np.cos(7 * np.cos(2 * x[i]))
            result += 0.25 * freq_mod * np.exp(-0.05 * (x[i] - 0.5)**2)
            
        # Add asymmetric ridge coupling with exponential decay
        for i in range(self.dim):
            ridge = 0.3 * np.exp(-0.4 * np.abs(x[i])) * np.sin(20 * x[i]) * np.cos(12 * x[i])
            result += ridge
            
        # Add nested sinusoidal structures with varying phases
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.3 * x[i])
            result += 0.2 * np.sin(40 * x[i] + phase_shift) * np.cos(15 * x[i] - phase_shift)
            
        # Add enhanced conditioning through polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                poly_coupling = (x[i]**2 + x[j]**2) * np.sin(8 * (x[i] - x[j]))
                result += 0.1 * poly_coupling
                
        # Add chaotic modulation with irregular amplitude scaling
        for i in range(self.dim):
            chaotic = 0.18 * np.sin(67 * x[i]) * np.cos(33 * x[i]) * np.exp(-0.2 * (x[i] - 1.0)**2)
            result += chaotic
            
        # Add irregular multi-modal peaks with varying heights
        for i in range(self.dim):
            peak = 0.25 * np.sin(50 * x[i]) * np.exp(-0.1 * (x[i] - 1.8)**2) + \
                   0.15 * np.cos(45 * x[i]) * np.exp(-0.15 * (x[i] + 1.2)**2)
            result += peak
            
        # Add final complex cross-dimensional interaction with sine-cosine coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = np.sin(23 * x[i]) * np.cos(17 * x[j]) * (x[i] - x[j])**3
                result += 0.08 * coupling
                
        return result