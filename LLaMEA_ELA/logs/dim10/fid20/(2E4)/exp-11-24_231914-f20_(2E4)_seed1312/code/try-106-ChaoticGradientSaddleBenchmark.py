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
        
        # Chaotic gradient component with enhanced saddle point interactions
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Enhanced saddle point modulation using hyperbolic functions
            chaotic_grad += np.tanh(freq * x[i]) * np.cos(freq * x[i]**2) * \
                           (1.0 + 0.4 * np.sin(3 * x[i]) + 0.2 * np.cos(5 * x[i]))
        
        # Multi-scale harmonic modulations with varying amplitudes and phase shifts
        harmonics = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine sine and cosine with exponential decay and phase modulation
            harmonics += (np.sin(freq * x[i]) * np.cos(freq * x[i]) * 
                         np.exp(-0.2 * np.abs(x[i])) + 
                         0.5 * np.sin(2 * freq * x[i]) * np.cos(1.5 * freq * x[i]) * 
                         np.exp(-0.1 * x[i]**2) + 
                         0.3 * np.sin(freq * x[i] + 0.5 * np.cos(2 * freq * x[i])) * 
                         np.exp(-0.15 * np.abs(x[i])))
        
        # Enhanced embedded saddle point landscape with asymmetric coupling
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += (x[i] * x[i+1] * np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) + 
                      0.3 * np.sin(x[i]) * np.cos(x[i+1]) * np.exp(-0.05 * np.abs(x[i] - x[i+1])) +
                      0.2 * np.tanh(x[i]) * np.sin(x[i+1]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2)))
        
        # High-frequency oscillatory component with enhanced discontinuity-inducing terms
        high_freq = 0.0
        for i in range(self.dim):
            # Introduce piecewise non-smooth behavior with enhanced irregularity
            if x[i] < 0:
                high_freq += np.sin(12 * x[i]) * np.exp(-0.5 * x[i]**2) + 0.1 * np.cos(15 * x[i])
            else:
                high_freq += np.cos(10 * x[i]) * np.exp(-0.3 * x[i]**2) + 0.1 * np.sin(13 * x[i])
        
        # Enhanced dimensional coupling with fractal-like scaling and additional irregularities
        coupling = 0.0
        for i in range(self.dim - 2):
            coupling += 0.5 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i+1]) * \
                       np.exp(-0.1 * (x[i+2]**2 + x[i]**2)) * (1 + 0.2 * np.sin(5 * x[i+2]) + 0.1 * np.cos(7 * x[i]))
        
        # Global modulation with enhanced chaotic phase shifts
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.6 * np.sin(3.0 * x[i] + 0.5 * np.sin(7 * x[i])) * \
                         np.cos(2.0 * x[i]) * np.exp(-0.15 * np.abs(x[i])) + \
                         0.2 * np.tanh(4 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced higher-order polynomial terms for ruggedness
        rugged = 0.0
        for i in range(self.dim - 1):
            rugged += (x[i]**4 + x[i+1]**4) * np.exp(-0.3 * (x[i] - x[i+1])**2) + \
                     0.5 * (x[i]**3 + x[i+1]**3) * np.exp(-0.2 * np.abs(x[i] - x[i+1]))
        
        # Enhanced fractal-like dimension coupling with asymmetric scaling
        fractal = 0.0
        for i in range(self.dim - 3):
            fractal += (np.sin(x[i]) * np.cos(x[i+1]) * 
                       np.exp(-0.2 * (x[i+2]**2 + x[i+3]**2)) * 
                       (1 + 0.1 * np.sin(4 * x[i]) * np.cos(3 * x[i+1])) * 
                       np.abs(x[i] - x[i+2]) + 
                       0.3 * np.sin(3 * x[i]) * np.cos(5 * x[i+1]) * 
                       np.exp(-0.1 * (x[i]**2 + x[i+1]**2)))
        
        # Enhanced asymmetric non-linear transformation for increased ruggedness
        asym = 0.0
        for i in range(self.dim):
            asym += (np.sin(x[i]**3) * np.cos(x[i]) * 
                    np.exp(-0.1 * np.abs(x[i])) + 
                    0.4 * np.tanh(2 * x[i]) * np.sin(3 * x[i]) * 
                    np.exp(-0.05 * x[i]**2) + 
                    0.2 * np.sin(4 * x[i]) * np.cos(2 * x[i]) * 
                    np.exp(-0.15 * np.abs(x[i])))
        
        # Enhanced novel high-frequency component with irregular oscillations
        novel_high_freq = 0.0
        for i in range(self.dim):
            novel_high_freq += (np.sin(15 * x[i]) * np.cos(8 * x[i]) * 
                               np.exp(-0.4 * x[i]**2) + 
                               0.7 * np.tanh(4 * x[i]) * np.sin(6 * x[i]) * 
                               np.exp(-0.2 * np.abs(x[i])) + 
                               0.3 * np.cos(18 * x[i]) * np.sin(9 * x[i]) * 
                               np.exp(-0.3 * x[i]**2))
        
        # Enhanced additional chaotic modulation with irregular frequency
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += (np.sin(2.3 * x[i] + 0.5 * np.cos(9 * x[i])) * 
                           np.cos(1.7 * x[i]) * 
                           np.exp(-0.1 * np.abs(x[i])) + 
                           0.4 * np.tanh(5 * x[i]) * np.sin(8 * x[i]) * 
                           np.exp(-0.2 * x[i]**2))
        
        # Enhanced additional chaotic phase shifts and irregularities
        irregularity = 0.0
        for i in range(self.dim):
            irregularity += (0.3 * np.sin(5 * x[i] + 0.2 * np.sin(11 * x[i])) * 
                           np.cos(4 * x[i]) * 
                           np.exp(-0.08 * np.abs(x[i])) + 
                           0.2 * np.tanh(3 * x[i]) * np.sin(7 * x[i]) * 
                           np.exp(-0.15 * x[i]**2) + 
                           0.1 * np.cos(14 * x[i]) * np.sin(6 * x[i]) * 
                           np.exp(-0.1 * x[i]**2))
        
        # Enhanced multi-peak chaotic modulation
        multi_peak = 0.0
        for i in range(self.dim):
            multi_peak += (np.sin(8 * x[i]) * np.cos(6 * x[i]) * 
                          np.exp(-0.25 * x[i]**2) + 
                          0.8 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * 
                          np.exp(-0.3 * np.abs(x[i])) + 
                          0.5 * np.tanh(5 * x[i]) * np.sin(4 * x[i]) * 
                          np.exp(-0.1 * x[i]**2) + 
                          0.3 * np.cos(16 * x[i]) * np.sin(7 * x[i]) * 
                          np.exp(-0.2 * np.abs(x[i])))
        
        # Combine all components with carefully tuned weights
        return base + 2.5 * chaotic_grad + 1.8 * harmonics + 1.2 * saddle + \
               1.5 * high_freq + 0.9 * coupling + 0.7 * global_mod + 0.8 * rugged + \
               1.0 * fractal + 0.6 * asym + 1.3 * novel_high_freq + 0.5 * chaotic_mod + \
               0.7 * irregularity + 0.9 * multi_peak