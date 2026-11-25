import numpy as np

class HybridChaoticStepBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        spherical = 0.1 * np.sum(x**2)
        
        # Step function component with dynamic thresholds
        step = 0
        for i in range(self.dim):
            threshold = 1.5 * np.sin(0.3 * i) + 0.5 * np.cos(0.2 * i)
            step += (x[i] > threshold) * (x[i] - threshold)**2
        
        # Sinusoidal component with varying frequencies and amplitudes
        sinusoidal = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.4 * i)
            amp = 1.0 + 0.3 * np.cos(0.3 * i)
            sinusoidal += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric scaling component
        asymmetric = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.5 * i) * np.cos(0.3 * i)
            if x[i] >= 0:
                asymmetric += scale_factor * x[i]**2
            else:
                asymmetric += (scale_factor * 0.5) * x[i]**2
        
        # Dynamic conditioning component with chaotic modulation
        conditioning = 0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.6 * np.sin(0.2 * i) * np.cos(0.4 * i)
            conditioning += cond_factor * x[i]**4
        
        # Multi-scale interaction component
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.5 + 0.2 * np.sin(0.3 * (i + j))
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Chaotic modulation component
        chaotic = 0
        for i in range(self.dim):
            chaos_factor = 0.3 * np.sin(0.7 * i) * np.cos(0.5 * i)
            chaotic += np.sin(x[i] + chaos_factor) * np.cos(x[i] - chaos_factor) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with dynamic weights
        coupling = 0
        for i in range(self.dim):
            weight = 0.8 + 0.2 * np.sin(0.4 * i)
            coupling += weight * (np.abs(x[i])**(1.5 + 0.3 * np.cos(0.2 * i)))
        
        # Combine all components
        return (spherical * 0.6 +
                step * 0.7 +
                sinusoidal * 0.5 +
                asymmetric * 0.4 +
                conditioning * 0.3 +
                interaction * 0.25 +
                chaotic * 0.35 +
                coupling * 0.3)