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
        
        # Fractal-like dimension coupling with asymmetric scaling
        fractal = 0.0
        for i in range(self.dim - 3):
            fractal += (np.sin(x[i]) * np.cos(x[i+1]) * 
                       np.exp(-0.2 * (x[i+2]**2 + x[i+3]**2)) * 
                       (1 + 0.1 * np.sin(4 * x[i]) * np.cos(3 * x[i+1])) * 
                       np.abs(x[i] - x[i+2]))
        
        # Asymmetric non-linear transformation for increased ruggedness
        asym = 0.0
        for i in range(self.dim):
            asym += (np.sin(x[i]**3) * np.cos(x[i]) * 
                    np.exp(-0.1 * np.abs(x[i])) + 
                    0.4 * np.tanh(2 * x[i]) * np.sin(3 * x[i]) * 
                    np.exp(-0.05 * x[i]**2))
        
        # Novel high-frequency component with irregular oscillations
        novel_high_freq = 0.0
        for i in range(self.dim):
            novel_high_freq += (np.sin(15 * x[i]) * np.cos(8 * x[i]) * 
                               np.exp(-0.4 * x[i]**2) + 
                               0.7 * np.tanh(4 * x[i]) * np.sin(6 * x[i]) * 
                               np.exp(-0.2 * np.abs(x[i])))
        
        # Additional chaotic modulation with irregular frequency
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += (np.sin(2.3 * x[i] + 0.5 * np.cos(9 * x[i])) * 
                           np.cos(1.7 * x[i]) * 
                           np.exp(-0.1 * np.abs(x[i])))
        
        # Add additional chaotic phase shifts and irregularities
        irregularity = 0.0
        for i in range(self.dim):
            irregularity += (0.3 * np.sin(5 * x[i] + 0.2 * np.sin(11 * x[i])) * 
                           np.cos(4 * x[i]) * 
                           np.exp(-0.08 * np.abs(x[i])) + 
                           0.2 * np.tanh(3 * x[i]) * np.sin(7 * x[i]) * 
                           np.exp(-0.15 * x[i]**2))
        
        # Add multi-peak chaotic modulation
        multi_peak = 0.0
        for i in range(self.dim):
            multi_peak += (np.sin(8 * x[i]) * np.cos(6 * x[i]) * 
                          np.exp(-0.25 * x[i]**2) + 
                          0.8 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * 
                          np.exp(-0.3 * np.abs(x[i])) + 
                          0.5 * np.tanh(5 * x[i]) * np.sin(4 * x[i]) * 
                          np.exp(-0.1 * x[i]**2))
        
        # Combine all components with carefully tuned weights
        return base + 2.0 * chaotic_grad + 1.5 * harmonics + 1.0 * saddle + \
               1.3 * high_freq + 0.8 * coupling + 0.6 * global_mod + 0.7 * rugged + \
               0.9 * fractal + 0.5 * asym + 1.2 * novel_high_freq + 0.4 * chaotic_mod + \
               0.6 * irregularity + 0.8 * multi_peak