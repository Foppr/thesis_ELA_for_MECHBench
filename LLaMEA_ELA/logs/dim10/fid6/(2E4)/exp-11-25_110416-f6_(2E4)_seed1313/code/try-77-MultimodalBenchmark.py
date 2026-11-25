import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponential decay sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 7 ** (i % 9 + 1) + 0.1 * np.sin(0.5 * x[i])
            amp = 2.0 * np.exp(-0.4 * np.abs(x[i]))
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Add asymmetric ridge penalties with exponential scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 1.2 * np.exp(-0.6 * (x[i] - 1.5)**2) * (x[i] - 1.5)**5
            else:
                result += 1.0 * np.exp(-0.5 * (x[i] + 2.0)**2) * (x[i] + 2.0)**6
                
        # Add multi-scale chaotic interactions with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interaction = np.exp(-0.15 * (x[i]**2 + x[j]**2)) * np.sin(35 * (x[i] - x[j]) + 0.2 * x[i] * x[j])
                result += 0.3 * interaction
                
        # Add a novel hybrid exponential-sine structure with varying phase shifts
        for i in range(self.dim):
            phase_shift = 0.7 * np.sin(0.8 * x[i]) + 0.3 * np.cos(1.2 * x[i]) + 0.1 * np.sin(2.5 * x[i])
            result += 0.4 * np.exp(-0.25 * np.abs(x[i])) * np.sin(50 * x[i] + phase_shift)
            
        # Add irregular asymmetric peaks with non-uniform scaling
        for i in range(self.dim):
            peak1 = 0.5 * np.exp(-0.6 * (x[i] - 2.2)**2) * np.cos(35 * x[i]) + 0.05 * np.sin(10 * x[i])
            peak2 = 0.4 * np.exp(-0.4 * (x[i] + 2.8)**2) * np.sin(30 * x[i]) + 0.03 * np.cos(15 * x[i])
            result += peak1 + peak2
            
        # Add a complex multi-modal component with nested frequency patterns
        for i in range(self.dim):
            result += 0.35 * np.sin(75 * x[i]) * np.cos(40 * x[i]) * np.exp(-0.15 * x[i]**2) + \
                      0.25 * np.sin(50 * x[i]) * np.cos(25 * x[i]) * np.exp(-0.1 * x[i]**2) + \
                      0.1 * np.sin(90 * x[i]) * np.cos(30 * x[i])
            
        # Add a global structure with multiple local minima and enhanced non-linearity
        for i in range(self.dim):
            result += 0.4 * np.sin(20 * x[i])**4 + 0.3 * np.cos(15 * x[i])**3 + \
                      0.1 * np.sin(25 * x[i])**2
            
        # Add novel chaotic coupling terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(20 * (x[i] + x[j]) + 0.3 * x[i]**2) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                result += 0.25 * coupling
                
        # Add a complex hybrid exponential-sine term with dynamic amplitude modulation
        for i in range(self.dim):
            amp_mod = 1.5 * np.sin(0.5 * x[i])**2 + 0.5 + 0.2 * np.cos(1.5 * x[i])
            result += 0.3 * amp_mod * np.exp(-0.3 * np.abs(x[i])) * np.sin(60 * x[i] + 0.4 * np.cos(20 * x[i]) + 0.1 * np.sin(25 * x[i]))
            
        return result