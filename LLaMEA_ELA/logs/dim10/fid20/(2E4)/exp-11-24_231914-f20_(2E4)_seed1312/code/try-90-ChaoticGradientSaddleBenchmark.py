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
            # Enhanced saddle point modulation using hyperbolic and trigonometric functions
            chaotic_grad += np.tanh(freq * x[i]) * np.cos(freq * x[i]**2) * \
                           (1.0 + 0.5 * np.sin(3 * x[i]) + 0.3 * np.cos(5 * x[i]))
        
        # Multi-scale harmonic modulations with increased complexity and varying amplitudes
        harmonics = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine multiple sine and cosine terms with exponential decay
            harmonics += (np.sin(freq * x[i]) * np.cos(freq * x[i]) * 
                         np.exp(-0.3 * np.abs(x[i])) + 
                         0.5 * np.sin(2 * freq * x[i]) * np.cos(1.5 * freq * x[i]) * 
                         np.exp(-0.2 * x[i]**2) +
                         0.3 * np.sin(3 * freq * x[i]) * np.cos(2 * freq * x[i]) *
                         np.exp(-0.1 * np.abs(x[i])))
        
        # Enhanced saddle point landscape with asymmetric coupling and fractal scaling
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += (x[i] * x[i+1] * np.exp(-0.15 * (x[i]**2 + x[i+1]**2)) + 
                      0.4 * np.sin(x[i]) * np.cos(x[i+1]) * np.exp(-0.08 * np.abs(x[i] - x[i+1])) +
                      0.2 * np.tanh(x[i]) * np.tanh(x[i+1]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2)))
        
        # High-frequency oscillatory component with stronger discontinuity-inducing terms
        high_freq = 0.0
        for i in range(self.dim):
            # Introduce piecewise non-smooth behavior with more abrupt transitions
            if x[i] < -2:
                high_freq += np.sin(15 * x[i]) * np.exp(-0.6 * x[i]**2)
            elif x[i] < 2:
                high_freq += np.cos(12 * x[i]) * np.exp(-0.4 * x[i]**2)
            else:
                high_freq += np.sin(10 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Enhanced dimensional coupling with fractal-like scaling and chaotic interactions
        coupling = 0.0
        for i in range(self.dim - 2):
            coupling += 0.7 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i+1]) * \
                       np.exp(-0.15 * (x[i+2]**2 + x[i]**2)) * (1 + 0.3 * np.sin(5 * x[i+2]) + 
                       0.2 * np.cos(7 * x[i]))
        
        # Global modulation with chaotic phase shifts and higher-order terms
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.8 * np.sin(3.0 * x[i] + 0.5 * np.sin(7 * x[i]) + 
                         0.3 * np.cos(9 * x[i])) * np.cos(2.0 * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        
        # Add higher-order polynomial terms for increased ruggedness and complexity
        rugged = 0.0
        for i in range(self.dim - 1):
            rugged += (x[i]**4 + x[i+1]**4) * np.exp(-0.4 * (x[i] - x[i+1])**2) + \
                     0.5 * (x[i]**3 + x[i+1]**3) * np.exp(-0.2 * (x[i] + x[i+1])**2)
        
        # Add a fractal-like component for self-similar complexity
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.4 * np.sin(8 * x[i]) * np.cos(6 * x[i]) * \
                      np.exp(-0.1 * np.abs(x[i])) + 0.3 * np.tanh(4 * x[i]) * \
                      np.exp(-0.2 * x[i]**2)
        
        # Combine all components with carefully tuned weights
        return base + 2.0 * chaotic_grad + 1.5 * harmonics + 1.1 * saddle + \
               1.3 * high_freq + 0.9 * coupling + 0.7 * global_mod + 0.8 * rugged + 0.6 * fractal