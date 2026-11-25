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
            freq = 7 ** (i % 6 + 1)
            amp = 2.0 * np.exp(-0.25 * np.abs(x[i]))
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Add asymmetric ridge penalties with exponential scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 1.0 * np.exp(-0.4 * (x[i] - 1.5)**2) * (x[i] - 1.5)**3
            else:
                result += 0.9 * np.exp(-0.3 * (x[i] + 2.0)**2) * (x[i] + 2.0)**4
                
        # Add multi-scale chaotic interactions with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interaction = np.exp(-0.15 * (x[i]**2 + x[j]**2)) * np.sin(25 * (x[i] - x[j]))
                result += 0.25 * interaction
                
        # Add a novel hybrid exponential-sine structure with varying phase shifts
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(0.8 * x[i])
            result += 0.35 * np.exp(-0.15 * np.abs(x[i])) * np.sin(35 * x[i] + phase_shift)
            
        # Add irregular asymmetric peaks with non-uniform scaling
        for i in range(self.dim):
            peak1 = 0.45 * np.exp(-0.4 * (x[i] - 2.2)**2) * np.cos(28 * x[i])
            peak2 = 0.35 * np.exp(-0.25 * (x[i] + 2.3)**2) * np.sin(22 * x[i])
            result += peak1 + peak2
            
        # Add a complex multi-modal component with nested frequency patterns
        for i in range(self.dim):
            result += 0.3 * np.sin(55 * x[i]) * np.cos(40 * x[i]) * np.exp(-0.12 * x[i]**2) + \
                      0.2 * np.sin(35 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Add a global structure with multiple local minima and enhanced non-linearity
        for i in range(self.dim):
            result += 0.35 * np.sin(20 * x[i])**3 + 0.25 * np.cos(15 * x[i])**2
            
        return result