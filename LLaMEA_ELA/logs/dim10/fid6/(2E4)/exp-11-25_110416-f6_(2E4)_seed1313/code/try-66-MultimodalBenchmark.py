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
            freq = 5 ** (i % 7 + 1)
            amp = 1.5 * np.exp(-0.3 * np.abs(x[i]))
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Add asymmetric ridge penalties with exponential scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.8 * np.exp(-0.5 * (x[i] - 1.2)**2) * (x[i] - 1.2)**4
            else:
                result += 0.7 * np.exp(-0.4 * (x[i] + 1.8)**2) * (x[i] + 1.8)**5
                
        # Add multi-scale chaotic interactions with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                interaction = np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(30 * (x[i] - x[j]))
                result += 0.2 * interaction
                
        # Add a novel hybrid exponential-sine structure with varying phase shifts
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.7 * x[i])
            result += 0.3 * np.exp(-0.2 * np.abs(x[i])) * np.sin(40 * x[i] + phase_shift)
            
        # Add irregular asymmetric peaks with non-uniform scaling
        for i in range(self.dim):
            peak1 = 0.4 * np.exp(-0.5 * (x[i] - 2.0)**2) * np.cos(30 * x[i])
            peak2 = 0.3 * np.exp(-0.3 * (x[i] + 2.5)**2) * np.sin(25 * x[i])
            result += peak1 + peak2
            
        # Add a complex multi-modal component with nested frequency patterns
        for i in range(self.dim):
            result += 0.25 * np.sin(65 * x[i]) * np.cos(35 * x[i]) * np.exp(-0.1 * x[i]**2) + \
                      0.15 * np.sin(45 * x[i]) * np.cos(20 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Add a global structure with multiple local minima and enhanced non-linearity
        for i in range(self.dim):
            result += 0.3 * np.sin(18 * x[i])**3 + 0.2 * np.cos(12 * x[i])**2
            
        return result