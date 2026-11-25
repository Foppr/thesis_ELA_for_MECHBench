import numpy as np

class ChaoticPolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial base with varying degrees and chaotic coefficients
        f1 = np.sum(0.5 * x_scaled**8 + 0.3 * x_scaled**7 - 0.2 * x_scaled**6 + 0.1 * x_scaled**5 + 
                   0.05 * x_scaled**4 - 0.02 * x_scaled**3 + 0.01 * x_scaled**2)
        
        # Sinusoidal wave interference creating complex local minima
        f2 = np.sum(np.sin(25 * x_scaled) * np.cos(20 * x_scaled) * 
                   np.sin(15 * x_scaled) * np.cos(10 * x_scaled))
        
        # Cross-dimensional coupling with chaotic interaction weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                weight = 0.5 + 0.3 * np.sin(i * j * 1.7) * np.cos((i + j) * 0.9)
                f3 += weight * np.sin(x_scaled[i]) * np.sin(x_scaled[j]) * (x_scaled[i]**2 + x_scaled[j]**2)
        
        # Fractal-like self-similarity through recursive sinusoidal modulation
        f4 = 0.0
        for i in range(self.dim):
            mod_freq = 10 + 5 * np.sin(i * 0.8)
            f4 += np.sin(mod_freq * x_scaled[i]) * np.cos(mod_freq * x_scaled[i] * 0.5) * \
                  np.sin(mod_freq * x_scaled[i] * 0.25) * np.cos(mod_freq * x_scaled[i] * 0.125)
        
        # Boundary avoidance with chaotic penalty exponents
        f5 = np.sum(0.7 * np.abs(x_scaled)**3.8 + 0.4 * np.abs(x_scaled)**2.9 + 0.2 * np.abs(x_scaled)**1.5)
        
        # High-frequency chaotic oscillation
        f6 = np.sum(np.sin(100 * x_scaled + np.cos(50 * x_scaled)) * 
                   np.cos(90 * x_scaled + np.sin(45 * x_scaled)))
        
        # Adaptive polynomial with random coefficients for each dimension
        f7 = 0.0
        for i in range(self.dim):
            coeff = 0.1 + 0.2 * np.sin(i * 1.3)
            f7 += coeff * (x_scaled[i]**6 + x_scaled[i]**4 + x_scaled[i]**2)
        
        # Combined chaotic structure
        return f1 + f2 + f3 + f4 + f5 + f6 + 0.1 * f7