import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with varying frequencies
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            chaotic += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Adaptive elliptic contour with dynamic eccentricity
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.5 * np.sin(x[i])
            elliptic += (x[i] ** 2) / (eccentricity ** 2)
        
        # Dynamic peak valleys with varying depths and widths
        peaks_valleys = 0.0
        for i in range(self.dim):
            depth = 2.0 + np.sin(0.5 * x[i])
            width = 1.0 + 0.3 * np.cos(x[i])
            peaks_valleys += depth * np.exp(-0.5 * (x[i] ** 2) / (width ** 2)) - 0.5 * np.sin(3 * x[i])
        
        # Cross-dimensional interference with cosine coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.cos(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j]) ** 2)
                cross += coupling
        
        # Asymmetric gradient deception with polynomial and exponential mixing
        deception = 0.0
        for i in range(self.dim):
            deception += (x[i] ** 4 - 3 * x[i] ** 3 + 2 * x[i] ** 2) * np.exp(-0.5 * x[i] ** 2)
        
        # Resonance peaks with dynamic frequency modulation
        resonance = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.3 * x[i])
            resonance += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) * (1.0 + 0.2 * np.abs(x[i]))
        
        # Combine all components with varying weights
        return 0.2 * chaotic + 0.15 * elliptic + 0.25 * peaks_valleys + 0.2 * cross + 0.1 * deception + 0.1 * resonance