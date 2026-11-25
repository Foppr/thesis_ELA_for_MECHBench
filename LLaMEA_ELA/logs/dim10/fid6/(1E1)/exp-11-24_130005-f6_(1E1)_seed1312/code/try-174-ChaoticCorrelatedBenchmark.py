import numpy as np

class ChaoticCorrelatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base chaotic component with exponential decay
        chaotic = 0.0
        for i in range(self.dim):
            # Exponentially decaying chaotic terms
            chaotic += np.exp(-0.1 * i) * np.sin(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i])
        
        # Multi-modal structure with sinusoidal coupling
        modal = 0.0
        for i in range(self.dim):
            # Sinusoidal coupling with neighboring dimensions
            coupling = 0.0
            for j in range(max(0, i-2), min(i+3, self.dim)):
                if i != j:
                    coupling += np.sin(x_scaled[i] - x_scaled[j]) * np.exp(-0.5 * (i-j)**2)
            modal += (1.0 + 0.5 * np.sin(x_scaled[i])) * coupling
        
        # Correlated noise component with dimensionally varying strength
        noise = 0.0
        for i in range(self.dim):
            # Correlated Gaussian noise with varying variance
            var = 0.1 + 0.2 * np.sin(i * 0.3)
            noise += np.random.normal(0, var) * np.cos(x_scaled[i] * 1.5)
        
        # Self-interaction with exponential decay and sinusoidal modulation
        interaction = 0.0
        for i in range(self.dim):
            # Exponential decay with sinusoidal modulation
            mod = 1.0 + 0.3 * np.sin(i * 0.7)
            interaction += mod * np.exp(-0.2 * i) * (x_scaled[i]**2 + x_scaled[i]**4)
        
        # Boundary attraction with exponentially increasing strength
        boundary = 0.0
        for i in range(self.dim):
            # Exponentially increasing attraction to boundaries
            strength = 2.0 * np.exp(0.1 * i)
            boundary += strength * (np.abs(x_scaled[i]) - 1.0)**2
        
        # Combined function with carefully tuned weights
        return 1.2 * chaotic + 0.8 * modal + 0.3 * noise + 0.6 * interaction + 0.4 * boundary