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
            freq = 2**(i % 3 + 1)
            amp = 1.0 + 0.3 * np.sin(i * 0.5)
            sinusoidal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Gaussian radial basis functions with adaptive centers and widths
        gaussian = 0.0
        for i in range(self.dim):
            center = 1.5 * np.sin(i * 0.6)
            width = 1.2 + 0.4 * np.cos(i * 0.3)
            gaussian += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(max(0, i-2), min(i+2, self.dim)):  # Reduced coupling range
                if i != j:
                    coupling += (x[i]**2 + x[j]**2) * np.sin(3 * (x[i] - x[j]))
        
        # Adaptive dimension weighting based on position
        weight = 0.0
        for i in range(self.dim):
            weight += (1.0 + 0.4 * np.tanh(x[i])) * x[i]**3
        
        # Multi-scale chaotic component with dynamic phase shifts
        chaotic = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.15) * np.cos(i * 0.2)
            chaotic += np.sin(4 * x[i] + phase) * np.cos(2 * x[i] + phase) * np.exp(-0.15 * x[i]**2)
        
        # Asymmetric landscape with piecewise polynomial terms
        asymmetric = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asymmetric += 0.3 * x[i]**3 + 0.1 * x[i]**2
            else:
                asymmetric += 0.5 * x[i]**4 - 0.05 * x[i]**2
        
        # Additional chaotic interaction term to increase complexity
        chaos_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                chaos_interaction += np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Combined fitness with adjusted scaling factors
        return spherical + 0.7 * sinusoidal + 0.6 * gaussian + 0.4 * coupling + 0.3 * weight + 0.5 * chaotic + 0.3 * asymmetric + 0.2 * chaos_interaction