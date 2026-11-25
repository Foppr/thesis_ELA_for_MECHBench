import numpy as np

class AdaptiveRidgeCosineLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial potential components with varying degrees
        for i in range(self.dim):
            # Varying polynomial degrees and coefficients
            degree = 2 + (i % 4)  # Degrees 2 to 5
            coeff = 1.0 + 0.3 * np.sin(0.5 * i)
            result += coeff * (x[i] ** degree)
        
        # Cosine modulation with adaptive frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.cos(i)
            amp = 1.0 + 0.2 * np.sin(0.3 * i)
            result += amp * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Ridge structures with adaptive widths and heights
        for i in range(self.dim):
            ridge_height = 0.5 + 0.5 * np.sin(0.4 * i)
            ridge_width = 0.3 + 0.2 * np.cos(0.6 * i)
            result += ridge_height * np.exp(-0.5 * ((x[i] - 1.0) / ridge_width)**2)
        
        # Cross-dimensional coupling with periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_freq = 3.0 + 0.4 * np.sin(0.2 * (i + j))
                coupling_amp = 0.7 + 0.3 * np.cos(0.3 * i)
                result += coupling_amp * np.sin(coupling_freq * (x[i] + x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Asymmetric saddle points with varying sharpness
        for i in range(self.dim):
            sharpness = 1.0 + 0.4 * np.sin(0.5 * i)
            result += 0.3 * (x[i] - 2.0)**2 * np.exp(-sharpness * (x[i] - 2.0)**2)
        
        # Global scaling factor based on dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        # Add noise component with varying intensity
        noise_intensity = 0.05 + 0.02 * np.sin(0.1 * self.dim)
        noise = np.sum(np.random.normal(0, 1, self.dim)) * noise_intensity
        result += noise
        
        return result