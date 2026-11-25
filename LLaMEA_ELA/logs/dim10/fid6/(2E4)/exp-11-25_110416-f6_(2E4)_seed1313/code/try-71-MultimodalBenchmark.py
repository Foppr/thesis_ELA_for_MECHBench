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
            freq = 5 ** (i % 6 + 1)  # Slightly reduced frequency range
            amp = 1.3 * np.exp(-0.35 * np.abs(x[i]))  # Slightly adjusted amplitude decay
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Add asymmetric ridge penalties with exponential scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.9 * np.exp(-0.55 * (x[i] - 1.1)**2) * (x[i] - 1.1)**4  # Slightly adjusted parameters
            else:
                result += 0.6 * np.exp(-0.45 * (x[i] + 1.9)**2) * (x[i] + 1.9)**5  # Slightly adjusted parameters
                
        # Add multi-scale chaotic interactions with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced interaction range
                interaction = np.exp(-0.12 * (x[i]**2 + x[j]**2)) * np.sin(35 * (x[i] - x[j]))  # Slightly modified parameters
                result += 0.25 * interaction
                
        # Add a novel hybrid exponential-sine structure with varying phase shifts
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(0.6 * x[i])  # Slightly adjusted phase shift
            result += 0.35 * np.exp(-0.22 * np.abs(x[i])) * np.sin(42 * x[i] + phase_shift)  # Slightly modified frequency and amplitude
            
        # Add irregular asymmetric peaks with non-uniform scaling
        for i in range(self.dim):
            peak1 = 0.35 * np.exp(-0.55 * (x[i] - 2.1)**2) * np.cos(32 * x[i])  # Slightly adjusted parameters
            peak2 = 0.25 * np.exp(-0.35 * (x[i] + 2.6)**2) * np.sin(27 * x[i])  # Slightly adjusted parameters
            result += peak1 + peak2
            
        # Add a complex multi-modal component with nested frequency patterns
        for i in range(self.dim):
            result += 0.28 * np.sin(68 * x[i]) * np.cos(37 * x[i]) * np.exp(-0.12 * x[i]**2) + \
                      0.18 * np.sin(48 * x[i]) * np.cos(22 * x[i]) * np.exp(-0.06 * x[i]**2)  # Slightly adjusted parameters
            
        # Add a global structure with multiple local minima and enhanced non-linearity
        for i in range(self.dim):
            result += 0.35 * np.sin(19 * x[i])**3 + 0.25 * np.cos(13 * x[i])**2  # Slightly adjusted parameters
            
        return result