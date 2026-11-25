import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Spherical component with adaptive scaling
        spherical = 0.5 * np.sum(x**2) / self.dim
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 1.0 + 0.5 * np.sin(i * 0.3)
            sinusoidal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Gaussian radial basis functions with adaptive centers and widths
        gaussian = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.7)
            width = 1.0 + 0.3 * np.cos(i * 0.4)
            gaussian += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling += (x[i]**2 + x[j]**2) * np.sin(2 * (x[i] - x[j]))
        
        # Adaptive dimension weighting based on position
        weight = 0.0
        for i in range(self.dim):
            weight += (1.0 + 0.5 * np.tanh(x[i])) * x[i]**3
        
        # Multi-scale chaotic component with dynamic phase shifts
        chaotic = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.2) * np.cos(i * 0.1)
            chaotic += np.sin(5 * x[i] + phase) * np.cos(3 * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric landscape with piecewise polynomial terms
        asymmetric = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asymmetric += 0.4 * x[i]**3 + 0.2 * x[i]**2
            else:
                asymmetric += 0.6 * x[i]**4 - 0.1 * x[i]**2
        
        # Combined fitness with adaptive scaling factors
        return spherical + 0.8 * sinusoidal + 0.5 * gaussian + 0.3 * coupling + 0.2 * weight + 0.6 * chaotic + 0.4 * asymmetric