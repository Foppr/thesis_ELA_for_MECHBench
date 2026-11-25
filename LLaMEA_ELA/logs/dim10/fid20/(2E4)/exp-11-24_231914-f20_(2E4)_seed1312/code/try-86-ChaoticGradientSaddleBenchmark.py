import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic frequencies for multi-scale interactions
        self.frequencies = [1.0, 2.5, 4.0, 5.5, 7.0][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Chaotic gradient component with saddle point interactions
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Saddle point modulation using hyperbolic functions
            chaotic_grad += np.tanh(freq * x[i]) * np.cos(freq * x[i]**2) * \
                           (1.0 + 0.3 * np.sin(3 * x[i]))
        
        # Multi-scale harmonic modulations with varying amplitudes
        harmonics = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine sine and cosine with exponential decay
            harmonics += (np.sin(freq * x[i]) * np.cos(freq * x[i]) * 
                         np.exp(-0.2 * np.abs(x[i])) + 
                         0.5 * np.sin(2 * freq * x[i]) * np.cos(1.5 * freq * x[i]) * 
                         np.exp(-0.1 * x[i]**2))
        
        # Embedded saddle point landscape with asymmetric coupling
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += (x[i] * x[i+1] * np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) + 
                      0.3 * np.sin(x[i]) * np.cos(x[i+1]) * np.exp(-0.05 * np.abs(x[i] - x[i+1])))
        
        # High-frequency oscillatory component with discontinuity-inducing terms
        high_freq = 0.0
        for i in range(self.dim):
            # Introduce piecewise non-smooth behavior
            if x[i] < 0:
                high_freq += np.sin(12 * x[i]) * np.exp(-0.5 * x[i]**2)
            else:
                high_freq += np.cos(10 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Dimensional coupling with exponential decay and fractal-like scaling
        coupling = 0.0
        for i in range(self.dim - 2):
            coupling += 0.5 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i+1]) * \
                       np.exp(-0.1 * (x[i+2]**2 + x[i]**2)) * (1 + 0.2 * np.sin(5 * x[i+2]))
        
        # Global modulation with chaotic phase shifts
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.6 * np.sin(3.0 * x[i] + 0.5 * np.sin(7 * x[i])) * \
                         np.cos(2.0 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
        
        # Add higher-order polynomial terms for ruggedness
        rugged = 0.0
        for i in range(self.dim - 1):
            rugged += (x[i]**4 + x[i+1]**4) * np.exp(-0.3 * (x[i] - x[i+1])**2)
        
        # Combine all components with carefully tuned weights
        return base + 1.8 * chaotic_grad + 1.2 * harmonics + 0.9 * saddle + \
               1.1 * high_freq + 0.7 * coupling + 0.5 * global_mod + 0.6 * rugged