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
            freq1 = 4 * (i % 8 + 1)
            freq2 = 6 * (i % 6 + 1)
            result += 0.4 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Add asymmetric exponential barriers with different scaling factors
        for i in range(self.dim):
            barrier1 = 0.6 * np.exp(-0.25 * (x[i] - 1.8)**2) * np.sin(35 * x[i])
            barrier2 = 0.5 * np.exp(-0.35 * (x[i] + 2.2)**2) * np.cos(30 * x[i])
            result += barrier1 + barrier2
            
        # Add refined cross-dimensional saddle-point interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                saddle = 0.2 * (x[i]**2 - x[j]**2) * np.sin(20 * (x[i] + x[j]))
                result += saddle
                
        # Add multi-scale frequency modulation with recursive structure
        for i in range(self.dim):
            freq_mod = 12 * np.sin(6 * np.sin(4 * x[i])) * np.cos(8 * np.cos(3 * x[i]))
            result += 0.3 * freq_mod * np.exp(-0.08 * (x[i] - 0.7)**2)
            
        # Add asymmetric ridge coupling with exponential decay
        for i in range(self.dim):
            ridge = 0.4 * np.exp(-0.5 * np.abs(x[i])) * np.sin(25 * x[i]) * np.cos(15 * x[i])
            result += ridge
            
        # Add nested sinusoidal structures with varying phases
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(0.4 * x[i])
            result += 0.25 * np.sin(45 * x[i] + phase_shift) * np.cos(20 * x[i] - phase_shift)
            
        # Add enhanced conditioning through polynomial coupling with higher degree
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                poly_coupling = (x[i]**3 + x[j]**3) * np.sin(10 * (x[i] - x[j]))
                result += 0.15 * poly_coupling
                
        # Add enhanced chaotic modulation with irregular amplitude scaling
        for i in range(self.dim):
            chaotic = 0.22 * np.sin(70 * x[i]) * np.cos(35 * x[i]) * np.exp(-0.25 * (x[i] - 1.2)**2)
            result += chaotic
            
        # Add irregular multi-modal peaks with varying heights and sharper transitions
        for i in range(self.dim):
            peak = 0.3 * np.sin(55 * x[i]) * np.exp(-0.12 * (x[i] - 2.0)**2) + \
                   0.2 * np.cos(50 * x[i]) * np.exp(-0.18 * (x[i] + 1.5)**2)
            result += peak
            
        # Add final complex cross-dimensional interaction with sine-cosine coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.sin(25 * x[i]) * np.cos(20 * x[j]) * (x[i] - x[j])**4
                result += 0.1 * coupling
                
        return result