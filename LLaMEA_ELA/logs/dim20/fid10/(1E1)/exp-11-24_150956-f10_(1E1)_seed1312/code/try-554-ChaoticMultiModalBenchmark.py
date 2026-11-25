import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic dynamics
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic logistic map component with time-delayed feedback
        chaotic = np.zeros(self.dim)
        for i in range(self.dim):
            if i == 0:
                chaotic[i] = self.a * x_scaled[i] * (1 - x_scaled[i])
            else:
                chaotic[i] = self.a * x_scaled[i] * (1 - x_scaled[i]) + self.b * chaotic[i-1] * np.sin(self.c * x_scaled[i-1])
        
        # Fractional Brownian motion-like correlation structure
        fbm = np.zeros(self.dim)
        for i in range(self.dim):
            fbm[i] = np.sum([np.sin((j+1) * x_scaled[i]) * (0.5 ** (abs(i-j))) for j in range(self.dim)])
        
        # Saddle-point dominated regions with polynomial potential wells
        saddle = np.zeros(self.dim)
        for i in range(self.dim):
            saddle[i] = (x_scaled[i]**4 - 2*x_scaled[i]**2 + 0.5) * np.cos(3*x_scaled[i])
        
        # Multi-scale sinusoidal modulation with varying amplitudes and frequencies
        modulated = np.sum(np.sin(10.0 * x_scaled**2) * np.cos(7.0 * x_scaled**3) + 
                          0.6 * np.sin(15.0 * x_scaled**4) * np.cos(12.0 * x_scaled**5))
        
        # Cross-dimensional coupling with exponential interaction terms
        cross = np.sum(np.exp(-2.0 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                      np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                      0.5 * np.exp(-3.0 * (x_scaled[:-2]**2 + x_scaled[2:]**2)) * 
                      np.cos(4.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric landscape with weighted sum of chaotic and harmonic components
        return 0.4 * np.sum(chaotic**2) + 0.3 * np.sum(saddle) + 0.2 * modulated + 0.1 * cross + 2.1